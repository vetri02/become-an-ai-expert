# Entry diagnostic

About an hour. Answer the ten questions in writing without looking anything up, then do the four tasks. Mark yourself against the key only when done: on the website it is collapsed at the bottom of this page; in the course folder it is `instructor/assessment-answers.md`. The readiness rule tells you where to start.

## Ten questions

1. What is the difference between a list and a dict lookup in Python, and when does it matter?
2. What happens, step by step, when a browser requests a URL from an API you wrote?
3. What does a virtual environment solve, and what does Docker solve that it does not?
4. Read this error and say which line caused it: `KeyError: 'user_id'` raised inside `handlers.py line 42` called from `app.py line 17`.
5. Write a SQL query that returns the three customers with the most orders in 2025.
6. What is a p-value, in one sentence a colleague would accept?
7. A model is 99% accurate on data where 99% of rows are one class. What is wrong, and what would you measure instead?
8. What is a gradient, and why do we subtract it?
9. Multiply a 2x3 matrix by a 3x1 vector. What shape results?
10. What is the difference between git merge and git rebase, in practice?

## Four practical tasks

1. Clone any public repository, create a branch, change one line, commit, and show the diff. Five minutes.
2. Write a function with a bug, write a pytest test that catches it, fix it, show the test passing. Fifteen minutes.
3. Load any CSV with about 1,000 rows (a city open-data file will do) into SQLite or pandas and answer: how many rows per category, and the mean of one numeric column per category. Ten minutes.
4. Get the course code first (the "Get the code" section of Set up the lab), then run `labs/lab01_gradient_descent.py` and explain in two sentences what the printed numbers mean. Ten minutes once the code is there.

## Readiness rule

- **8 or more questions right and all four tasks done:** start Module 01.
- **5 to 7 questions right, or one task failed:** do the Foundation bridge (40 hours), then Module 01.
- **Fewer than 5, or two or more tasks failed:** take Path A, the on-ramp from zero (A1 to A5, about 210 hours), then join at Module 03. Choose Novice in the sidebar and the site puts it into your path.

Be strict. The course assumes the base; the diagnostic is cheaper than discovering a gap in week 10.
