'''
# we need to create 2 arrays for dict with same size
# 1st array is known as slots which stores key
# 2nd will store data/values of that keys
# we need to maintain 2 arrays for dict at a time
'''

class Dictionary:

    def __init__(self,size):
        self.size = size
        self.slots= [None]*self.size
        # stores key values
        self.data = [None]*self.size
        # stores data for that value

    # first we need to create hash function
    def hash_func(self,key):
        # abs() will turn negative into positive and hash() will convert string/tuple/char,etc into integer.
        return abs(hash(key))% self.size

    # this fun will insert key and value pair in dict
    def put(self, key, value):
        hash_val = self.hash_func(key)
        '''Now there are 2 possibilites:
           if that particular index is empty then store the value

           if that particular index is already taken
        '''
        if self.slots[hash_val] == None:
            self.slots[hash_val] = key
            self.data[hash_val] = value
        else:
            # if we need to update ie if key is already stored into the slot
            if self.slots[hash_val] == key:
                self.data[hash_val] = value
            # if we need to insert new data and we dont want to update it
            else:
                
                new_hash_val = self.rehash(hash_val)
                # we need to run a loop if another slot is also full and if we need to update data in particular key we need to check weather it is present and after loop we need to to update
                while self.slots[new_hash_val] != None and self.slots[new_hash_val] != key:
                    new_hash_val = self.rehash(new_hash_val)
                
                if self.slots[new_hash_val] == None:
                    self.slots[new_hash_val] = key
                    self.data[new_hash_val] = value
                else:
                    self.data[new_hash_val] = value

    # we need to recalulate the hash value
    def rehash(self, old_hash):
        return (old_hash+1)% self.size
    # to use D1['python'] = 64 as we get in dictionary in python
    def __setitem__(self, key, value):
        self.put(key, value)

    # to get items from dictionary
    def get(self,key):
        start_pos = self.hash_func(key)
        curr_pos = start_pos
        '''
        looping from start and 
        if we get key we will return the corresponding value
        if we dont get the key :
            if we come to the pos where we started and another condition is and if we get None while searchoing
            so that key is not inserted
        '''
        while self.slots[curr_pos] != None:
            if self.slots[curr_pos] == key:
                return self.data[curr_pos]
            curr_pos = self.rehash(curr_pos)

            if curr_pos == start_pos:
                return "Not Found - curr = start"
        return "Not Found - None found"
    # synax for getitem : D1[key] --> return same as get function
    def __getitem__(self,key):
        return self.get(key)
    
    # printing the dictionary
    def  __str__(self):
        result = ''
        for i in range(len(self.slots)):
            if self.slots[i] != None:     
                result = result + f'{self.slots[i]} : {self.data[i]}, '   
        return '{ ' + result[:-2] + ' }'
        

    
d1 = Dictionary(3)


# d1.put('python', 100)
# d1.put('java', 10)
d1['python'] = 100
d1['php'] = 23
d1['java'] =46 

# print(d1.get('c'))
print(d1)
# print(d1.slots)
# print(d1.data)
            

        

    