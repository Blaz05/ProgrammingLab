class ExamException(Exception):
    pass

class MovingAverage:
    def __init__(self, N):
        self.N = N
        try:
            self.N = int(N)
        except:
            raise ExamException('Inserire un numero intero.')
    
    def compute(self, lista):
        media_mobile = []
        try:
            float_list = []
            for el in lista:
                float_list.append(float(el))
            """Media mobile!!!"""
            for i in range(len(float_list) - self.N + 1):
                N_values = float_list[i:(i + self.N)]
                #print(N_values)
                average = sum(N_values) / self.N
                #print(average)
                media_mobile.append(average)
        except:
            raise ExamException("Fornire elementi numerici validi.")
        return media_mobile

moving_average = MovingAverage(2)
result = moving_average.compute([2,4,8,16]) 
print(result) # Deve stampare a schermo [3.0,6.0,12.0]