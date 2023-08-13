class InvestmentStrategy:
    def __init__(self, name, assets, risk_tolerance):
        self.name = name
        self.assets = assets
        self.risk_tolerance = risk_tolerance

    def execute(self):
        raise NotImplementedError("Subclasses must implement this method")


class MovingAverageStrategy(InvestmentStrategy):
    def __init__(self, name, assets, risk_tolerance, window):
        super().__init__(name, assets, risk_tolerance)
        self.window = window

    def execute(self):
        # Implement your moving average strategy here
        pass
