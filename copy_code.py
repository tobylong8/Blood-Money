import pyperclip

files = ["main.py", "characters.py", "utils.py", "combat.py", "story.py"]

output = "Here are the files for my project:\n\n"

for file in files:
    try:
        with open(file, "r", encoding="utf-8") as f:
            output += f"### File: {file}\n"
            output += "```python\n"
            output += f.read().strip()
            output += "\n```\n\n"
    except FileNotFoundError:
        print(f"Warning: '{file}' not found. Skipping...")

if output:
    pyperclip.copy(output)
    print("Formatted prompt copied to clipboard!")
else:
    print("No code was found to copy.")
