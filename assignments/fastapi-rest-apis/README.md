# 📘 Assignment: REST APIs with FastAPI

## 🎯 Objective

Build a simple REST API using FastAPI to practice creating endpoints, handling request data, and returning structured JSON responses.

## 📝 Tasks

### 🛠️ Create Core API Endpoints

#### Description
Set up a FastAPI application and implement foundational endpoints for health checking and item retrieval.

#### Requirements
Completed program should:

- Create a FastAPI app in `starter-code.py`.
- Add a `GET /health` endpoint that returns `{"status": "ok"}`.
- Add a `GET /items` endpoint that returns a list of at least 3 sample items.


### 🛠️ Add Item Creation and Validation

#### Description
Expand the API so users can create new items and receive clear validation feedback when data is incomplete or invalid.

#### Requirements
Completed program should:

- Define a Pydantic model for an item with `name`, `price`, and `in_stock` fields.
- Add a `POST /items` endpoint that accepts an item and stores it in memory.
- Return the created item in the response and show automatic validation errors for invalid input.
