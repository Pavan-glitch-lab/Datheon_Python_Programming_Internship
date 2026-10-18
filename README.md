
# Datheon Python Programming Internship

This repository contains the projects completed during my Python Programming Internship at Datheon.

## Task 1: Hangman Game

### Description
A simple word-guessing game developed using Python. The player guesses a hidden word one letter at a time.

### Files
- `hangman.py` - Main game program.
- `words.txt` - List of words used in the game.

### Technologies
- Python 3
- File handling

## Task 2: Stock Portfolio Tracker

### Description
A Python program that tracks stock investments and calculates invested capital, current market value, and profit or loss for each holding.

### Features
- Enter stock ticker symbols, buying prices, and quantities.
- Read sample stock prices from a CSV file.
- Calculate the market value of each holding.
- Calculate percentage gain or loss.
- Display total investment and overall return.
- Save the portfolio summary to a CSV file.

### Files
- `portfolio.py` - Main program.
- `sample_prices.csv` - Sample stock prices.
- `constituents.csv` - S&P 500 ticker dataset.
- `portfolio_summary.csv` - Generated portfolio summary.

### Technologies
- Python 3
- CSV module
- File handling

**Note:** Task 2 uses illustrative sample prices, not live stock market prices.

## Task 3: File Organizer

### Description
A Python automation utility that organizes files into category folders based on their file extensions.

### Features
- Automatically creates Documents, Images, Videos, Archives, and Code folders.
- Moves files according to their extensions.
- Avoids overwriting files by generating unique filenames.
- Handles permission and file-operation errors.
- Records operations and errors in a log file.
- Displays a summary of moved, skipped, and failed files.

### Files
- `organizer.py` - Main file organizer program.

### Technologies Used
- Python 3
- `os`
- `shutil`
- `pathlib`
- `logging`

### How to Run
1. Open a terminal inside the `Task-3-File-Organizer` folder.
2. Run `python organizer.py`.
3. Enter the path of the folder you want to organize.

**Note:** Test the program on a sample folder before using it on important directories.

## Task 4: Rule-Based Interactive Terminal Chatbot

### Description
An interactive, rule-based chatbot developed using Python. It recognizes user intents through keywords and regular expressions and provides contextual responses to common internship support questions.

### Features
- Recognizes greetings and multiple intents in a single message.
- Answers frequently asked questions about business hours, project submission, and certificates.
- Loads FAQ questions and answers from a JSON file.
- Normalizes user input by converting it to lowercase and removing extra whitespace.
- Uses regular expressions for keyword and intent recognition.
- Provides fallback responses for unrecognized questions.
- Supports `help` and `faq` commands.
- Maintains conversation history during the current session.
- Remembers the user's name during the current session.
- Supports clean exit commands: `bye`, `goodbye`, `good bye`, `exit`, and `quit`.
- Handles missing FAQ files and invalid JSON data with an error message.

### Files
- `chatbot.py` - Main chatbot program.
- `faq.json` - Contains greeting patterns and frequently asked questions with their answers.

### Technologies Used
- Python 3
- `re` - Regular expressions
- `json` - FAQ data handling
- `pathlib` - File path handling

### How to Run
1. Open a terminal inside the `Task-4-Rule-Based-Chatbot` folder.
2. Run `python chatbot.py`.
3. Ask questions about business hours, internship project submission, or certificates.
4. Type `help` to view supported commands.
5. Type `faq` to display available FAQ questions.
6. Type `history` to view the conversation history.
7. Type `bye`, `goodbye`, `exit`, or `quit` to stop the chatbot.

**Note:** This is a rule-based chatbot. Its responses depend on predefined keywords, regular expressions, and FAQ data. Name memory and conversation history are maintained only for the current session.

## Technologies Used Across Projects

- Python 3
- File handling
- CSV and JSON
- Regular expressions
- File system automation
- Logging and exception handling
- Git and GitHub


## Repository Structure

```text
Datheon_Python_Programming_Internship/
├── Task-1-Hangman-Game/
│   ├── hangman.py
│   └── words.txt
├── Task-2-Portfolio-Tracker/
│   ├── portfolio.py
│   ├── sample_prices.csv
│   ├── constituents.csv
│   └── portfolio_summary.csv
├── Task-3-File-Organizer/
│   └── organizer.py
├── Task-4-Rule-Based-Chatbot/
│   ├── chatbot.py
│   └── faq.json
└── README.md
```

## Author

Pavan Gowda C B

