# Design Document – Agent-Based Financial Market Simulator

## Project Overview

This project aims to build an agent-based financial market simulator to study how simple trading behaviours can generate complex market dynamics.

Rather than assuming perfectly rational investors, the simulator models a heterogeneous population of traders who interact by buying and selling assets in a simulated market. Prices emerge from these interactions over time.

The purpose of the simulator is not to predict real financial markets directly, but to provide a flexible research framework for exploring questions about market behaviour, trader interaction, volatility, mispricing, bubbles, crashes, and wealth outcomes.

## Research Scope

The simulator is intended to support multiple research questions.

Examples include:

- How does the proportion of different trader types affect market behaviour?
- Does increasing the proportion of momentum traders increase volatility?
- Do fundamental traders stabilise prices?
- Which strategies generate the greatest long-term wealth?
- Can simple behavioural rules produce bubbles and crashes?
- Under what assumptions does the simulator reproduce stylised facts of financial markets?

Different research questions may require different assumptions, parameter settings, market mechanisms, and evaluation metrics. For this reason, the simulator should be designed as a reusable framework rather than as a single-purpose experiment.

## Design Goals

The simulator should:

- support multiple trader types
- allow different market assumptions to be tested
- produce reproducible results across random seeds
- record price, return, and wealth histories
- generate outputs suitable for statistical analysis
- be simple enough to extend over time

The first version should prioritise clarity and modularity over realism.

## Baseline Model Assumptions

The initial version of the simulator will use a deliberately simple baseline model.

Baseline assumptions:

- one tradable asset
- one market
- discrete time steps
- all agents observe the same market information
- fractional shares are allowed
- all orders execute immediately
- no transaction costs
- no bid-ask spread
- no explicit order book
- external news shocks may affect prices
- a fixed or externally specified fundamental value may be used

These assumptions define the baseline model only. Later experiments may relax them.

## Trader Types

The baseline simulator may include several trader types.

### Fundamental Traders

Fundamental traders compare the current market price with an estimated fundamental value.

Typical behaviour:

- buy when the asset appears undervalued
- sell when the asset appears overvalued

### Momentum Traders

Momentum traders respond to recent price trends.

Typical behaviour:

- buy after prices rise
- sell after prices fall

### Mean Reversion Traders

Mean reversion traders assume prices tend to return towards a recent average or reference level.

Typical behaviour:

- buy when price is below the moving average
- sell when price is above the moving average

### Noise Traders

Noise traders make random or weakly structured trading decisions.

Purpose:

- introduce randomness
- increase market activity
- reduce determinism in the simulation

Additional trader types may be added in future versions.

## Core Components

The simulator consists of several core objects.

### Agent

An agent represents an individual trader.

Responsibilities:

- observe market information
- generate trading decisions
- track cash and holdings
- update wealth over time

### Market

The market represents the trading environment in which agents interact.

Responsibilities:

- store the current price
- receive aggregate order flow
- update prices
- record market history

### Order

An order represents a buy or sell request submitted by an agent.

In the baseline model, an order may be represented simply as a signed quantity:

- positive values represent buy orders
- negative values represent sell orders

More detailed order objects may be introduced later if the market mechanism becomes more realistic.

### Simulation

The simulation controls the overall experiment run.

Responsibilities:

- initialise the market
- initialise agents
- advance the simulation through time
- record outputs
- export results for analysis

## Simulation Flow

Each timestep follows the same general sequence:

1. Observe Market
2. Generate Trading Signals
3. Submit Orders
4. Aggregate Orders
5. Update Market Price
6. Update Cash and Holdings
7. Record Statistics
8. Repeat