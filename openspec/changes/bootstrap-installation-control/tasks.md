## 1. Review and exact test authorization

The human approved the merged specification's bounded synthetic proof scope
on 2026-11-17, then reviewed and merged the exact workflow through control PR 3.
Unchecked items below are not implicit successes. See the design's evidence
table for observed manual results, cleanup, and untested boundaries.

- [x] 1.1 Review the framework/control contract and obtain explicit approval of the synthetic test revision; verify the approved scope excludes Azure, Foundry, private source reads, and Fabric.
- [x] 1.2 Confirm permitted human roles, solo versus separation policy, and public metadata disclosure; verify incompatible policy blocks the test.

## 2. Synthetic native-gate proof

- [x] 2.1 Configure only the approved synthetic human-review environment and trusted workflow path; re-read reviewer and bypass settings to verify actual protection.
- [x] 2.2 Add the approved manual smoke workflow with a harmless synthetic action; verify it contains no cloud access, private checkout, or secret-bearing output.
- [x] 2.3 Start an authorized synthetic request and stop before approval; verify its action has not executed.
- [x] 2.4 Let the designated human approve through GitHub; verify the resulting action and reviewer evidence without the assistant submitting approval.
- [x] 2.5 Start and manually reject a separate request; verify no action executes.
- [x] 2.6 Exercise a representative unauthorized agent identity if authorized credentials exist; verify refusal, otherwise explicitly record the missing proof.
- [x] 2.7 Inspect public logs and artifacts and clean up temporary test resources; verify only synthetic references and no unintended public content remain.
- [x] 2.8 Disable the workflow before deleting the temporary environment after all runs are terminal.
- [x] 2.9 Obtain human review and merge of the evidence/cleanup PR to remove the disabled workflow definition.

## 2a. Separately authorized bot-denial follow-up

- [x] 2a.1 Review and human-merge the exact manual Actions bot-denial workflow; verify no human approval credential or cloud/private input is used.
- [x] 2a.2 Configure and re-read the temporary human-only environment, disabled administrator bypass, and branch-only main restriction.
- [x] 2a.3 Observe authenticated bot reads, explicit reviewer ineligibility, the classified refusal, and the same job still waiting with no executed steps.
- [x] 2a.4 Independently verify review history and public output; record the exact token-class boundary and any unproven identity cases.
- [x] 2a.5 Cancel the waiting run without review, verify all jobs terminal, disable the workflow, then delete its environment.
- [ ] 2a.6 Obtain human review and merge of bot-proof evidence and disabled-workflow removal.

## 3. Separately approved private dispatch

- [ ] 3.1 Obtain approval of exact Azure/bootstrap identities and grants; verify no cloud provisioning precedes that decision.
- [ ] 3.2 Implement private manifest registration and public opaque-ID dispatch; verify public fields cannot contain solution mappings, prompts, data, or diagnostics.
- [ ] 3.3 Configure environment-specific federation to the private dispatcher; verify wrong repository, ref, action, and environment tokens cannot launch a worker.
- [ ] 3.4 Verify request/digest binding, revocation, policy drift, concurrent claims, reruns, and retry behavior; each negative case must refuse execution.
- [ ] 3.5 Validate private worker isolation and per-environment deployment identities with synthetic inputs; verify no public job or build sandbox can obtain deployment authority.
- [ ] 3.6 Obtain human acceptance of the complete proof before activating real solution delivery; verify any unproven boundary remains visibly blocked.
