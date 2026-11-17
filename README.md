# Fabric Delivery OS Control

Public control-plane repository for one Fabric Delivery OS installation.

## Status

The initial specifications are merged. A separately human-authorized
synthetic proof demonstrated native human approval and rejection on GitHub
Free in this public repository. Both runs waited without a runner or executed
steps before the human made a decision.

The temporary workflow was disabled before its environment was removed.
The human merged its evidence/cleanup change and removed its definition.
No runtime, private dispatcher, federation, or Azure/Fabric operations are
implemented in this control repository. The unauthorized-bot case remains
untested pending the separately authorized follow-up below.

## Bot-denial follow-up

The proposed `.github/workflows/bot-denial-proof.yml` uses only manual dispatch
from branch `main`, with no checkout, external actions, private input, or cloud
access. It requires human review and merge before execution. A fresh temporary
environment `approval-bot-test` must require the sole designated human, allow
only branch `main`, and disable administrator bypass.

One job waits at that gate. An independent synthetic probe uses only its
ephemeral GitHub Actions token with `actions: read` and `deployments: write`,
not the human dispatcher's credentials. It verifies authenticated reads work
and that the bot is ineligible, attempts approval once, and requires HTTP 403
with the classified integration-access denial. It must then confirm the same
gate is still waiting with no runner and no executed steps.

This tests the Actions installation token, not an independently installed
future runtime App. An API unsupported for integrations is an integration
authentication boundary, not evidence that every reviewer policy or future
identity has been tested. Unexpected responses, missing gates, read failures,
or a released job fail the proof rather than count as refusal.

Do not manually approve this run. After evidence collection, cancel the waiting
run, verify termination, disable the workflow, and only then delete its
temporary environment. Remove the disabled definition through human review.

Run the probe's local false-positive checks without network access using
`python -m unittest discover -s tests -v`. Mocked checks are not live proof.

## Synthetic proof results

The [approved run](https://github.com/Remc0000/Fabric-Delivery-OS-Control/actions/runs/44166554472)
executed only the fixed synthetic completion command after the designated
human approved through GitHub. The separate
[rejected run](https://github.com/Remc0000/Fabric-Delivery-OS-Control/actions/runs/44166850165)
failed with no runner assigned and no steps executed after the human rejected
it through GitHub. This failure is the expected negative-case result.

Reviewer requirements, branch-only `main` restrictions, and disabled
administrator bypass were verified by fresh API reads before dispatch.
The chosen solo-human profile allowed the initiating human to approve.
The assistant did not submit either review decision.

Public logs contained GitHub setup metadata and the fixed synthetic
command/status; neither run produced artifacts. The exact workflow revision,
review histories, cleanup, and remaining proof gaps are recorded in the
OpenSpec design. This gate-only result does not authorize real delivery.

## Boundary

This repository is public so GitHub Free can provide native required-reviewer
jobs. It contains trusted generic orchestration, not private solution code.
Every build and every deployment to development, test, or production needs its
own appropriate human approval.

Runtime agent identities cannot write to this repository or administer its
protections. Human-authorized installation bootstrap is separate from those
unprivileged runtime identities. The
framework repository supplies reviewed, versioned control assets; an adopter
explicitly upgrades its own installation.

Only opaque request references and non-sensitive operational status belong in
public runs. Detailed review material, source mappings, manifests, prompts,
code, data, and worker logs stay private. Run existence and timing remain public.

Installation requirements live under `openspec/changes`. Completing or merging
them does not authorize implementation or bootstrap beyond a separately
approved action.
