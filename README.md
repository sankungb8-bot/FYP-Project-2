# Industry 4.0 Readiness and Digital Gap Assessment System

## 1. Project Overview

This project develops a rule-based prototype for assessing Industry 4.0 readiness and identifying digitalisation gaps for HICOM Automotive Manufacturers (Malaysia) Sdn. Bhd.

The system is designed to support a structured workflow:

**Measure → Diagnose → Prioritise**

The prototype applies the structure of the **Industry4WRD Readiness Assessment (Industry4WRD-RA)** as the main readiness framework and uses **Smart Industry Readiness Index (SIRI)** prioritisation logic as a supporting reference for ranking improvement priorities.

The system is an academic prototype and does **not** claim to provide official Industry4WRD certification.

---

## 2. Project Scope

The system focuses on:

- Industry 4.0 readiness measurement
- Assessment-cycle management
- Assessment question and response management
- Readiness score calculation
- Digital gap identification
- Gap prioritisation
- Phased digitalisation roadmap generation
- Management dashboards and visualisations
- Downloadable assessment/report outputs
- User roles and access control
- Activity/audit records
- Evidence-supported assessment records

### Framework boundaries

- **Industry4WRD-RA** is the primary readiness assessment framework.
- Industry4WRD-RA uses the Shift Factors **People (20%), Process (30%), and Technology (50%)**.
- The framework contains **8 Thrusts and 21 Dimensions**.
- Dimensions are evaluated using a **0–4 scoring scale**.
- Readiness profiles include **Conventional, Newcomer, Learner, Experienced, and Leader**.
- **SIRI is used as a prioritisation reference**, not as a second official readiness assessment framework.
- **ESG is treated as a supplementary analytical layer**, not as an additional official Industry4WRD dimension.
- The core recommendation logic is **rule-based**. AI-based recommendations are outside the core implementation scope.

---

## 3. Technology Stack

| Layer | Technology |
|---|---|
| Frontend | React |
| Backend | FastAPI |
| Database | PostgreSQL |
| Containerisation | Docker / Docker Compose |
| Development Environment | WSL2 |
| Programming | JavaScript/React, Python, SQL |
| Version Control | Git / GitHub |
| Project Management | Jira |
| Testing | Unit, functional, integration, and validation testing |

---

## 4. System Architecture

The system follows a three-tier architecture:

```text
┌──────────────────────────────┐
│     Presentation Tier        │
│          React UI            │
└──────────────┬───────────────┘
               │ HTTP / REST API
               ▼
┌──────────────────────────────┐
│     Application Tier         │
│          FastAPI             │
│ Authentication / Business    │
│ Logic / Assessment / Reports │
└──────────────┬───────────────┘
               │ SQL / ORM
               ▼
┌──────────────────────────────┐
│        Data Tier             │
│         PostgreSQL           │
│ Users / Assessments /        │
│ Results / Gaps / Roadmaps    │
└──────────────────────────────┘
```

---

## 5. User Roles

The prototype defines three main user roles:

### Administrator
Responsible for:

- User account management
- Role management
- Assessment-cycle/content management
- System monitoring
- Activity records

### Assessor
Responsible for:

- Accessing assigned assessment cycles
- Completing assessment questions
- Saving assessment progress
- Providing evidence where required
- Submitting completed assessments

### Management User
Responsible for:

- Reviewing readiness results
- Reviewing identified gaps
- Reviewing prioritisation results
- Reviewing digitalisation roadmaps
- Viewing dashboards and reports

---

## 6. Core Functional Requirements

The implementation is based on the approved Chapter 3 requirements baseline.

| ID | Requirement |
|---|---|
| FR-01 | Login / secure access |
| FR-02 | User account management |
| FR-03 | Assessment cycles/content management |
| FR-04 | Assessment assignment/monitoring |
| FR-05 | Complete assessment |
| FR-06 | Save assessment progress |
| FR-07 | Validate assessment submission |
| FR-08 | Calculate readiness |
| FR-09 | Identify digital gaps |
| FR-10 | Rank/prioritise gaps |
| FR-11 | Generate phased roadmap |
| FR-12 | Dashboards/visualisations |
| FR-13 | Management review |
| FR-14 | Downloadable reports |
| FR-15 | Activity records |

