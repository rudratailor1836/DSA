class Node:
    def __init__(self, Value):
        self.data = Value
        self.next = None 


class Stack:
    def __init__(self):
        self.top = None
        self.n = 0
    
    # creating a function which tells us that stack is empty or not
    def isEmpty(self):
        return self.top == None
    
    # inserting an item on the top
    def push(self, value):
        # creating a new node
        new_node = Node(value)
        # new node next address will be set to self.top which will connect to stack
        new_node.next = self.top
        # reassigning the top with new_node
        self.top = new_node
        self.n += 1
    
    # traversal which will help to print the items
    def traverse(self):
        curr = self.top
        result = ''
        while curr != None:
            result = result + str(curr.data) 
            curr = curr.next
        return result
    
    # stAacks to be print with print statement
    def __str__(self):
        curr = self.top
        result = ''
        while curr != None:
            result = result + str(curr.data) + '->'
            curr = curr.next
        return result[:-2]
    
    # to get to top item value peek function is used
    def peek(self):
        if (self.isEmpty()):
            return 'Stack Empty'
        else:
            return self.top.data
        
    # we need to delete the top item and return its value
    def pop(self):
        if self.isEmpty == True:
            return 'Stack Empty'
        else:
            item = self.top
            self.top = self.top.next
            self.n -= 1
            return item.data
        
    def size(self):
        return self.n
    

            
        


        



# S = Stack()
# S.push(12)
# S.push(9)
# S.push(1)
# S.push(100)
# # print(S)
# # print(S.peek())
# x = S.pop()
# print(x)
# print(S)

