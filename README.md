# Fabric Delivery OS Control

Public control-plane repository for one Fabric Delivery OS installation.

## Status

The initial specifications are merged. A separately human-authorized
synthetic proof demonstrated native human approval and rejection on GitHub
Free in this public repository. Both runs waited without a runner or executed
steps before the human made a decision.

The temporary workflow was disabled before its environment was removed.
The evidence/cleanup change removes its executable definition; until that
change is human-merged, the definition on `main` must remain disabled.
No runtime, private dispatcher, federation, or Azure/Fabric operations are
implemented or authorized. The unauthorized-bot case remains untested.

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
