import json, argparse, os

HISTORY_FILE = "history.json"

def load_history():
    if not os.path.exists(HISTORY_FILE):
        return []
    with open(HISTORY_FILE, "r") as f:
        return json.load(f)
    
def save_history(history):
    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=2)
    
def evaluate(expr):
    try:
        result = eval(expr)
        return result
    except Exception as e:
        return f"Error: {e}"

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("expression", nargs="?", help="Expression to evaluate, like '2 + 2'")
    parser.add_argument("--history", action="store_true", help="Show calculation history")
    parser.add_argument("--clear", action="store_true", help="Clear calculation history")

    args = parser.parse_args()
    history = load_history()

    if args.clear:
        save_history([])
        print("History cleared.")
        return
    
    if args.history:
        for item in history:
            print(f"{item['expr']} = {item['result']}")
        return
    
    if args.expression:
        result = evaluate(args.expression)
        print(f"{args.expression} = {result}")
        history.append({"expr": args.expression, "result": result})
        save_history(history)
    else:
        print("No expression provided. Use --help for options.")

if __name__ == "__main__":
    main()