class MyQueue:
    def __init__(self):
        
        self.q = []
    def push(self, x):
         
         return self.q.append(x)
         
     
    def pop(self): 
         
         if not self.q:
             return -1
         return self.q.pop(0)

 