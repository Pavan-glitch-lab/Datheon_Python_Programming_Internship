
# Hangman Game

A terminal-based Hangman game developed using Python 3.

## Features

- Random English word selection
- Letter-by-letter word guessing
- Maximum of 6 incorrect guesses
- ASCII gallows art updated after incorrect guesses
- Tracks previously guessed letters
- Prevents duplicate penalty deduction
- Displays victory and defeat messages
- Option to play again

## Technologies Used

- Python 3
- Python standard library (`random`)
- Visual Studio Code

## Project Files

- `hangman.py` - Main game program
- `words.txt` - English word list

## How to Run

1. Install Python 3.
2. Keep `hangman.py` and `words.txt` in the same folder.
3. Open the project folder in VS Code.
4. Open the terminal.
5. Run:

   python hangman.py

## How to Play

1. Run the game.
2. Guess one letter at a time.
3. Avoid making more than six incorrect guesses.
4. Guess the complete word to win.

## Author
Pavan Gowda C B

## Task 2: Stock Portfolio Tracker

### Description
A Python program that tracks stock investments by calculating
total invested capital, current portfolio value, and profit or
loss for each stock holding.

### Features
- Enter stock ticker symbols, buying prices, and share quantities.
- Read sample stock prices from a CSV file.
- Calculate the market value of each holding.
- Calculate percentage gain or loss for each stock.
- Display total investment, portfolio value, and overall return.
- Save the portfolio summary to a CSV file.

### Files
- `portfolio.py` - Main Python program.
- `sample_prices.csv` - Sample stock prices.
- `constituents.csv` - S&P 500 ticker dataset.
- `portfolio_summary.csv` - Generated portfolio summary.

### Technologies Used
- Python 3
- CSV module
- File handling

### How to Run
1. Open the terminal in the Task 2 folder.
2. Run:

   `python portfolio.py`

3. Enter stock tickers, buying prices, and share quantities.
4. Enter `done` to display and save the portfolio summary.

**Note:** The program uses illustrative sample prices, not live
stock market prices.