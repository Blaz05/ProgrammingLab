class MovingAverage:
    def __init__(self, window):
        self.window = window
    
    def compute(self, lista):
        if not type(lista) == list:
            raise ExamException("L'input fornito non è una lista.")
        if not len(lista) >= 2:
            raise ExamException("Fornire una lista con almeno due elementi, per calcolare la media mobile")
        mobile = []
        prev_element = None
        try:
            for element in lista:
                element = float(element)
                if(prev_element != None):
                    mobile.append((prev_element+element)/2)
                prev_element = element
        except:
            raise ExamException("Fornire elementi validi")
        return mobile

class ExamException(Exception):
    pass

moving_average = MovingAverage(2)
result = moving_average.compute([2,4,8,16]) 
print(result)
