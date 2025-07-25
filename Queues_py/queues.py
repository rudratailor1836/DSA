class Node:
    def __init__(self, item):
        self.data = item
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.n = 0


    def enqueue(self, val):
        new_node = Node(val)

        if self.front == None:
            self.front = new_node
            self.rear = self.front
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.n += 1
        
    def dequeue(self):
        if self.front == None:
            return 'Empty'
        else:
            item = self.front.data
            self.front = self.front.next
            self.n -= 1
            return item
        
    def traverse(self):
        temp = self.front
        while temp != None:
            print(temp.data)
            temp = temp.next

    def __str__(self):
        curr = self.front
        res = '' 
        while curr != None:
            res = res + str(curr.data) + '->'
            curr = curr.next
        return res[:-2]
    
    def isEmpty(self):
        return self.front == None
    
    def __len__(self):
        return self.n
    
    def front_item(self):
        if self.front == None:
            return 'Empty'
        else:
    
            return self.front.data
    def rear_item(self):
        if self.front == None:
            return 'Empty'
        else:
            return self.rear.data


q = Queue()

print(q.isEmpty())


q.enqueue(1)
q.enqueue(3)
q.enqueue(23)
q.enqueue('str')

print(q)
print(len(q))

print(q.isEmpty())
# print(q.dequeue())
print(q.front_item())
print(q.rear_item())