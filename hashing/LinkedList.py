class Node:
    def __init__(self, value):
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
    
    
    # insert a node from head
    def head_insert(self, value):
        # creating new Node
        new_node = Node(value)
        # creating connection
        new_node.next = self.head
        # reassigning new head
        self.head = new_node
        self.n += 1

    # traversing/Printing Linkedlist
    def __str__(self):
        #  assign a temperory variable as the current head of the linkedlist
        curr = self.head
        # this will store what to print when function is called.
        result = ''
        # This Loop is used to fetch data from the Linkedlist
        while curr != None:
            # result will store now the data of the Linkedlist
            result = result + str(curr.data) + '->'
            # this is used to switch to the next variable and check the condition
            curr = curr.next
        # we need to slice the result bcoz it will also print the last arrow which is not needed
        return result[:-2]
    
    def traverse(self):
        curr = self.head
        result = ''
        while curr != None:
            result = result + str(curr.data)
            curr = curr.next
        return result  

    # append - insert from the tail
    def append(self,value):
        # create a new Node
        new_node = Node(value)
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
    
    # insert Node in middle
    def insert_after(self, after, value):
        # traverse to the no. after which we need to insert
        new_node = Node(value)
        # we need to set temperary value for loop to start 
        curr = self.head
        while curr != None:
            if curr.data == after:
                break
            curr = curr.next
        # Case 1 - If item is found.
        if curr != None:
            new_node.next = curr.next
            curr.next = new_node
            self.n += 1 
        # case 2 - If item is not in the list
        else:
            print('Item Not Found')
    
    # clearing the linkedlist
    def clear(self):
        self.head = None
        self.n = 0
    
    # delete from head:
    def delete_head(self):
        if self.head == None:
            print("LinkedList is Empty.")
        else:
            item = self.head.data
            self.head = self.head.next
            self.n -= 1
            return item

    # delete from tail/ pop operation
    def pop(self):
        # we need to traverse to last second element
        curr = self.head
        # LinkedList is Empty
        if self.head == None:
            print("Empty Linked List")
        # LinkedList has Only One element
        elif curr.next == None:
            item = self.delete_head()
            self.n -= 1 
            return item
        else:
            # curr.next.next represent second last node
            while curr.next.next != None:
                curr = curr.next
            # need to return the deleted element
            item = curr.next.data
        # need to set next element to none
            curr.next = None
            self.n -= 1
            return item
    
    def remove(self, value):
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
            # here we need to check that the item matches the curr.next ka data 
                if curr.next.data == value:
                    break                 
                curr = curr.next
            if curr.next == None:
                # Item not found in LL
                print("Item not Found")
            else:
                # item found in LL
                item = curr.next.data
                # reassingning address to delete the element and join the other one
                curr.next = curr.next.next        
                self.n -= 1
                return item
                
    # searching the index from value
    def search(self, value):
        curr = self.head
        # getting a position element to count the indices
        pos = 0
        # traversing to the searching value by loop
        while curr!= None:
            if curr.data == value:
                return pos
            curr = curr.next
            pos += 1
        # if item is not in LL
        return 'Item Not Found'
    
    # index position - getting value from index
    def __getitem__(self, index):
        curr = self.head
        pos = 0
        # traversing to the given index
        while curr != None:
            if pos == index:
                return curr.data
            curr = curr.next
            pos += 1
        # if index not found
        return "IndexError : Index Not found"

    #  deleting by index
    def __delitem__(self, index):
        curr = self.head 
        pos = 0
        # traversing to the index befor the given Index
        while curr.next != None:
            if pos + 1 == index:
                curr.next = curr.next.next
            curr =   curr.next
            pos += 1
        return "IndexError : Index Doesn't Exist"
    # prob 1 ; find maximum and replace it with a given value
    def replace_max(self, val):
        # iterrate/ traverse to the maximum value
        temp = self.head
        max = temp
        # looping to compare
        while temp != None:
            if temp.data > max.data:
                max = temp.data
            temp = temp.next
        max.data = val
    
    # replace function
    def replace(self, value_in_LL, replace_value):
        # need to traverse to the item
        curr = self.head
        while curr != None:
            if curr.data == value_in_LL:
                curr.data = replace_value
            curr = curr.next
    
    # max function
    def max(self):
        curr = self.head
        # traversing and iterratting to find the maxvalue
        max = curr.data
        while curr != None:
            if curr.data > max:
                max = curr.data
            curr = curr.next
        return max
    
    def min(self):
        curr = self.head
        # need to loop and check that value is less then the minimum value
        min = curr.data
        # traversing
        while curr != None:
            if curr.data < min:
                min = curr.data
            curr = curr.next
        return min
    
    # to check that value is presenbt or not
    def present(self, item):
        curr = self.head
        #To check the value is present we need to traverse till the end
        while curr != None:
            if curr.data == item:
                return True
            curr = curr.next
        return False
    
    # sum of all values in LL
    def sum(self):
        curr = self.head
        result = 0
        # need to traverse asnd add the value to result
        while curr != None:
            result = result + curr.data
            curr = curr.next
        return result
    
    # sum of odd indexes
    def sum_odd(self):
        curr = self.head
        counter = 0
        result = 0
        # traverseing and using if else statement we will add value of odd indices
        while curr != None:
            if counter%2 != 0:
                result = result + curr.data
            counter += 1
            curr = curr.next 
        return result
    
    # sum of even indices
    def sum_even(self):
        curr = self.head
        counter = 0
        result = 0
        # traverseing and using if else statement we will add value of odd indices
        while curr != None:
            if counter%2 == 0:
                result = result + curr.data
            counter += 1
            curr = curr.next 
        return result
    
    # don't create a new LL as it isw called inplace reverse
    def reverse(self):
        prev_node = None
        curr = self.head
        # traversing the LL
        while curr != None:
            next_node = curr.next
            curr.next = prev_node
            prev_node = curr
            curr = next_node
        self.head = prev_node
    
    # convert given LL in string where we need to replace '/' and '*' with space and if 2 // or ** or /* or */ we need to give space and convert the first letter into capital/uppercase of next word 
    def get_sentence(self):
        curr = self.head
        while curr != None:
            # here single / or* represent space and after that / * represent that we need to jump from that to its next and change that character into uppercase
            # we need to create nested if statement
            if curr.data == '/' or curr.data == '*':
                curr.data = ' '
                # this will give space
                if curr.next.data == '*' or curr.next.data == '/':
                    # now change the next node after 2nd symbol to uppercase
                    curr.next.next.data = curr.next.next.data.upper()
                    # to delete the second symbol as it wont give another space so set the below statement.
                    curr.next = curr.next.next
            curr = curr.next
        
            
L = LinkedList()

L.append(1)
L.head_insert(12)
L.head_insert(13)
L.head_insert(19)
L.append(17)
L.insert_after(12, 23)

print(L)
L.reverse()
print(L)


# sent = LinkedList()
# sent.append('T')
# sent.append('h')
# sent.append('e')
# sent.append('/')
# sent.append('*')
# sent.append('s')
# sent.append('k')
# sent.append('y')
# sent.append('*')
# sent.append('i')
# sent.append('s')
# sent.append('/')
# sent.append('/')
# sent.append('b')
# sent.append('l')
# sent.append('u')
# sent.append('e')

# print(sent.traverse())

# sent.get_sentence()
# print(sent.traverse())

