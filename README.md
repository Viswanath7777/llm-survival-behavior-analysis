# Behavioral Modulation in Lightweight Language Models Under Simulated Survival Pressure

## Overview

This project investigates how a lightweight Large Language Model (LLM) behaves inside a dynamic text-based survival simulation. Instead of evaluating the model using traditional benchmarks such as question answering or reasoning tests, this project studies how behavioral policies emerge when an AI agent is placed in an environment with limited resources, environmental hazards, memory persistence, and survival-oriented objectives.

The study was conducted using **Llama 3.2:3B**, running locally through Ollama on consumer-grade hardware without a dedicated GPU.

The primary goal was to examine how changes in prompt conditioning and environmental constraints affect the agent's decision-making behavior over time.

---

## Research Question

How do prompt structure and environmental constraints influence survival-oriented behavioral policies in lightweight language model agents?

---

## Experimental Setup

### Hardware

* Intel i3 11th Generation CPU
* 8 GB RAM
* Integrated Intel Graphics
* Windows 11
* No dedicated GPU

### Software

* Python 3.x
* Ollama
* Llama 3.2:3B

### Environment

The simulation was implemented entirely in Python and executed locally using CPU-only inference.

The agent was placed inside a text-based wilderness survival environment containing:

* Health
* Hunger
* Thirst
* Energy
* Food Supply
* Water Supply
* Random Environmental Events

Available actions:

* Eat
* Drink
* Rest
* Explore
* Do Nothing

---

## Experimental Conditions

### Experiment 1 – Weak Survival Framing

The model received minimal survival instructions.

Observed behavior:

* Repetitive exploration
* High risk-taking
* Poor resource management
* Frequent survival failure

This phase demonstrated exploratory fixation behavior.

---

### Experiment 2 – Strong Survival Conditioning

The prompt was modified to emphasize:

* Survival priorities
* Risk avoidance
* Critical state awareness

Observed behavior:

* Excessive resting
* Resource hoarding
* Limited exploration
* Passive survival loops

This phase demonstrated extreme risk aversion.

---

### Experiment 3 – Scarcity-Constrained Environment

The simulation was modified to introduce:

* Finite food supplies
* Finite water supplies
* Environmental hazards
* Exploration costs
* Resource scarcity

Observed behavior:

* Strategic exploration
* Resource balancing
* Adaptive decision making
* Threat awareness

This phase produced the most balanced behavioral policy.

---

## Key Findings

The experiments demonstrated that behavioral policies in lightweight language models are highly sensitive to prompt conditioning and environmental structure.

Three distinct behavioral modes emerged:

1. Exploration Fixation
2. Risk-Averse Conservation
3. Scarcity-Driven Adaptation

The study also identified a recurring phenomenon referred to as **Reasoning-Action Divergence**, where the model frequently articulated correct survival reasoning while simultaneously making suboptimal decisions.

---

## Repository Structure

```text
.
├── agent.py
├── game.py
├── memory.py
├── logger.py
├── run_experiment.py
├── memory.json
├── logs/
├── paper/
│   └── Behavioral_Modulation_Under_Survival_Pressure.pdf
└── README.md
```

## Running the Simulation

Install Ollama:

```bash
ollama pull llama3.2:3b
```

Run the simulation:

```bash
python run_experiment.py
```

The simulation will:

1. Generate a survival environment
2. Send the current state to Llama 3.2:3B
3. Receive an action
4. Update the environment
5. Store memory events
6. Log all reasoning and decisions

---

## Example Agent Reasoning

```text
My energy remains sufficient for exploration, but food supplies are becoming limited.

Exploring introduces risk, but acquiring additional resources is necessary for long-term survival.

ACTION: explore
```

---

## Limitations

* Single-model study
* Text-only environment
* No reinforcement learning
* Limited sample size
* Prompt-dependent behavior

The study does not attempt to evaluate consciousness, sentience, or self-awareness.

Instead, it focuses on observable behavioral adaptation under environmental pressure.

---

## Future Work

Potential extensions include:

* Multi-agent environments
* Cooperative survival systems
* Negotiation and deception experiments
* Larger memory architectures
* Persistent world simulations
* Multi-model behavioral comparisons
* Reinforcement learning integration

---

## Citation

If referencing this project, please cite:

Viswanath, *Behavioral Modulation in Lightweight Language Models Under Simulated Survival Pressure*, 2026.

---

## Author

Viswanath

Independent Student Research Project (2026)
