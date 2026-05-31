import json

MEMORY_FILE = "memory.json"

def load_memory():

    try:

        with open(MEMORY_FILE, "r", encoding="utf-8") as f:
            return json.load(f)

    except:

        return []

def save_memory(memory):

    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump(memory, f, indent=2)

def add_memory(event):

    memory = load_memory()

    memory.append(event)

    # Keep last 8 memories
    memory = memory[-8:]

    save_memory(memory)