## Context

This is the public control repository of one installation, not a central
multi-customer control service. It implements the public framework's proposed
human-authorization and information-boundary contracts.

The initial framework and control specifications were human-merged. Only the
bounded synthetic proof subsequently received explicit implementation
authorization. After the human merged its workflow, the native approval and
rejection cases were exercised. Bot denial remains untested. The temporary
workflow was disabled before its environment was removed. No released runtime
version is implied.

## Goals / Non-Goals

**Goals**

- Native human review on GitHub Free for each requested execution action.
- Exact private request binding without publishing the private request.
- A bounded, low-impact proof before cloud/bootstrap implementation.

**Non-goals**

- Native branch protection inside a private GitHub Free solution repository.
- A custom replacement for GitHub's review decision.
- Hosting agent reasoning or generated code on a public Actions runner.
- Starting real workers during the first synthetic gate test.

## Decisions

### Separate public gates and private state

Use native protected environments named generically for build, development,
test, and production. Private issue integration freezes a manifest and
provides a private review summary containing the public run link. Public
workflow input is only a random request ID.

Every installation keeps its own private registry of allowed solutions,
identities, policies, and requests. That registry is maintained by trusted
integration code, not by an agent editing a public configuration file.

The approved job requests short-lived Azure access, sends its opaque request
reference, and receives only a sanitized outcome. It must not import private
source code or logs to compute that outcome.

### Protect the execution route, not a decorative environment

Bootstrap verifies public visibility, designated reviewers, trusted workflow
revisions/ref restrictions, and disallowed administrative bypass. The dispatcher
checks the expected policy before accepting a launch. A workflow pointing to
an unconfigured environment or a private caller is not an equivalent gate.

For the pilot, the same authorized human can hold each role. GitHub's option
to prevent the initiating user from approving must be configured consistently
with that explicitly allowed solo policy. It does not permit an agent identity
or a worker carrying human credentials to approve.

Organizations needing multiple independent approvals must map those decisions
to distinct enforceable checkpoints or be reported unsupported. Listing several
reviewers at one native gate does not require all of them to approve.

### Use a minimal clean public dispatcher

The proposed default control job runs on a standard GitHub-hosted runner;
all agent computation remains on private Azure workers. It has only the
permissions required to dispatch its action after approval. Reusable framework
assets are pinned to an approved immutable revision.

No pull-request-controlled code executes with private-worker access. Solution
repository tokens, App keys, model credentials, and deployment identities do
not become environment variables in the public dispatcher.

### Define the human-operated proof before implementing it

After explicit approval, implement only a manual synthetic workflow with no
checkout of solution content and no cloud credentials. Demonstrate:

1. A requested job is waiting and has not run its harmless synthetic action.
2. The designated human sees and explicitly approves one run.
3. A separately requested run is rejected and does not execute.
4. A representative bot/non-reviewer cannot satisfy the gate.
5. Public output contains only synthetic data and allowlisted status.

The assistant must not call an approval API with the user's token. If an
authorized test bot is unavailable, report the negative-actor case as untested,
not passed. No lasting Azure worker is required for this first gate-only test.

An approved second proof covers federation, policy drift, private manifests,
single use, altered inputs, and isolated Azure workers. Gate-only success is
not acceptance of the full platform.

## Risks / Trade-offs

- **Run timing and reviewer identity can be public** -> disclose this before
  activation; keep private details in the private review material.
- **Someone edits an environment instead of code** -> verify configuration and
  disable execution on drift.
- **A replayed approved run looks legitimate** -> private atomic single-use
  request consumption remains mandatory.
- **Self-hosting public runner workloads exposes Azure** -> do not register a
  general-purpose privileged worker on the public repository.
- **No native private branch protection** -> do not treat source pushes or
  merges as authorization to use private execution identities.

## Rollout

Review proposal, approve the synthetic test scope, configure the test gate,
run it together with the designated human, and remove temporary test-only
resources after capturing evidence. Production gate/bootstrap work follows
only after a separate approval. Any unsupported capability leaves the
installation inactive; there is no weaker automatic fallback.

## Synthetic proof implementation and evidence

On 2026-11-17 the human authorized the bounded gate-only proof in conversation,
after its exclusion of Azure/Fabric operations was stated. This approval does
not cover any private dispatcher, source access, Foundry, or worker bootstrap.
The implementation branch is not permission for the assistant to merge it.

