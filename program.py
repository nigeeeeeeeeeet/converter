class ConverterLogic:
    def __init__(self):
        self.rates = {
            'USD': 1.0,
            'EUR': 0.97,
            'UAH': 41.69,
            'GBP': 0.75,
            'BTC' : 0.0000098
        }

    def convert(self, amount, from_currency, to_currency):
        if from_currency == to_currency:
            return amount
        return amount * self.rates[to_currency] / self.rates[from_currency]