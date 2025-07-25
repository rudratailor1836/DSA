import ctypes


class MyList:

    def __init__(self):
        self.size = 1
        self.n = 0
        # self.n is no. of items and self.size is size of array
        # Create a C type array with size = self.size
        self.A = self.__make_array(self.size)

# creating a list
    def __make_array(self, capacity):
        # creates a Ctype array with size capacity which is static and referential array
        return (capacity*ctypes.py_object)()
    
# len fuction of List
    def __len__(self):
        return self.n

# print function of List 
    def __str__(self):
        result = ''
        for i in range(self.n):
            result = result + str(self.A[i]) + ','
        return '[' + result[:-1] + ']'

# to delete the item at an given index 
    def __delitem__(self, pos):
        if pos < self.n and pos >= 0:
            for i in range(pos, self.n-1):
                self.A[i] = self.A[i+1]       
            self.n = self.n - 1

# function to expand the size of array  
    def __resize(self,new_capacity):
        # create a new array with new capacity
        B = self.__make_array(new_capacity)
        self.size = new_capacity
        # now we need to copy the content of A to B
        for i in range(self.n):
            B[i] = self.A[i]
            # reassign A
            self.A = B

# function to append/ add item at last
    def append(self,item):
        if self.n == self.size:
            # resize
            self.__resize(self.size + 8)

        self.A[self.n] = item
        self.n = self.n + 1

# Indexing/ getting an item from its index
    def __getitem__(self,index):
        if index < self.n and index >= 0:
            return self.A[index]
        else:
            print('IndexError : Index not found')

# popping method/ removed from the last and return its value
    def pop(self):
        popped_item = self.A[self.n - 1]
        if self.n == 0:
            print("Empty List")
        else:
            self.n = self.n - 1
            return popped_item
    
# to clear all item of the list
    def clear(self):
        self.n = 0
        self.size = 1

# to create a find function, wwhich will give the index from item
    def find(self, item):
        for i in range(self.n):
            if self.A[i] == item:
                return i
        return 'Item Not Found'
        
# to insert the item at your desire index
    def insert(self, item, index):
        # check if there is a space in array and if not we need to call resize function
        # if there is a space we need to shift every elemnt till the given index + 1 from right which is negative loop
        if self.n == self.size:
            # resize
            self.__resize(self.size + 8)
        if index > self.n:
            print("Index Out Of Range")
        else:
            for i in range(self.n, index, -1):
                self.A[i] = self.A[i - 1]
            # setting that item at the given index
            self.A[index] = item
            self.n += 1

# remove function : item is given not index
    def remove(self, item):
        pos = self.find(item)
        if type(pos) == int:
            self.__delitem__(pos)
        else:
            return pos


L = MyList()
L.append('hello')
L.append(5)
L.append('A')
L.append(12.34)
L.insert('Hii', 123)
print(L)