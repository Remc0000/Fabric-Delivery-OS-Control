# Fabric Delivery OS Control

Public control-plane repository for one Fabric Delivery OS installation.

## Status

Specification proposal only. No executable workflows, credentials, approval
environments, or Azure resources are configured by these documents.

## Boundary

This repository is public so GitHub Free can provide native required-reviewer
jobs. It contains trusted generic orchestration, not private solution code.
Every build and every deployment to development, test, or production needs its
own appropriate human approval.

Agents cannot write to this repository or administer its protections. The
framework repository supplies reviewed, versioned control assets; an adopter
explicitly upgrades its own installation.

Only opaque request references and non-sensitive operational status belong in
public runs. Detailed review material, source mappings, manifests, prompts,
code, data, and worker logs stay private. Run existence and timing remain public.

Draft installation requirements live under `openspec/changes`. Completing them
does not authorize workflow implementation or bootstrap.
