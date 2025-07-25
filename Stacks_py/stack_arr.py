class Stack:

    def __init__(self, size):
        self.size = size
        self.__stack = [None]* self.size
        self.top = -1

    def push(self, val):
        if self.top == self.size - 1:
            return "Overflow"
        else:
            self.top += 1
            self.__stack[self.top] = val

    def pop(self):
        if self.top == -1:
            return "Empty"
        else:
            data = self.__stack[self.top]
            self.top -= 1
            return data
    
    def traverse(self):
        for i in range(self.top + 1):
            print(self.__stack[i], end =' ')

s = Stack(3)

s.push(2)
s.push(3)
s.push(4)
print(s.pop())
s.traverse()
# print('\n')
# print(s.stack)