---

## 7. Non-Functional Requirements

The system must consider:

- Usability and clear navigation
- Authentication and role-based access control
- Secure password hashing
- Input validation and data protection
- Acceptable response performance
- Data integrity
- Error handling and recovery
- Maintainable and modular code
- Scalability
- Browser/device compatibility
- Backup and restoration
- Audit/activity records

---

## 8. Repository Structure

```text
FYP Project 2/
│
├── frontend/              # React presentation tier
├── backend/               # FastAPI application tier
├── database/              # Database scripts, migrations and seed data
├── tests/                 # Unit, functional and integration tests
├── docs/                  # Technical and project documentation
├── evidence/              # Implementation and testing evidence
│
├── docker-compose.yml     # Container orchestration
├── .gitignore             # Files excluded from version control
└── README.md              # Project documentation
```

---

## 9. Development Environment

The project is developed using:

- Windows
- WSL2
- VS Code
- Git
- Docker / Docker Compose
- Node.js and npm
- Python
- PostgreSQL

### Recommended setup verification

```bash
git --version
node --version
npm --version
python --version
docker --version
docker compose version
```

---

## 10. Git Branch Strategy

The repository follows a controlled branch strategy.

### Main branches

```text
main
develop
```

- `main` — stable and review-ready versions.
- `develop` — integration branch for completed feature work.

### Feature branches

Feature work should use:

```text
feature/<scope>
```

Approved implementation scopes include:

```text
feature/authentication
feature/assessment
feature/readiness-scoring
feature/gap-analysis
feature/prioritisation
feature/roadmap
feature/dashboard-reporting
feature/testing
```

A feature branch should normally be created from `develop`.

---

## 11. Git Workflow

For each implementation task:

```text
Jira Task
   ↓
Create / select feature branch
   ↓
Implement approved scope
   ↓
Run tests
   ↓
Commit changes
   ↓
Push branch
   ↓
Review
   ↓
Merge into develop
   ↓
Stable review
   ↓
Merge into main
```

Do not commit unrelated changes to a feature branch.

---

## 12. Commit Convention

Use the following commit prefixes:

| Prefix | Purpose |
|---|---|
| `feat:` | New functionality |
| `fix:` | Defect correction |
| `test:` | Tests |
| `docs:` | Documentation/evidence |
| `refactor:` | Internal restructuring |
| `chore:` | Configuration/tooling |

Examples:

```text
feat: implement role based authentication (FYP2-XX)
feat: add assessment response persistence (FYP2-XX)
test: add readiness score calculation tests (FYP2-XX)
docs: update requirements traceability matrix (FYP2-XX)
fix: validate incomplete assessment submission (FYP2-XX)
chore: configure development environment (FYP2-XX)
```

Meaningful implementation commits should reference the related Jira issue.

---

## 13. Jira Workflow

Every significant development activity must be traceable to Jira.

The project uses:

**Jira project:** FYP Project 2  
**Project key:** FYP2  
**Board:** I4R board

The implementation follows:

```text
Requirement
    ↓
Jira Issue
    ↓
Git Branch
    ↓
Commit
    ↓
Implementation
    ↓
Test
    ↓
Evidence
    ↓
Chapter 4
```

The Jira issue should not be marked **Done** until its implementation and required evidence have been verified.

---

## 14. Testing Strategy

Testing is part of the implementation workflow rather than a final-stage activity.

### Unit testing

Used for isolated functions such as:

- Readiness score calculations
- Validation rules
- Prioritisation calculations
- Business rules

### Functional testing

Functional requirements FR-01 to FR-15 are tested against their expected behaviour.

### Integration testing

