# Development and Review Workflow

## Definition of Done

A task is considered complete only when:

1. The requirement is identified and linked to the relevant Jira issue.
2. The implementation is completed.
3. Code is committed to Git using the project commit convention.
4. Relevant tests are created or updated.
5. Tests pass successfully.
6. Relevant non-functional requirements are considered.
7. Evidence is captured in the appropriate `evidence/` directory.
8. Jira is updated with the implementation and verification status.
9. The implementation can be traced to the relevant Chapter 4 section.

## Traceability

Requirement → Jira Issue → Git Branch → Commit → Implementation → Test → Evidence → Chapter 4

## Review Workflow

1. Create or update the Jira task.
2. Implement the feature on the appropriate branch.
3. Run relevant tests.
4. Review the implementation and test results.
5. Capture evidence.
6. Commit the changes.
7. Update Jira with verification details.
8. Mark the task Done only after the Definition of Done is satisfied.

## Commit Convention

- `feat:` New functionality
- `fix:` Bug correction
- `test:` Testing changes
- `docs:` Documentation
- `refactor:` Code restructuring
- `chore:` Configuration or maintenance