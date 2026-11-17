## Context

This is the public control repository of one installation, not a central
multi-customer control service. It implements the public framework's proposed
human-authorization and information-boundary contracts.

There are no executable workflows or configured gates yet. The framework and
this proposal must be reviewed together; no released runtime version is
implied by their existence.

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
