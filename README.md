# Fabric Delivery OS Control

Public control-plane repository for one Fabric Delivery OS installation.

## Status

The initial specifications are merged. A separately human-authorized,
manual-only synthetic approval proof is proposed in
`.github/workflows/approval-smoke-test.yml`. It performs only a fixed synthetic
log message after native human approval. It has no checkout, action
dependencies, token permissions, cloud access, or private inputs.

The human must review and merge this workflow before it can be dispatched.
Native gate behavior is not proven until the human-operated tests complete.
No runtime, private dispatcher, federation, or Azure/Fabric operations are
implemented or authorized.

## Synthetic proof procedure

The temporary `approval-smoke-test` environment must require the designated
human reviewer, permit only the `main` branch, and disallow administrator
bypass. The explicitly selected solo-human profile permits the initiating
human to approve; this does not authorize an assistant to use their approval
credentials. Verify the bypass setting in GitHub's environment settings if
the API does not expose it. Do not dispatch while any protection is unverified.

After human merge and protection verification, dispatch from `main`. Verify
that the job is waiting and has executed no steps. The human then uses
GitHub's **Review deployments** control to approve that run. Dispatch a second
run and have the human reject it; its synthetic step must not execute.
Record run links, revisions, reviewer decisions, actual results, and any
untested bot case in the OpenSpec design. An assistant must never approve or
reject either run using the human's token.

After inspecting the public output, disable the test workflow and remove only
its temporary environment. Keep the workflow disabled until a human-reviewed
cleanup PR removes or intentionally replaces it. This proof grants no
authority to activate real delivery.

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
