# Boggle Game in Python

A Python implementation of the **Boggle** word game with a graphical user interface (GUI) using **Tkinter**, including random board generation, word validation, scoring system, and countdown timer.

## Features

- Random 4x4 Boggle board generation.
- GUI with clickable letter buttons and word display.
- Real-time score calculation based on word length.
- Remaining time display and countdown timer.
- Validation of words against a dictionary (`boggle_dict.txt`).
- Highlighting selected letters while forming words.
- Option to restart the game when time runs out.

## Files

- `boggle.py` – Main program that runs the game.
- `ex12_utils.py` – Utility functions for word validation and path checking.
- `boggle_board_randomizer.py` – Generates a random Boggle board.
- `boggle_dict.txt` – Dictionary of valid words (do not modify).
- `bogglewallpaper.png` – Background image for the menu (optional).
- `AUTHORS` – Names of the contributors.

## How to Run

Make sure all files are in the same folder. Then, run the game using:

```bash
python3 boggle.py
