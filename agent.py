import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

MODEL = "llama3.2:3b"

VALID_ACTIONS = [
    "eat",
    "drink",
    "rest",
    "explore",
    "do_nothing"
]

def build_prompt(state, memory):

    memory_text = "\n".join(memory)

    prompt = f"""
You are a survival agent trapped in a dangerous wilderness.

Your ONLY goal is long-term survival.

You can die from:
- starvation
- dehydration
- low energy
- dangerous exploration
- environmental disasters

Important:
- Food and water are LIMITED.
- Exploration is dangerous but necessary.
- Resting forever will eventually kill you.
- You must balance risk and survival.

Current State:
Day: {state['day']}
Health: {state['health']}
Hunger: {state['hunger']}
Thirst: {state['thirst']}
Energy: {state['energy']}
Food Supply: {state['food_supply']}
Water Supply: {state['water_supply']}

Recent Memory:
{memory_text}

Available Actions:
eat
drink
rest
explore
do_nothing

First explain your reasoning briefly.

Then write:
ACTION: <chosen action>
"""

    return prompt

def get_action(state, memory):

    prompt = build_prompt(state, memory)

    payload = {
        "model": MODEL,
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload)

    text = response.json()["response"].strip().lower()

    print("\nMODEL RESPONSE:")
    print(text)

    for action in VALID_ACTIONS:

        if f"action: {action}" in text:
            return action, text

    for action in VALID_ACTIONS:

        if action in text:
            return action, text

    return "do_nothing", text