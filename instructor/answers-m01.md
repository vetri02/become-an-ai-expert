### Answer key: Module 01

### Quiz answers and reasoning

1. The key is hashed to a bucket, so lookup cost does not depend on size (amortised constant). Keys must be hashable and immutable in the relevant sense; a mutable key would change its hash.
2. Retry with exponential backoff and jitter, a bounded number of attempts, and a per-attempt timeout. The request must be idempotent (or carry an idempotency key) so a retry after an ambiguous failure cannot double-apply an effect.
3. The operating system, system libraries, binaries and environment variables. A venv only isolates Python packages.
4. Environment differences (Python or dependency versions, missing env vars), test order or shared state, and timing or network assumptions. Check the CI logs for the first difference, pin versions, and make tests independent.
5. The Global Interpreter Lock lets only one thread execute Python bytecode at a time in a process. It matters when a serving process does CPU-bound Python work per request; it matters less when the work is I/O or inside native code (NumPy, tokenizers), and multiprocessing or async sidesteps it.
6. File handles leak until the process hits its limit; errors are hidden so the service appears healthy while failing. Caught by a test that asserts on the error path, a linter, and reading the diff before merging.

### Lab assessment and mastery gate

The reviewer runs the three commands from a clean clone. Any manual step not in the README fails the gate. The explanation check is oral or written; "I'd have to look" on any function fails it. The profiling evidence must show numbers before and after.

### How to use this key

Open after attempting every question in writing. Mark yourself strictly; the questions reappear in interviews.
