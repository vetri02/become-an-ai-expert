# Lab contract

What the thirteen labs promise to anyone who relies on them or extends them.

## Promise

- Each lab is one file, standard library plus NumPy, runnable with `python3 labs/labNN_name.py` from the course root or `./run_all.sh` from `labs/`.
- Each prints the measurement that backs one or more first principles and ends with `OK`; a false principle makes an assertion fail with a message that says what was expected.
- Seeds are fixed. Numbers printed in the modules and in FIRST-PRINCIPLES.md were produced by these files on 2026-11-05 on Python 3.14 with NumPy 2.5; small platform differences in timing lines (lab 03, lab 12) are expected, assertion thresholds leave room for them.
- No lab needs a GPU, a network connection, a key or more than a minute.

## Not promised

- The labs are not the projects. They show a mechanism; the modules' projects apply it to a real system.
- Lab 03's decoder, lab 09's policy and lab 10's reader are toys. The invariants are real; the models are not.
- Lab 12's measured batch effect depends on your CPU's BLAS; the assertion asks only for a clear gap.

## Extending

Copy a lab, change one variable, add one assertion, and write the paragraph. That is Project 7 (an ablation) at its smallest.
