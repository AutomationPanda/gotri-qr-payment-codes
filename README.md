# GoTri QR Payment Codes

This repository contains the example code for Chapter 4 in Andrew Knight's book, *The Way To Test Software*.
Each section of the chapter iteratively builds a small test automation solution in Python
to test QR payment codes for a fictitious public transit system named "GoTri".

The example code for each section is placed into subdirectories within this repository
so you can view and execute the progress as a snapshot made at each stage of its development.

1. Section 4.1 shows a few functions for generating QR payment codes.
2. Section 4.2 shows how to build a custom test framework from scratch.
3. Section 4.3 shows how to rewrite the entire test solution using [`pytest`](https://docs.pytest.org/).
4. Section 4.4 shows a new set of tests developed using *Test-Driven Development* (TDD).


## Installation

The example code should work on any operating system (Windows, macOS, Linux).
To install it:

1. Install [Python](https://www.python.org/) 3.8 or higher.
2. Clone this repository onto your local machine.
3. Install dependency packages from the command line:
   * Change directory to the project's root directory.
   * Run `pip install -r requirements.txt` to install all dependencies.


## Execution

Each section subdirectory functions as its own project.
The table below shows how to execute the code at each snapshot.
Change directory into the project subdirectory before running commands.

| Section | Project Subdirectory | Execution Commands |
| ------- | -------------------- | ------------------ |
| 4.1     | `gotri_app`          | Load and call functions from the `qrcodes` module in the `python` interpreter |
| 4.2.2   | `gotri_app`          | `python test_qrcodes.py`  |
| 4.2.3   | `gotri_app`          | `python test_qrcodes.py`  |
| 4.2.4   | `gotri_app`          | `python run_all_tests.py` |
| 4.2.5   | `gotri_app`          | `python run_all_tests.py` |
| 4.2.6   | `gotri_app`          | `python run_all_tests.py` |
| 4.2.7   | `gotri_app`          | `python run_all_tests.py` |
| 4.3     | `gotri_app_pytest`   | `python -m pytest tests`  |
| 4.4.2   | `gotri_app_pytest`   | `python -m pytest tests`  |
| 4.4.3   | `gotri_app_pytest`   | `python -m pytest tests`  |
| 4.4.4   | `gotri_app_pytest`   | `python -m pytest tests`  |