The tested workflow was `.github/workflows/approval-smoke-test.yml` at commit
`63fae0675c10d91586350c0d7d1fbe1931443327`. Its
[immutable definition](https://github.com/Remc0000/Fabric-Delivery-OS-Control/blob/63fae0675c10d91586350c0d7d1fbe1931443327/.github/workflows/approval-smoke-test.yml)
remains available after cleanup. It had
only `workflow_dispatch`, no inputs, no checkout or external actions, empty
token permissions, and one fixed shell command that prints
`synthetic-action-completed`. Its single job required the temporary
`approval-smoke-test` environment and a `refs/heads/main` workflow context.
The runner was GitHub-hosted and its execution timeout was two minutes.

Configure the native environment with the designated installation human as
its sole required reviewer, `prevent_self_review=false` for the selected solo
profile, administrator bypass disabled, and only the branch `main` allowed.
The deployment policy must distinguish branch `main` from a tag of that name.
Re-read the reviewer and branch rules after creation. If the API does not
expose administrator bypass, require a human settings inspection and record
that verification method; an API write accepting an unknown field is not
proof that bypass is disabled. No dispatch precedes complete verification.

Before each dispatch, confirm that the environment policy is still verified
and that the current default-branch workflow revision is the human-merged
revision. Use no public input containing solution details. Record the actual
run links, workflow commit, reviewer decisions, step results, and sanitized
log inspection after execution. Pending evidence is not a successful test.

| Check | Current evidence |
| --- | --- |
| Human authorization of bounded scope | Explicit conversation approval on 2026-11-17 |
| Human merge of exact workflow revision | Human merged [control PR 3](https://github.com/Remc0000/Fabric-Delivery-OS-Control/pull/3); both runs used commit `63fae0675c10d91586350c0d7d1fbe1931443327`, whose workflow content matched the reviewed definition |
| Required reviewer, branch-only restriction, disabled bypass | Configured on 2026-11-17; fresh API reads verified the sole designated human reviewer, `prevent_self_review=false`, `can_admins_bypass=false`, and exactly one deployment rule of type `branch` named `main` |
| Job blocked with no executed steps | Observed `status=waiting`, no runner, and `steps=[]` for both runs before either review decision |
| Human-approved run executes fixed action | [Run 44166554472](https://github.com/Remc0000/Fabric-Delivery-OS-Control/actions/runs/44166554472): review history `approved` by the designated human; conclusion `success`; fixed completion step succeeded |
| Separately human-rejected run executes no action | [Run 44166850165](https://github.com/Remc0000/Fabric-Delivery-OS-Control/actions/runs/44166850165): review history `rejected` by the designated human; conclusion `failure`; no runner and `steps=[]` |
| Representative non-reviewer/bot cannot approve | Untested; no authorized test identity supplied |
| Public logs and artifacts contain only permitted synthetic output | Complete approved-run log inspected: GitHub runner/setup metadata and the literal synthetic command/status only; rejected run executed no steps; artifact counts were zero for both |
| Temporary environment removed and workflow disabled | After both runs completed, API verified workflow `disabled_manually` before deleting the temporary environment; fresh environment listing returned zero configured environments |

Review history was read from each run's `/approvals` endpoint after the human
reported their GitHub UI action. The assistant dispatched and inspected runs
but did not submit an approval or rejection. GitHub's default setup/teardown
steps are platform metadata, not additional solution processing. No source
records, private checkout, model call, or Azure/Fabric operation occurred.

The rejection is an expected failed workflow, not an implementation failure
or a cancellation. A successful approved run alone would not have established
this negative case. Conversely, neither outcome establishes refusal of an
unauthorized agent identity, manifest binding, replay prevention, federation,
or worker isolation.

The human merged the evidence/cleanup change and removed that disabled
workflow definition. No additional workflow activation or cloud bootstrap is
authorized by recording these results.

After capturing evidence, disable the workflow before deleting the temporary
environment so a later manual dispatch cannot recreate it without protection.
Do not delete the environment while any test run is waiting or active. A
human-reviewed cleanup PR can then remove the disabled workflow. Never report
the gate proof as complete while its required manual cases remain pending;
the missing bot case must remain explicitly unproven.

## Separately authorized Actions bot-denial follow-up

On 2026-11-17 the human explicitly requested the missing bot-denial test. The
new workflow `.github/workflows/bot-denial-proof.yml` requires human review
and merge before dispatch; it does not reactivate the removed first workflow.
There are no private inputs, external actions, checkout, or cloud credentials.

Use the ephemeral GitHub Actions installation token as a concrete non-reviewer
bot, not a human credential or an assumed external App secret. Its independent
probe job has only `actions: read` and `deployments: write`; all workflow-level
permissions and the gated job's token permissions are empty. The only possible
gated action remains the literal synthetic completion message.

The temporary environment `approval-bot-test` requires the designated human
under the agreed solo profile, disables administrator bypass, and permits
only branch `main`. Verify those settings and the exact human-merged workflow
before dispatch. The probe waits a bounded time for that environment to become
pending, verifies its token's `current_user_can_approve=false`, and confirms
the gated job is waiting with no runner and no steps.

It attempts exactly one approval using only `github.token`. The expected
response is HTTP 403, `Resource not accessible by integration`. This
classification follows the official GitHub REST/OpenAPI contract: the review
endpoint is not enabled for GitHub Apps. Successful pending-deployment and
job reads distinguish the test from an absent/invalid credential, and fresh
post-attempt reads must show the same gate is still blocked. Other responses
or errors fail explicitly. No response body or token is printed publicly.

This establishes refusal for an Actions installation token through that
integration-access boundary. It does not isolate a reviewer-membership check
for an otherwise supported user credential, nor validate a future runtime
App's exact installation and permissions. Do not overstate the result.

The human must not approve the waiting test. After independently inspecting
the probe's outcome, gate state, and empty review history, cancel the run
without submitting a review. Verify terminal jobs, disable the workflow,
then delete the temporary environment. A human-reviewed cleanup PR removes
the disabled workflow and records actual evidence. All results remain pending
until observed.
