# Odd-Even Cricket Game

A modular, terminal-based Python simulation of the classic Hand Cricket game played between a user and the computer.

## Overview
This project provides an interactive simulation of traditional Odd-Even cricket. It features an automated toss, dynamic run tracking, boundary condition validation, and match outcome evaluation. The codebase is organized into modular Python files to separate game engine logic, user input sanitization, terminal display rendering, and computer decision-making.

## Features
* **Rule-Based Toss:** Interactive Odd-Even toss resolving batting and bowling rights.
* **Match Mechanics:** Standard two-innings format limited to 12 legal deliveries or 1 wicket per side.
* **Dynamic Target Calculation:** Real-time scoring updates and early chase termination upon passing the target.
* **Defensive Input Handling:** Catches conversion errors, empty inputs, and numbers outside the valid 1–6 range without crashing.
* **Computer Opponent:** Randomized adversary choices for fair delivery outcomes.
* **Session Management:** Post-match summary with an interactive replay loop.

## Technologies Used
* **Language:** Python 3
* **Standard Libraries:** `random`, `sys`
* **Development Environment:** Visual Studio Code / Terminal
* **Version Control:** Git & GitHub

## Project Structure
```text
Vityarthi_project-/
├── main.py          # Entry point and match orchestrator
├── engine.py        # Core innings and target evaluation logic
├── player.py        # Computer adversary decision routines
├── validator.py     # Input sanitization and bounds checking
├── display.py       # Terminal UI and scoreboard formatting
├── test_cricket.py  # Unit test suite
├── statement.md     # Project scope and problem statement
└── README.md        # Documentation and execution guide