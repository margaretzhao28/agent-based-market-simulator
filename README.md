# Agent-Based Financial Market Simulator

Agent-based simulation of financial markets exploring how simple trading behaviours can generate complex market dynamics such as bubbles, crashes, volatility clustering and mispricing.

## Overview

Financial markets are complex systems in which thousands of individual participants interact through buying and selling decisions. Rather than assuming perfectly rational investors, this project models a heterogeneous population of traders with different strategies and investigates how their interactions influence market behaviour.

The project aims to answer questions such as:

- How do different trader populations affect market volatility?
- Can simple behavioural rules generate bubbles and crashes?
- How does the proportion of momentum traders influence market stability?
- Which trading strategies are most profitable under different market conditions?

---

## Project Roadmap

- [x] Project setup
- [ ] Baseline market simulation
- [ ] Multiple trader types
- [ ] Experimental framework
- [ ] Wealth analysis
- [ ] Strategy evolution
- [ ] Market maker
- [ ] Limit order book
- [ ] Real market comparison

---

## Features

Current features:

- Fundamental traders
- Momentum traders
- Mean reversion traders
- Noise traders
- Market price simulation
- Wealth tracking
- Performance metrics
- Experimental framework

Planned features:

- Limit order book
- Market maker
- Transaction costs
- Adaptive agents
- Strategy evolution
- News events
- Network interactions
- Comparison with real market data

---

## Project Structure

```text
agent-based-market-simulator/

src/
    agents.py
    market.py
    simulation.py
    metrics.py

experiments/
    experiment_1.py

notebooks/

data/

figures/

tests/
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/yourusername/agent-based-market-simulator.git
```

Create a virtual environment

```bash
python3 -m venv .venv
```

Activate it

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Current Research Question

> How does the proportion of momentum traders affect market volatility, price stability and wealth distribution?

The first experiment compares markets with different trader compositions while measuring:

- volatility
- drawdown
- return distribution
- mispricing
- trader wealth

---

## Future Work

- Implement a realistic order book
- Introduce liquidity constraints
- Model transaction costs
- Add adaptive learning agents
- Compare simulated returns with real financial markets
- Investigate volatility clustering and heavy-tailed return distributions

---

## Technologies

- Python
- NumPy
- Pandas
- Matplotlib
- SciPy (planned)

---

## Author

Margaret Zhao

Bachelor of Science (Advanced) and Master of Mathematical Sciences  
University of Sydney

Interested in quantitative trading, complex systems and computational finance. 