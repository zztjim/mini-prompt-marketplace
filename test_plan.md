# Test Plan

| ID | Test Case | Input | Expected Output |
|----|------------|--------|----------------|
| T1 | Login with valid username | "Alice" | Redirect to upload page |
| T2 | Submit full prompt | Title, Description, Sample Output | Prompt appears on “All Prompts” page |
| T3 | Leave a blank field | Missing field | Error or no redirect |
| T4 | View all prompts | Access `/prompts` | All uploaded prompts listed |
| T5 | Logout | Click logout | Redirect to login page |
