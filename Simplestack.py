class Simplestack:
     def __init__(self, initial_value):
          "set up an empty stack (last in first out"
          self.values = []
          if initial_value != None:
               self.push(initial_value)

     def push(self, item):
          """insert item into stack at the top (next pop will 
           deliver this item """

          self.values.append(item)

     def pop(self):
          """deliver the top thing on the stack (the last thing
           that was pushed onto it"""

          retval = self.values[-1]
          del self.values[len(self.values)-1]
          return retval

     def top(self):
          "deliver the top thing on the stack without removing it"
          return self.values[-1]

     def peek(self):
          "synonym for top(), does the same thing"
          return self.top()

     def size(self):
          "tells how many things are in the stack"
          return len(self.values)

     def clear(self):
          "removes all things from the stack"
          self.values = []

     def empty(self):
          """returns True if there are 0 things in the stack,
           or returns False if there is 1 or more"""

          return len(self.values) == 0

     def __str__(self):
          "returns a string image of the stack for easy viewing"
          return str(self.values)
