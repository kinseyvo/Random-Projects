from datetime import datetime

entry = input("Write your jornal entry for the day: ")
date = datetime.now().strftime("%m-%d-%Y")

with open("journal.txt", "a") as f:
    f.write(f"## {date}\n{entry}\n\n")

print("Daily Entry Complete :))")