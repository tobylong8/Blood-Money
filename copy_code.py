import pyperclip
import os

project_root = "."

files = [
    "main.py", 
    "characters/player.py", 
    "characters/npcs.py", 
    "characters/enemies.py", 
    "utils.py", 
    "story_state.py", 
    "combat.py", 
    "story/prologue.py"
]

output = "Here are the files for my project:\n\n"

for file in files:
    filepath = os.path.join(project_root, file)
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            output += f"### File: {file}\n"
            output += "```python\n"
            output += f.read().strip()
            output += "\n```\n\n"
    except FileNotFoundError:
        print(f"Warning: '{filepath}' not found. Skipping...")

if output != "Here are the files for my project:\n\n":
    pyperclip.copy(output)
    print("Formatted prompt copied to clipboard!")
else:
    print("No code was found to copy.")