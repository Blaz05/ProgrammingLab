class TrendModel():
    def __init__(self, window=3): 
        self.window = window
    def predict(self, data):
        if len(data) != self.window:
            raise ValueError('Passati {} mesi, ma il modello richiede di averne {}.'.format(len(data), self.window))
        variations = [] 
        item_prev = None 
        for item in data:
            if item_prev is not None: 
                variations.append(item-item_prev)
            item_prev = item
        avg_variation = sum(variations)/len(variations) 
        prediction = data[-1] + avg_variation
        return prediction