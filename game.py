import random

def initialize_state():

    return {
        "day": 1,
        "health": 100,
        "hunger": 20,
        "thirst": 20,
        "energy": 100,
        "food_supply": 2,
        "water_supply": 2,
        "alive": True
    }

def update_state(state, action):

    result = ""

    # Passive survival decay
    state["hunger"] += 10
    state["thirst"] += 10
    state["energy"] -= 5

    # -----------------------------
    # EAT
    # -----------------------------

    if action == "eat":

        if state["food_supply"] > 0:

            state["food_supply"] -= 1
            state["hunger"] -= 40

            result = "You consumed stored food."

        else:

            result = "You have no food left."

    # -----------------------------
    # DRINK
    # -----------------------------

    elif action == "drink":

        if state["water_supply"] > 0:

            state["water_supply"] -= 1
            state["thirst"] -= 40

            result = "You drank stored water."

        else:

            result = "You have no water left."

    # -----------------------------
    # REST
    # -----------------------------

    elif action == "rest":

        state["energy"] += 25

        result = "You rested and recovered energy."

    # -----------------------------
    # EXPLORE
    # -----------------------------

    elif action == "explore":

        # Exploration costs energy
        state["energy"] -= 15

        outcome = random.choice([
            "food",
            "food",
            "water",
            "water",
            "danger",
            "danger",
            "nothing"
        ])

        # FOOD FOUND
        if outcome == "food":

            state["food_supply"] += 1

            result = "You found food supplies."

        # WATER FOUND
        elif outcome == "water":

            state["water_supply"] += 1

            result = "You found clean water."

        # DANGER
        elif outcome == "danger":

            damage = random.randint(20, 40)

            state["health"] -= damage

            result = f"You were attacked while exploring and lost {damage} health."

        # NOTHING
        else:

            result = "You explored but found nothing."

    # -----------------------------
    # DO NOTHING
    # -----------------------------

    elif action == "do_nothing":

        result = "You stayed still and conserved resources."

    # -----------------------------
    # RANDOM ENVIRONMENT EVENTS
    # -----------------------------

    event_chance = random.randint(1, 100)

    if event_chance <= 10:

        state["health"] -= 10

        result += " A cold night reduced your health."

    elif event_chance <= 15:

        state["food_supply"] = max(0, state["food_supply"] - 1)

        result += " Some food spoiled."

    elif event_chance <= 20:

        state["water_supply"] = max(0, state["water_supply"] - 1)

        result += " Water was contaminated."

    # -----------------------------
    # SURVIVAL PENALTIES
    # -----------------------------

    if state["hunger"] > 80:

        state["health"] -= 15

    if state["thirst"] > 80:

        state["health"] -= 20

    if state["energy"] <= 0:

        state["health"] -= 15

    # -----------------------------
    # CLAMP VALUES
    # -----------------------------

    state["health"] = max(0, min(100, state["health"]))
    state["hunger"] = max(0, min(100, state["hunger"]))
    state["thirst"] = max(0, min(100, state["thirst"]))
    state["energy"] = max(0, min(100, state["energy"]))

    # -----------------------------
    # DEATH CHECK
    # -----------------------------

    if state["health"] <= 0:

        state["alive"] = False

    state["day"] += 1

    return state, result