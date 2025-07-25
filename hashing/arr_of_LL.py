'''
Here We have only one array in which we will store LinkedList as an item

'''
class Node:
    def __init__(self, key,value):
        self.key = key
        self.data = value
        self.next = None


class LinkedList:
    
    def __init__(self):
        # Creating Empty LinkedList
        self.head = None
        self.n = 0

    # Len function of LinkedList
    def __len__(self):
        return self.n
        

    # traversing/Printing Linkedlist
    def __str__(self):
        #  assign a temperory variable as the current head of the linkedlist
        curr = self.head
        result = ''
        while curr != None:
            result = result + str(curr.key) + ' : ' + str(curr.data) + '->'
            curr = curr.next
        return result[:-2]
    
    # def traverse(self):
    #     curr = self.head
    #     result = ''
    #     while curr != None:

    #         curr = curr.next
    #     return result  

    # append - insert from the tail
    def add(self,key,value):
        # create a new Node
        new_node = Node(key,value)
        # we need to travrse till the last and add new node
        if self.head != None:
            curr = self.head
            while curr.next != None:
                curr = curr.next
            # now you are on the last node so in its address we will store the new node.
            curr.next = new_node
        else:
            self.head = new_node
        # increment of n
        self.n += 1
    



    
    # delete from head:
    def delete_head(self):
        if self.head == None:
            print("LinkedList is Empty.")
        else:
            item = self.head.data
            self.head = self.head.next
            self.n -= 1
            return item
    
    # delete from head:
    def delete_head(self):
        if self.head == None:
            print("LinkedList is Empty.")
        else:
            item = self.head.data
            self.head = self.head.next
            self.n -= 1
            return item

        
    def remove(self, key):
        # traverse to the item which comes before the item we need to remove
        curr = self.head
        # if LL is empty
        if curr == None:
            print("Empty LL")
        # if list have only 1 element.
        elif curr.next == None:
            item = self.delete_head()
            self.n -= 1
            return item
        else:
            while curr.next != None:
                if curr.next.key == key:
                    break                 
                curr = curr.next
            if curr.next == None:
                # Item not found in LL
                print("Item not Found")
            else:
                item = curr.next.data
                curr.next = curr.next.next        
                self.n -= 1
                return item
                
    # searching the index from value
    def search(self, key):
        curr = self.head
        # getting a position element to count the indices
        pos = 0
        # traversing to the searching value by loop
        while curr!= None:
            if curr.key == key:
                return pos
            curr = curr.next
            pos += 1
        # if item is not in LL
        return -1
    
    def get_node_index(self,index):
        curr = self.head
        count= 0
        while curr != None:
            if count == index:
                return curr
            curr = curr.next
            count+=1
      
 

class Dictionary:

    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0

        self.buckets = self.make_arr(self.capacity)

    
    def make_arr(self, capacity):
        L = []
        for i in range(capacity):
            L.append(LinkedList())
        return L 
    
    def HashVal(self, key):
        return abs(hash(key)) % self.capacity
    
    def put(self,key,value):
        # first we need to calculate hash value
        bucket_index = self.HashVal(key)
        node_index = self.get_node_index(bucket_index, key)

        if node_index == -1:
            # inserting case
            self.buckets[bucket_index].add(key,value)
            self.size += 1
            # now we need to check load factor ie lambda for rehashing
            if self.size/self.capacity >= 2:
                self.rehash()
        else:
            # update
            node = self.buckets[bucket_index].get_node_index(node_index)
            node.data = value

    def __setitem__(self, key, value):
        self.put(key, value)
    
    def rehash(self):
        self.capacity = self.capacity * 2
        # this will store information of the array which was created before rehashing
        old_buckets = self.buckets
        self.size = 0
        self.buckets = self.make_arr(self.capacity)
        
        # we need to run loop in a loop to fetch item and put it in another array
        for i  in old_buckets:
            for j in range(len(i)):
                node = i.get_node_index(j)
                key_item = node.key
                value_item = node.data
                self.put(key_item,value_item)
                
    def get_node_index(self,bucket_index, key):
        node_index = self.buckets[bucket_index].search(key)
        return node_index
    
    def get(self, key):
        # step 1 :- we need to decide where it would be set 
        bucket_index = self.HashVal(key)
        res = self.buckets[bucket_index].search(key)

        if res == -1:
            return "Not Found"
        else:
            node = self.buckets[bucket_index].get_node_index(res)
            return node.data
    
    def __getitem__(self, key):
        return self.get(key)
    # deletion of Node
    def __delitem__(self,key):
        bucket_index = self.HashVal(key)
        self.buckets[bucket_index].remove(key)
        self.size -= 1

# we need to traverse or print the whole dictionary
    def __str__(self):
        for i in self.buckets:
            print(i)
        
        return ''
    
    def __len__(self):
        return self.size

        
# L = LinkedList()

# L.add(4,5)
# L.add(2,3)

# print(L)
D1 =Dictionary(2)

D1.put('Py', 10)
D1.put('java', 100)
D1.put('php', 1000)
D1.put('ruby', 200)
D1.put('mac', 2100)

# del D1['php']

# print(D1['php'])
print(D1)
print(len(D1))