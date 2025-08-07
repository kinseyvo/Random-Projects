# 🧮 Command-Line Calculator with History
A simple Python calculator that evaluates arithmetic expressions from the command line and stores a history of calculations in a local JSON file.

## 🚀 Features
- Supports basic math expressions (`+`, `-`, `*`, `/`)
- Saves expression and result history to `history.json`
- View or clear history from the command line

## 🧰 Requirements
- Python 3.x

## Files
- calculator.py - main script
- history.json - stores calculation history (auto-created)

## 🛠 Usage

```bash
# Run a calculation
python calculator.py "9 + 28"

# Show calculation history
python calculator.py --history

# Clear calculation history
python calculator.py --clear

# Example
$ python calculator.py "10 / 3"
10 / 3 = 3.3333333333333335

$ python calculator.py --history
9 + 28 = 37
10 / 3 = 3.3333333333333335
