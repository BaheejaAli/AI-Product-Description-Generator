# AI Product Description Generator

Generate professional product descriptions from product names and features using AI.

## Overview

AI Product Description Generator is a full-stack AI application that generates professional product descriptions from a product name and a list of product features.

The application uses a structured multi-step AI workflow consisting of a Planner, Executor, and Validator. The Planner analyzes the product information and creates a writing plan, the Executor generates the description using an LLM, and the Validator checks the generated output before it is returned to the user.

The application also includes input validation, conditional retry handling, API error handling, and a React-based user interface.

## Key Features

- AI-powered product description generation
- Multi-step AI workflow
- Planner → Executor → Validator architecture
- Context passing between workflow steps
- Conditional retry when validation fails
- LLM integration through OpenRouter API
- Input validation using Django REST Framework serializers
- AI output validation
- API and LLM error handling
- User-friendly error messages
- React-based frontend
- Django REST Framework backend
- REST API for product description generation
- Postman API testing

## AI Workflow

```text
User Input
    ↓
Planner
    ↓
Plan
    ↓
Executor
    ↓
OpenRouter LLM API
    ↓
Generated Description
    ↓
Validator
    ↓
Valid?
 ├── Yes → Final Output
 └── No  → Retry Executor
```

### Workflow Steps

**1. Planner**

Analyzes the product name and features and creates a structured writing plan.

**2. Executor**

Uses the original product information and the Planner's output to construct the generation prompt and request the product description from the LLM.

**3. Validator**

Checks whether the generated description is valid and contains the required product name.

**4. Conditional Retry**

If validation fails, the Executor is called again using the existing Planner output.

This prevents an invalid AI response from being returned directly to the user.

## Application Architecture

```text
React Frontend
      ↓
Django REST API
      ↓
Workflow Orchestrator
      ↓
Planner
      ↓
Executor
      ↓
OpenRouter LLM
      ↓
Validator
      ↓
Final Response
      ↓
React UI
```

The Django backend acts as the orchestration layer. It receives and validates user input, executes the AI workflow, handles validation and retry logic, and returns the final result to the frontend.

## Tech Stack

### Frontend

- React
- Vite
- JavaScript
- CSS

### Backend

- Python
- Django
- Django REST Framework

### AI Integration

- OpenRouter API
- OpenAI-compatible API client
- LLM-based prompt processing

### Development Tools

- Git
- GitHub
- Postman
- VS Code

## Project Structure

```text
ai-product-description-generator/
│
├── backend/
│   ├── config/
│   │   ├── settings.py
│   │   └── urls.py
│   │
│   ├── products/
│   │   ├── planner.py
│   │   ├── executor.py
│   │   ├── validator.py
│   │   ├── workflow.py
│   │   ├── prompts.py
│   │   ├── llm.py
│   │   ├── serializers.py
│   │   ├── views.py
│   │   └── urls.py
│   │
│   ├── manage.py
│   ├── requirements.txt
│
├── frontend/
│   └── src/
│       ├── components/
│       │   ├── Header.jsx
│       │   ├── ProductForm.jsx
│       │   └── DescriptionResult.jsx
│       │
│       ├── services/
│       │   └── productService.js
│       │
│       ├── App.jsx
│       ├── App.css
│       └── main.jsx
│
└── docs/
    └── ai-product-description-workflow.png
```

## Setup

### 1. Clone the Repository

```bash
git clone https://github.com/BaheejaAli/AI-Product-Description-Generator.git
cd AI-Product-Description-Generator
```

### 2. Backend Setup

Navigate to the backend:

```bash
cd backend
```

Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Create a `.env` file inside the `backend` directory:

```env
OPENROUTER_API_KEY=your_api_key
OPENROUTER_MODEL=openrouter/free
```

Run migrations:

```bash
python manage.py migrate
```

Start the Django development server:

```bash
python manage.py runserver
```

The backend will be available at:

```text
http://127.0.0.1:8000/
```

### 3. Frontend Setup

Open another terminal and navigate to the frontend:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Start the Vite development server:

```bash
npm run dev
```

The frontend will be available at:

```text
http://localhost:5173/
```

### 4. Using the Application

1. Enter a product name.
2. Add one or more product features.
3. Click **Generate with AI**.
4. The request is sent to the Django REST API.
5. The request passes through the multi-step AI workflow.
6. The generated description is validated.
7. The final description is displayed in the React interface.

## API

### Generate Product Description

**Endpoint**

```text
POST /api/products/generate/
```

### Request

```json
{
  "product_name": "Wireless Bluetooth Headphones",
  "features": [
    "Bluetooth 5.3",
    "40-hour battery life",
    "Noise cancellation",
    "Lightweight design",
    "Fast charging"
  ]
}
```

### Response

```json
{
  "description": "Generated product description..."
}
```

## Error Handling

The application handles failures at multiple stages.

### Input Validation

Invalid product names and empty feature lists are rejected before the AI workflow runs.

The Django REST Framework serializer validates incoming API data.

### AI Output Validation

The Validator checks the generated description before it is returned to the user.

The current validation checks that:

- The AI returned a response.
- The response is valid text.
- The generated description contains the product name.

### Conditional Retry

If the generated output fails validation, the Executor is called again using the existing Planner output.

```text
Executor
   ↓
Validator
   ↓
Valid?
 ├── Yes → Final Output
 └── No  → Retry Executor
```

### LLM / API Failure

If the AI service fails, the backend catches the exception and returns a user-friendly error response instead of exposing internal errors.

## Example

### Input

```text
Product Name:
Wireless Bluetooth Headphones

Features:
- Bluetooth 5.3
- 40-hour battery life
- Noise cancellation
- Lightweight design
- Fast charging
```

### Processing

```text
Product Information
       ↓
Planner
       ↓
Writing Plan
       ↓
Executor
       ↓
OpenRouter LLM
       ↓
Generated Description
       ↓
Validator
       ↓
Final Description
```

### Output

```text
A professional product description generated by the AI workflow.
```

## Testing

The application was tested at multiple levels.

### Workflow Testing

- Planner execution
- Executor execution
- Validator execution
- Complete workflow execution
- Conditional retry flow

### API Testing

- Successful product description generation
- Empty product name
- Empty feature list
- Invalid API input
- LLM/API failure handling

### Frontend Testing

- Product name validation
- Feature validation
- Successful AI generation
- API error handling
- Display of generated descriptions

Postman was used to test the backend API independently from the React frontend.