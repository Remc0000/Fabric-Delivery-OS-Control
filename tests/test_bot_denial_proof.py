import contextlib
import io
import os
from pathlib import Path
import textwrap
import unittest
from unittest.mock import Mock, patch


WORKFLOW = Path(__file__).resolve().parents[1] / ".github" / "workflows" / "bot-denial-proof.yml"


class BotDenialProofTests(unittest.TestCase):
    def setUp(self):
        source = WORKFLOW.read_text(encoding="utf-8")
        script = source.split("python3 - <<'PY'\n", 1)[1].rsplit("          PY", 1)[0]
        self.namespace = {"__name__": "workflow_test"}
        with patch.dict(
            os.environ,
            {
                "GITHUB_API_URL": "https://api.github.com",
                "GITHUB_REPOSITORY": "example/control",
                "GITHUB_RUN_ID": "1",
            },
        ):
            exec(compile(textwrap.dedent(script), str(WORKFLOW), "exec"), self.namespace)
        self.gate = {
            "environment": {"id": 42, "name": "approval-bot-test"},
            "current_user_can_approve": False,
        }
        self.waiting = {
            "jobs": [{
                "name": "Human-gated synthetic action",
                "status": "waiting",
                "runner_name": None,
                "steps": [],
            }],
        }
        self.denied = (403, {"message": "Resource not accessible by integration"})

    def run_probe(self, responses):
        request = Mock(side_effect=responses)
        self.namespace["request_json"] = request
        with contextlib.redirect_stdout(io.StringIO()), patch.object(
            self.namespace["time"], "sleep"
        ):
            self.namespace["main"]()
        return request

    def test_classified_refusal_keeps_same_gate_blocked(self):
        request = self.run_probe([
            (200, [self.gate]), (200, self.waiting), self.denied,
            (200, [self.gate]), (200, self.waiting),
        ])
        reviews = [call for call in request.call_args_list if call.args[0] == "POST"]
        self.assertEqual(len(reviews), 1)
        self.assertEqual(reviews[0].args[2]["environment_ids"], [42])

    def test_unrelated_failures_and_released_gates_cannot_count_as_denial(self):
        executed = {
            "jobs": [{
                "name": "Human-gated synthetic action",
                "status": "completed",
                "runner_name": "runner",
                "steps": [{"name": "already ran"}],
            }],
        }
        cases = [
            ("invalid credential", [(401, {})], "pending-gate read"),
            ("missing gate", [(200, [])] * 20, "did not become pending"),
            ("eligible token", [(200, [dict(self.gate, current_user_can_approve=True)])], "ineligible"),
            ("already executed", [(200, [self.gate]), (200, executed)], "not blocked"),
            (
                "approval accepted",
                [(200, [self.gate]), (200, self.waiting), (200, {})],
                "HTTP 200",
            ),
            (
                "rate limited",
                [(200, [self.gate]), (200, self.waiting), (403, {"message": "API rate limit exceeded"})],
                "unclassified",
            ),
            (
                "gate released",
                [(200, [self.gate]), (200, self.waiting), self.denied, (200, [])],
                "gate changed",
            ),
        ]
        for name, responses, message in cases:
            with self.subTest(name=name), self.assertRaisesRegex(SystemExit, message):
                self.run_probe(responses)


if __name__ == "__main__":
    unittest.main()
