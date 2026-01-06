# HIPAA-Compliant Patient Encounter API
## Setup & Running
- Dependencies installation
pyenv local 3.11 
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

- How to run the application
uvicorn server:app

- How to run tests
pytest tests/

## Design Decisions
- Key architectural choices and why
1. Resource structure of routes, controllers and repositories for separation of usability and business logic.
2. 
- Trade-offs you considered
- What you'd change for production
1. Repository with MySQL DB instead of in-memory storage.
2. 

## Testing Philosophy
### What I Tested
- [E2E schema validation test]: this tests the full flow of the app, ensures the schema validation occurs, and that PHIs are redacted.
- [Internal business logic test]: 
- [Data integrity test]:
### What I'd Test With More Time (Prioritized)
1. Data entered is data retrieved
2. User only gets audits of their own records
### How I Made This Testable
- Design decisions that enable testing
- Mocking strategy
- Test isolation approach

## Time Breakdown (Optional)
40 min repo structure + rough encounter implementation
30 min detailed encounter + audit implementation + extras 
30 min rough local run and tests
30 min local run and tests and README writeup
