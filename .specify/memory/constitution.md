# Speckit Constitution

<!-- Example: Spec Constitution, TaskFlow Constitution, etc. -->

## Core Principles

### I. Library-First

Speckit features start life as a standalone, importable library with a clear public API.

* **Separation of concerns**: domain logic lives in libraries, not in apps or scripts.
* **Stable contracts**: public functions/classes are intentional, typed, and documented.
* **No “organizational-only” packages**: every module must justify existence through reusable capability.
* **Layering rule**: `core` (pure) → `adapters` (IO) → `apps` (wiring). Keep dependencies flowing in one direction.

### II. Explicit Interfaces and Schemas

Every boundary must have an explicit contract: types, schemas, and error models.

* Use **Pydantic models** (or equivalent) for request/response and internal boundaries.
* Define **domain types** (enums, dataclasses, value objects) instead of loose dicts.
* Prefer **small, composable** functions with clear input/output.
* Maintain **backwards compatibility** where possible; when not, provide migration steps.

### III. Test-First (Non-Negotiable)

Testing is part of design. New functionality is accepted only when verified by tests that reflect user intent.

* **Default to TDD** for core logic (Red → Green → Refactor).
* **Pyramid**: unit tests (fast) > integration tests (realistic) > end-to-end tests (minimal but critical).
* **Behavior focus**: test observable outcomes, not implementation details.
* **Determinism**: no flaky tests; random seeds fixed; time and IO are injected/mocked.

### IV. Integration Testing as Contract Protection

Where systems meet, we test contracts end-to-end.

* Required for: API routes, persistence adapters, file/format IO, external service clients.
* Use ephemeral resources: sqlite/duckdb, temporary folders, test containers (when needed).
* Include **schema compatibility tests** for serialized formats (JSON/Parquet/Arrow).
* Add **regression tests** for bugs before fixing them.

### V. Error Handling with Human and Machine Clarity

Errors are part of the API. They must be consistent, actionable, and observable.

* Define an **error taxonomy**: validation errors, domain errors, infra errors.
* Raise **typed exceptions** in core; translate at boundaries (API/CLI) into structured responses.
* Include **actionable messages**: what failed, why, and how to fix.
* Never swallow errors; log with context; avoid noisy stack traces in expected failures.

### VI. Consistent UX Across CLI, API, and UI

User experience is a product surface, not a side effect.

* **Single source of truth** for domain logic used by CLI, API, and UI.
* CLI: consistent commands, help text, exit codes, and structured output options (JSON + human).
* API: consistent response shapes, pagination patterns, and error responses.
* UI: consistent terminology, labels, units, date formats, and empty/loading/error states.

### VII. Performance by Design, Measured by Defaults

Performance requirements are stated, measured, and protected.

* Prefer **vectorized operations** (Pandas/Polars) and avoid Python loops for data transforms.
* Avoid unnecessary copies; be explicit about memory usage.
* Add **profiling hooks** and baseline benchmarks for hot paths.
* Define service-level constraints: p95 latency targets, throughput, and memory ceilings.
* Use caching deliberately: clear invalidation rules and bounded size.

### VIII. Observability and Operability

If it runs, it must be diagnosable.

* Structured logging with stable keys (request_id, user_id if applicable, trace_id, dataset_id, job_id).
* Metrics for key workflows: counts, durations, error rates, queue time.
* Tracing for distributed boundaries where relevant.
* Health checks and readiness probes for services.

### IX. Documentation as an API Surface

Documentation is treated as a deliverable, maintained alongside code.

* Every public function/class: docstring with purpose, inputs, outputs, errors, examples.
* Every module/package: README with quickstart, contracts, and common pitfalls.
* Keep examples executable and tested (doctest or example tests) where practical.
* Prefer short “how-to” docs over long narratives; add diagrams for complex flows.

### X. Dependency Discipline

Dependencies are a liability. Choose intentionally and keep the graph small.

* Prefer mature, widely adopted libraries with strong maintenance signals.
* Pin versions; document upgrade policy; use lockfiles.
* Avoid optional dependency sprawl; use extras for truly optional features.
* Don’t leak heavy dependencies into core modules.

### XI. Security and Privacy by Default

Sensitive data handling is part of the definition of done.

* Minimum data access: only what is needed, only for as long as needed.
* Redact secrets and sensitive fields in logs.
* Validate all external inputs; sanitize file paths and query params.
* For data exports: include provenance, access controls, and retention rules.

### XII. Versioning, Compatibility, and Migration

Breaking changes must be explicit, rare, and supported with migration.

* Use semantic versioning: MAJOR.MINOR.PATCH.
* Maintain changelogs with “Added/Changed/Fixed/Deprecated/Removed”.
* Deprecate before removal when possible; provide migration scripts or guides.

## Engineering Standards

### Code Quality Standards

* **Formatting and linting** enforced via CI (black/ruff, or equivalent).
* **Type hints** required for public APIs and non-trivial internal logic.
* **Pure core**: keep domain logic side-effect free; IO at edges.
* **Naming**: explicit, domain-relevant, and consistent; avoid ambiguous abbreviations.
* **Small modules**: prefer composable units over monoliths; refactor early.

### Data Engineering Standards (Pandas-inspired)

* Treat dataframes as immutable: return new objects rather than mutating in place.
* Validate schema early: required columns, dtypes, nullability, allowed values.
* Prefer explicit column selection, stable ordering, and consistent naming conventions.
* Keep transforms as a pipeline of small steps; each step testable.
* Avoid hidden global state; pass configuration explicitly.

### API Standards (FastAPI-inspired)

* Explicit request/response models; no anonymous dict payloads.
* Use dependency injection for cross-cutting concerns (auth, db, settings).
* Validate at the edge; keep endpoints thin: parse → call service → map response.
* Consistent status codes and error envelopes.
* Document routes via OpenAPI; examples included for important endpoints.

### Testing Standards

* Unit tests: fast, isolated, no external services.
* Integration tests: real adapters with ephemeral resources.
* Contract tests: schemas and response formats must not drift.
* Performance tests: benchmark hot paths and protect against regressions.
* Coverage target is a guardrail, not a goal; focus on risk-weighted coverage.

### Performance Standards

* Default inputs should run efficiently on typical hardware.
* Large data operations must state expected complexity and memory profile.
* Prefer streaming / chunking for large files.
* Concurrency is explicit: async only when justified and correctly bounded.

## Development Workflow

### Branching and PR Rules

* Small PRs, focused scope, clear description and motivation.
* Every PR must include: tests, documentation updates, and changelog entry if user-facing.
* Reviews focus on: correctness, contracts, readability, performance, and UX consistency.

### Quality Gates (CI)

* Lint + format check
* Type checks (where applicable)
* Unit + integration tests
* Minimal benchmark suite for hot paths
* Security checks (dependency scanning, secrets scanning)

### Release Process

* Release notes generated from changelog.
* Version bump aligned with semantic versioning.
* Backwards compatibility checked; migrations documented.

## Governance

* This constitution supersedes local conventions. Exceptions require explicit documentation.
* Every repository must include a short `CONTRIBUTING.md` that maps repo-specific rules to this constitution.
* Amendments require: rationale, migration plan, and a version bump.
* PR reviewers are responsible for enforcement; unresolved violations block merge.

**Version**: 1.0.0 | **Ratified**: 2025-12-13 | **Last Amended**: 2025-12-13
