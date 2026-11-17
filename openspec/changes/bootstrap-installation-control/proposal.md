## Why

Private GitHub Free solutions need enforceable human authorization without
publishing their implementation or creating a custom human-approval service.
A separate public control repository provides native GitHub gates while the
installation keeps its request state and agent execution private.

## What Changes

- Specify public native approval gates for builds and each deployment stage.
- Specify opaque request handling, immutable private request binding, and
  federation to narrowly authorized Azure dispatch.
- Specify a synthetic, human-operated smoke test before any real agent or
  Fabric execution is enabled.

This proposal depends on the framework's `human-authorization`,
`agent-execution`, and `information-boundaries` contracts. It does not configure
environments or add a runnable workflow by itself.

## Capabilities

### New Capabilities

- `installation-control`: Native human gates, trusted dispatch, private-state binding, and a bounded proof.

### Modified Capabilities

None.

## Impact

Future work affects this repository's rules, environments, Actions workflow,
and approved federation. Private repository mappings and identities remain
outside public files. Implementation and any Azure bootstrap require separate
human authorization after review.
