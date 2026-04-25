# Project Overview

Production-grade FastAPI backend designed for scalability, maintainability, and clean architecture.

Focus: clear separation of concerns, async performance, and service-oriented design.

---

# Core Principles

## Code quality
- Write concise, explicit, and production-ready code
- Prefer functional and modular design over unnecessary classes
- Avoid duplication; reuse services and utilities
- Use descriptive variable names (is_active, has_permission, etc.)
- Use lowercase_with_underscores for files and modules

## Architecture mindset
- Strict separation of concerns:
  routes → services → schemas → utils
- Keep API layer thin and logic-free
- Business logic must live in services layer

---

# Architecture Layers

## Responsibilities

- **routes/** → HTTP layer only (request/response handling)
- **services/** → business logic (core domain logic)
- **schemas/** → Pydantic validation (input/output models)
- **models/** → database structure (if ORM used)
- **utils/** → reusable helpers

---

# Function Design Principles

- Prefer `def` for pure functions
- Use `async def` for I/O-bound operations
- Use type hints for all functions
- Use RORO pattern (Receive Object, Return Object)
- Always use structured inputs/outputs (Pydantic models)

---

# API Layer Rules (FastAPI)

- Routes must be thin and declarative
- No business logic in routes
- Always use dependency injection for services
- Use explicit request/response schemas
- Keep route functions short and readable

---

# Error Handling

## Principles
- Handle errors early using guard clauses
- Avoid deep nesting
- Keep happy path last
- Use explicit exception types

## Standards
- Use HTTPException for expected errors
- Centralized exception handling middleware
- Log all unexpected errors with context
- Return consistent error structure

---

# Performance Rules

## Async-first design
- Use async for all database and external API calls
- Avoid blocking operations in request lifecycle

## Optimization
- Cache frequent reads (Redis recommended)
- Use lazy loading for large datasets
- Optimize serialization using Pydantic
- Monitor latency and throughput

---

# Dependencies (Recommended Stack)

- FastAPI
- Pydantic v2
- async database driver (asyncpg / aiomysql)
- SQLAlchemy 2.0 (optional ORM)
- Redis (caching layer)

---

# Middleware Strategy

Use middleware for:
- Request/response logging
- Error tracking
- Performance monitoring
- Rate limiting (optional)

---

# Dependency Injection

- Use FastAPI dependency injection system
- Never use global state for services or DB connections
- Inject database sessions and services explicitly

---

# Database Rules

- Use async database access only
- Avoid N+1 queries
- Keep DB logic inside services layer or ORM helpers
- Use transactions for critical operations

---

# Validation Strategy

- All inputs must use Pydantic models
- Never accept raw dicts in routes
- Validate at API boundary only

---

# Services Layer (Core Rule)

- All business logic lives here
- Services handle:
  - data processing
  - DB interactions
  - external API calls

- Routes must only call services

---

# Error Handling Strategy

- Use consistent API error format
- Never expose internal stack traces
- Use custom exceptions where needed
- Centralize error formatting

---

# Logging Strategy

- Log requests and responses
- Log slow operations
- Log exceptions with context
- Use structured logging format

---

# Key Conventions

- Keep routes thin
- Keep services logic-heavy
- Keep schemas clean and minimal
- Keep utils stateless and reusable
- Prefer composition over inheritance

---

# Non-negotiable Rules

- No business logic in routes
- No blocking code in async endpoints
- No raw dict inputs/outputs in API layer
- No duplicated logic across services
- No global state for services or DB
- No unhandled exceptions in production