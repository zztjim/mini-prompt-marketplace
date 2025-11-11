# Risk Table

| Risk | Likelihood | Impact | Mitigation |
|-------|-------------|---------|-------------|
| Database file locked | Medium | Medium | Close connection after each query |
| Form submission error | High | Low | Validate inputs on both frontend/backend |
| Merge conflicts | Medium | Medium | Coordinate pushes and use branches |
| Flask crash during test | Low | Medium | Restart locally and check routes |