Integration testing verifies communication across:

```text
React → FastAPI → PostgreSQL
```

### Validation

Validation checks whether the implemented prototype satisfies the approved requirements and project objectives.

---

## 15. Evidence Management

Implementation evidence is stored under:

```text
evidence/
├── 01-environment/
├── 02-database/
├── 03-authentication/
├── 04-assessment/
├── 05-readiness/
├── 06-gap-analysis/
├── 07-prioritisation/
├── 08-roadmap/
├── 09-dashboard/
├── 10-reporting/
└── 11-testing/
```

Evidence may include:

- Configuration screenshots
- Database screenshots
- Application screenshots
- Test results
- API responses
- Git history
- Jira records
- Validation results
- Final system outputs

Evidence should be clearly named and linked to the relevant Jira requirement.

---

## 16. Chapter 4 Traceability

Implementation documentation should preserve the following traceability chain:

```text
Chapter 1–3 Requirement
        ↓
Jira Issue
        ↓
Git Branch
        ↓
Git Commit
        ↓
Implemented Feature
        ↓
Test Case
        ↓
Test Result
        ↓
Evidence Artifact
        ↓
Chapter 4
```

This ensures that the final implementation can be demonstrated and justified against the approved project requirements.

---

## 17. Database Scope

The database is expected to support the following major data areas:

- Users and roles
- Assessment cycles
- Framework dimensions
- Indicators
- Questions
- Response scales
- Assessor responses
- Evidence
- Target levels
- Readiness results
- Digital gaps
- Prioritisation inputs
- Recommended initiatives
- Activity records

Database design should follow normalisation principles and maintain data integrity.

---

## 18. Security Conventions

The system must not store plaintext passwords.

Security-related implementation should include:

- Password hashing
- Authentication
- Role-based access control
- Input validation
- Protected API endpoints
- Appropriate error handling
- Environment-based secret configuration
- No committed credentials or secrets

Sensitive configuration should be stored through environment variables and excluded from Git where appropriate.

---

## 19. Environment Variables

Environment-specific configuration should not be hard-coded into source files.

Example:

```text
DATABASE_URL=<database-connection-string>
```

Use a local environment file for development where appropriate and ensure secret files are excluded through `.gitignore`.

Never commit passwords, API keys, tokens, or other secrets to the repository.

---

## 20. Definition of Done

A development task is considered complete only when:

1. The Jira requirement is clearly identified.
2. The approved scope is implemented.
3. The implementation is committed to Git.
4. Relevant tests have been executed.
5. Applicable non-functional requirements have been considered.
6. Evidence has been captured.
7. Jira has been updated.
8. Documentation has been updated where necessary.
9. The implementation can be traced to Chapter 4.

---

## 21. Development Principles

The project follows these principles:

- Implement the approved requirements before adding optional features.
- Keep the core system rule-based.
- Maintain clear separation between frontend, backend, and database layers.
- Keep framework terminology consistent with the approved project report.
- Do not claim official Industry4WRD certification.
- Treat SIRI as prioritisation support rather than a second readiness framework.
- Treat ESG as a supplementary analytical layer.
- Test features as they are implemented.
- Preserve evidence throughout development.
- Keep Jira, Git, tests, evidence, and Chapter 4 aligned.

---

## 22. Current Development Status

The project foundation has been established.

Completed foundation work includes:

- Jira project and board
- Sprint 0 — Project Foundation
- Requirements baseline and traceability planning
- Git repository
- `main` branch
- `develop` branch
- Feature branch workflow
- Initial repository structure
- README and development conventions

Further implementation should proceed incrementally through the approved Jira backlog.

---

## 23. Academic Scope Statement

This repository supports an academic Final Year Project implementation. The system is a prototype developed to demonstrate the application of the approved assessment framework, digital gap analysis, prioritisation logic, and roadmap generation.

The prototype should be evaluated according to the approved project requirements, methodology, architecture, testing strategy, and validation approach documented in the final project report.
