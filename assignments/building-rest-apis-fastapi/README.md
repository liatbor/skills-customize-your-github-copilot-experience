```markdown
# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Create a small REST API using the FastAPI framework to learn routing, request handling, validation, and running a local development server.

## 📝 Tasks

### 🛠️ Task 1 — Basic API Endpoints

#### Description
Build a FastAPI application that exposes CRUD-style endpoints for a simple resource (e.g., `notes` or `tasks`).

#### Requirements
Completed project should:

- Implement at least the following endpoints:
  - `GET /items/` — list items
  - `GET /items/{id}` — retrieve a single item
  - `POST /items/` — create a new item
  - `PUT /items/{id}` or `PATCH /items/{id}` — update an item
  - `DELETE /items/{id}` — remove an item
- Use Pydantic models for request/response validation.
- Store items in an in-memory list or dictionary (no DB required).
- Return appropriate HTTP status codes.

### 🛠️ Task 2 — Validation & Error Handling (required)

#### Description
Add input validation and clear error responses.

#### Requirements

- Validate request payloads with Pydantic and return `422` on invalid input.
- Return `404` when an item is not found.
- Return helpful JSON error messages for client errors.

### 🛠️ Task 3 — Optional Enhancements

#### Description
Add at least one enhancement to improve developer experience or API features.

#### Examples

- Add query parameters for pagination or filtering.
- Add simple authentication (API key via headers).
- Persist items to a local JSON file.

```
