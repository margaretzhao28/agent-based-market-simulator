class Market:
    """
    Simulated market with a single asset and a simple price update rule.

    Parameters
    ----------
    initial_price : float
        Starting market price of the asset.
    fundamental_value : float
        Reference value used by fundamental traders.
    impact_strength : float
        Controls how strongly net order flow moves the price.
    shock_std : float
        Standard deviation of the random news shock added each timestep.
    rng :
        Random number generator used for reproducible randomness.
    """

    def __init__(self, initial_price, fundamental_value, impact_strength, shock_std, rng):
        # Check if initial price is negative or zero
        if initial_price <= 0:
            raise ValueError("initial_price must be positive")
        
        self.price = initial_price
        self.fundamental_value = fundamental_value
        self.impact_strength = impact_strength
        self.shock_std = shock_std
        self.rng = rng

        self.price_history = [initial_price]
        self.return_history = []
        self.net_order_history = []
    
    def get_price(self):
        return self.price
    
    def get_fundamental_value(self):
        return self.fundamental_value

    # Update price based on actions taken by traders
    def update_price(self, net_order, num_agents):
        # Raise error if invalid num_agents
        if num_agents <= 0:
            raise ValueError("num_agents must be positive")
                             
        # Draw random market shock from a normal distribution with mean 0
        shock = self.rng.normal(0, self.shock_std)

        # Average buying / selling pressure
        trading_pressure = net_order / num_agents

        # Total proportional price change from trading pressure plus randomness
        price_change = (self.impact_strength * trading_pressure) + shock

    
        old_price = self.price
        # Ensure price is not zero or negative
        self.price = max(0.01, old_price * (1 + price_change))
        
        # Calculate price change relative to old price 
        simple_return = (self.price - old_price) / old_price

        # Store return, aggregate net order and updated market price 
        self.return_history.append(simple_return)
        self.net_order_history.append(net_order)
        self.price_history.append(self.price)
    
    def record_state(self):
        # Return state
        return {
            "price": self.price,
            "fundamental_value": self.fundamental_value,
            "price_history": self.price_history.copy(),
            "return_history": self.return_history.copy(),
            "net_order_history": self.net_order_history.copy(),
        }
