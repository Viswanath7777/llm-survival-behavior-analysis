from game import initialize_state, update_state
from agent import get_action
from memory import load_memory, add_memory
from logger import log

MAX_DAYS = 50

state = initialize_state()

action_counts = {
    "eat": 0,
    "drink": 0,
    "rest": 0,
    "explore": 0,
    "do_nothing": 0
}

print("\nSTARTING SURVIVAL SIMULATION\n")

while state["alive"] and state["day"] <= MAX_DAYS:

    memory = load_memory()

    action, reasoning = get_action(state, memory)

    action_counts[action] += 1

    current_day = state["day"]

    state, result = update_state(state, action)

    memory_event = f"""
Day {current_day}
Action: {action}
Result: {result}
"""

    add_memory(memory_event)

    output = f"""
================================
DAY {current_day}

REASONING:
{reasoning}

ACTION:
{action}

RESULT:
{result}

STATE:
Health={state['health']}
Hunger={state['hunger']}
Thirst={state['thirst']}
Energy={state['energy']}
Food Supply={state['food_supply']}
Water Supply={state['water_supply']}

================================
"""

    print(output)

    log(output)

print("\nSIMULATION COMPLETE\n")

if state["alive"]:

    print(f"Agent survived all {MAX_DAYS} days.")

else:

    print(f"Agent died on day {state['day']}.")

print("\nACTION COUNTS:")

for action, count in action_counts.items():

    print(f"{action}: {count}")

log("\nFINAL ACTION COUNTS\n")

for action, count in action_counts.items():

    log(f"{action}: {count}")