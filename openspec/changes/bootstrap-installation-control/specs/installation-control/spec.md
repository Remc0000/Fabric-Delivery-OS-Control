## Purpose

Use native GitHub human approval gates for private work without placing private
solution processing or privileged general-purpose workers in public workflows.

## ADDED Requirements

### Requirement: Control is owned and protected per installation
The installation SHALL own this public repository and restrict changes to
trusted control code and settings through human review. Agents MUST NOT have
control write/admin credentials. Reviewer rules, trusted refs, public
visibility, and disabled bypass SHALL be verified before activation.

#### Scenario: An agent proposes a control workflow edit
- **WHEN** a private solution task attempts to write control code or settings
- **THEN** its tools deny the operation and report the boundary violation privately

### Requirement: Each execution action has its own human gate
The control plane SHALL provide separate native approval checkpoints for
building and deployment to development, test, and production. Each checkpoint
MUST list only authorized human reviewers for its action.

#### Scenario: A test deployment is approved
- **WHEN** its control job finishes
- **THEN** production remains unapproved until a new production request passes its own gate

#### Scenario: A bot attempts approval
- **WHEN** a non-reviewer agent identity attempts to release the waiting job
- **THEN** it cannot satisfy the native human reviewer requirement

### Requirement: Approval refers to a frozen private request
Every control run SHALL refer to exactly one opaque request ID bound to an
immutable private review manifest. The human SHALL be able to review the
corresponding private action, input/artifact revision, and target before
approving. Mutable issue text and branch names MUST NOT replace this binding.

#### Scenario: A private proposal changes after the request was registered
- **WHEN** the current proposal no longer matches the frozen request
- **THEN** the changed operation requires a new request rather than inheriting the old approval

### Requirement: Public jobs never process private solution content
Control inputs, workflow logs, summaries, job names, errors, caches, and
artifacts SHALL use an explicit non-sensitive allowlist. Detailed manifests,
solution identifiers, code, prompts, source metadata, and worker output MUST
remain in approved private storage or the private repository.

#### Scenario: Dispatch fails with a detailed private error
- **WHEN** the public job reports the failure
- **THEN** it emits only the generic status and opaque correlation reference

### Requirement: Federation authorizes only the intended action
Approved jobs SHALL authenticate with short-lived workload federation bound to
the expected repository identity, trusted workflow context, and environment.
The dispatcher MUST verify request state and atomically consume a grant before
starting a worker. It MUST reject another repository, environment, request,
workflow attempt, or changed artifact.

#### Scenario: An old workflow run is rerun
- **WHEN** its previous request was already consumed
- **THEN** the dispatcher refuses another execution even if GitHub starts the job again

### Requirement: Private work cannot enter through a public runner path
The public control job SHALL execute only fixed orchestration and MUST NOT
check out private code or run agent/solution scripts. Agent tasks and
deployment tasks SHALL run in separate approved private Azure worker profiles.

#### Scenario: A public pull request changes an orchestration file
- **WHEN** the pull request is unreviewed
- **THEN** it cannot schedule a private worker or obtain execution credentials

### Requirement: Protection failures disable execution
An unsupported reviewer feature, missing human role, changed policy,
unverified bypass configuration, or missing private dispatcher SHALL leave
affected execution inactive. A partially created unprotected environment
MUST NOT be reported as a successful approval setup.

#### Scenario: GitHub accepts an environment but rejects its reviewer rule
- **WHEN** onboarding reads the resulting configuration
- **THEN** it reports failure and removes or clearly quarantines only its newly created unprotected test resource

### Requirement: The first proof is synthetic and human operated
Before adding the smoke workflow, a human SHALL approve its exact scope.
The proof SHALL use synthetic identifiers only, show a job blocked before
approval, exercise manual approval/rejection and an unauthorized actor, and
record actual results. It MUST NOT call Foundry, read source data, provision
Azure, or operate Fabric.

#### Scenario: The proof reaches its authorized boundary
- **WHEN** the synthetic approval behavior is observed
- **THEN** the test stops and reports only that gate-level result
- **AND** it does not claim that worker isolation or production deployment is proven

#### Scenario: An unreviewed branch or automatic event attempts the proof
- **WHEN** the synthetic workflow is evaluated outside a manual dispatch from branch `main`
- **THEN** its synthetic action cannot execute
- **AND** the temporary environment permits branch `main`, not a tag or another branch

#### Scenario: The designated human rejects the separate negative run
- **WHEN** the human rejects the waiting synthetic job through GitHub
- **THEN** the fixed completion step does not execute
- **AND** the proof records the actual rejection rather than a cancellation as evidence

#### Scenario: Administrator bypass cannot be read through the API
- **WHEN** the API cannot expose the configured bypass setting
- **THEN** dispatch remains blocked until a human verifies disabled bypass in environment settings
- **AND** the evidence distinguishes human settings verification from API verification

#### Scenario: The synthetic proof is cleaned up
- **WHEN** all test runs are terminal and their evidence has been recorded
- **THEN** the workflow is disabled before its temporary environment is deleted
- **AND** cleanup cannot leave an enabled workflow pointing to a missing unprotected environment
