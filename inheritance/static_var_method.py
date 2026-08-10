class CounterRun:
    counter=0
    @staticmethod
    def increment():
        CounterRun.counter+=1
        
    @staticmethod
    def decrement():
        CounterRun.counter-=1  
        

i=1
while i<6:
    CounterRun . increment()
    i+=1

k=1
while k<3:
    CounterRun.decrement()
    k+=1    
    
print(CounterRun.counter)    