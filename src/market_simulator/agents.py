class Agent:
    def __init__(self, agent_id, cash, holdings):
        # Raise errors if invalid inputs
        if cash < 0:
            raise ValueError("cash must be non-negative")
        if holdings < 0 :
            raise ValueError("holdings must be non-negative")
        
        self.cash = float(cash)
        self.holdings = float(holdings)
        self.agent_id = agent_id

        self.order_history = []
        self.trade_history = []
        self.wealth_history = []
    
    def decide_order(self, market):
        ...
    
    def apply_trade(self, price, quantity):
        ...
    
    def wealth(self, price):
        ....

class FundamentalTrader():
    ...

class MomentumTrader():
    ...
