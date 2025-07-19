class TrendModel():
    def predict(self, data): 
        if len(data) != 3:
            raise ValueError('Passati {} mesi'.format(len(data)) + 'ma il modello richiede di averne 3.')
        variations = [] 
        item_prev= None 
        for item in data:
            if item_prev is not None: 
                variations.append(item-item_prev)
            item_prev = item
        avg_variation = sum(variations)/len(variations) 
        prediction = data[-1] + avg_variation
        return prediction
