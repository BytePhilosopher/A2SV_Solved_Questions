# dequeue
# enqueue


class Queue:
    def __init__(self) -> None:
        self.q = []
        #
        #

    def dequeue(self):
        self.q.pop(0)
      

    def enqueue(self,val):
       self.q.append(val)
obj=Queue()
obj.enqueue(10)
print(obj.q)