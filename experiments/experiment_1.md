# Experiment Document – Experiment 1

## Experiment Title

Effect of Momentum Trader Proportion on Market Volatility

## Research Question

This experiment asks:

> Does increasing the proportion of momentum traders increase market volatility and market instability?

This is the first baseline experiment for the simulator. It focuses on how trader composition affects aggregate market behaviour, with particular attention to volatility, mispricing, drawdowns, and wealth outcomes.

## Motivation

Momentum trading amplifies recent price movements by encouraging traders to buy after price increases and sell after price decreases. In real and simulated markets, this kind of positive feedback may contribute to excess volatility, trend persistence, bubbles, and crashes.

This experiment is designed to test whether a higher proportion of momentum traders makes the simulated market less stable under otherwise similar conditions.

## Hypothesis

The main hypothesis is:

- increasing the proportion of momentum traders will increase market volatility

Secondary hypotheses include:

- higher momentum participation will increase maximum drawdown
- higher momentum participation will increase average mispricing
- higher momentum participation may produce stronger price trends and larger deviations from fundamental value
- momentum traders may perform well during sustained trends but not necessarily across all market conditions

## Experimental Setup

This experiment uses the baseline simulator described in `design.md`.

The purpose is to vary trader composition while keeping the rest of the market structure fixed.

## Baseline Assumptions

The experiment assumes:

- one tradable asset
- one market
- discrete time steps
- all agents observe the same market information
- fractional shares are allowed
- all orders execute immediately
- no transaction costs
- no bid-ask spread
- no explicit order book
- a simple price update rule based on aggregate order pressure
- a fixed or externally specified fundamental value
- random news shocks may be included

These assumptions are intentionally simple so that the effect of trader composition can be studied more clearly.

## Trader Types Included

The experiment may include the following trader types:

- fundamental traders
- momentum traders
- mean reversion traders
- noise traders

Their behavioural rules should remain fixed across scenarios. The main change across scenarios is the proportion of momentum traders in the market.

## Independent Variable

The independent variable is:

- proportion of momentum traders in the total trader population

This is the main factor being changed between experimental runs.

## Controlled Variables

The following should remain fixed across scenarios unless explicitly stated otherwise:

- total number of agents
- initial asset price
- fundamental value
- initial cash endowment
- initial asset holdings
- trading intensity or order size rules
- price update mechanism
- number of timesteps
- random shock distribution
- non-momentum trader behaviour rules

Keeping these constant helps isolate the effect of momentum trader proportion.

## Experimental Scenarios

Four trader-composition scenarios will be compared:

### Scenario 1: Low Momentum

A market with a relatively small proportion of momentum traders.

### Scenario 2: Balanced

A market with a moderate or balanced proportion of momentum traders relative to other trader types.

### Scenario 3: High Momentum

A market with a large proportion of momentum traders.

### Scenario 4: Extreme Momentum

A market dominated by momentum traders.

Exact percentages can be defined in code or in a parameter table once the implementation is finalised.

## Parameter Choices

The experiment should specify values for:

- number of agents
- number of timesteps
- initial market price
- fundamental value
- size of random news shocks
- lookback window for momentum signals
- lookback window for mean reversion signals
- order size or position sizing rule
- number of simulation repetitions per scenario
- random seed set

If these values are not yet final, they can be added later as the implementation becomes more concrete.

## Simulation Procedure

For each trader-composition scenario:

1. initialise the market with the same baseline settings
2. initialise the agent population with the chosen trader proportions
3. run the simulation for a fixed number of timesteps
4. record price, returns, holdings, and wealth histories
5. repeat the simulation across multiple random seeds
6. aggregate results across runs
7. compare outcomes across scenarios

Using multiple seeds is important because random shocks and noise traders may produce substantial variation across single runs.


## Data to Record

The experiment should record:

- price series
- return series
- fundamental value series if applicable
- mispricing over time
- agent cash balances
- agent holdings
- agent wealth over time
- aggregate buy and sell pressure
- summary statistics for each run

These outputs will support both descriptive analysis and later validation work.

## Evaluation Metrics

The main metrics for comparison are:

- volatility
- maximum drawdown
- average mispricing
- return distribution
- wealth distribution by trader type

Additional metrics may include:

- skewness of returns
- kurtosis of returns
- frequency of extreme price moves
- duration of price trends
- final wealth ranking of trader types

## Analysis Plan

The results will be analysed by comparing metric distributions across the four scenarios.

Key comparisons include:

- whether volatility rises as momentum trader share increases
- whether drawdowns become deeper in higher-momentum markets
- whether prices deviate further from fundamental value
- whether certain trader types systematically accumulate more wealth
- whether return behaviour becomes more unstable or heavy-tailed

Plots may include:

- price paths
- return histograms
- volatility comparisons across scenarios
- drawdown plots
- wealth distribution plots
- mispricing over time

## Validation Strategy

This experiment should be checked for both internal consistency and economic plausibility.

Internal validation:

- ensure prices remain finite and non-negative if that is a model constraint
- ensure wealth updates are calculated correctly
- ensure agent holdings and cash balances evolve consistently with trades
- ensure scenario definitions differ only in intended trader composition
- ensure repeated runs with the same seed are reproducible

Behavioural validation:

- confirm that momentum-heavy markets do not behave identically to low-momentum markets
- check whether stronger trend-following produces more persistent price movements
- examine whether mispricing and volatility respond in economically sensible ways

External validation can come later by comparing stylised properties of simulated returns with real market behaviour.

## Expected Outcomes

Expected patterns include:

- low-momentum markets should be relatively more stable
- balanced markets may show moderate trend behaviour without severe instability
- high-momentum markets may generate stronger price swings
- extreme-momentum markets may be most prone to bubbles, crashes, or amplified trends

These are hypotheses rather than guaranteed outcomes. The purpose of the experiment is to test them.

## Limitations

This experiment has several limitations:

- the market mechanism is intentionally simplified
- there is no realistic order book or market microstructure
- agents may use very stylised trading rules
- results may depend strongly on parameter choices
- conclusions will apply to the baseline simulator, not directly to real financial markets

These limitations should be acknowledged when interpreting results.

## Relationship to the Broader Project

This experiment is the first test case for the simulator framework.

Its role is to:

- evaluate whether the simulator produces meaningful differences across trader compositions
- establish a baseline workflow for running experiments
- identify useful metrics for future studies
- provide a foundation for later experiments with richer assumptions

Later experiments may change the pricing mechanism, introduce market frictions, vary information structure, or test different trader behaviours.

## Success Criteria

This experiment will be considered successful if it:

- runs reproducibly across multiple seeds
- produces interpretable differences across trader-composition scenarios
- records the intended output data
- allows comparison of volatility, mispricing, drawdowns, and wealth outcomes
- helps assess whether momentum participation contributes to market instability