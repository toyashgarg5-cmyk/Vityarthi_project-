# Project Statement

## Problem Statement
Traditional physical Hand Cricket (Odd-Even) is a popular casual game, but informal play often encounters disputes such as synchronous gesture timing, human scorekeeping mistakes, and ambiguous boundary or target resolutions. Furthermore, beginner software recreations often implement the game as a single monolithic script that crashes on invalid inputs and tightly couples game rules with terminal printing.

This project addresses these issues by developing a modular, deterministic command-line simulation engine. The solution formalizes the complete rule set, automates target resolution, prevents runtime crashes through defensive input validation, and separates application concerns into dedicated modules.

## Scope of the Project
The scope encompasses a complete two-innings cricket simulation played between a human user and an automated computer adversary:
* Rule-based Odd-Even toss to determine choice of batting or bowling.
* Dynamic two-innings match cycle restricted to 12 legal deliveries or 1 wicket per innings.
* Input validation pipeline ensuring valid parity calls and bounded integer entries (1 to 6).
* Real-time target calculation and early termination checks during the second innings.
* Match verdict computation (win by runs, win by wickets, or tie) with replay session handling.
* Out of scope: Persistent database storage, graphical interfaces, and network multiplayer.

## Target Users
* Casual users seeking a quick, lightweight, and deterministic terminal-based game.
* Students and developers examining a clean reference implementation of modular architecture, input sanitization, and state-machine transitions in Python.

## High-Level Features
* **Modular Architecture:** Split across distinct components for input validation, adversary logic, game engine, and terminal display.
* **Defensive Validation:** Continuous loop error handling preventing crashes from alphabetic inputs, empty lines, or out-of-range integers.
* **Autonomous Computer Adversary:** Random-choice generation simulating fair deliveries and toss selections.
* **Dynamic Target Tracking:** Instant chase-cutoff logic terminating the game as soon as the target score is reached.
* **Session Orchestration:** End-of-game result summaries and clean match replay loops.