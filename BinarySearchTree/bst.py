class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    
    def add_child(self, data):
        if data == self.data:
            return
        
        if data < self.data:
            # add into left subtree
            if self.left:
                self.left.add_child(data)
            else:
                self.left = TreeNode(data)
        else:
            # add into right subtree
            if self.right:
                self.right.add_child(data)
            else:
                self.right = TreeNode(data)

    def InOrderTraversal(self):
        elements = []
        # visit left tree
        if self.left:
            elements += self.left.InOrderTraversal()
        
        # visit base Node
        elements.append(self.data)

        # visit right subtree
        if self.right:
            elements += self.right.InOrderTraversal()

        return elements
    
    def search(self,item):
        if self.data == item:
            return True
        if item < self.data:
            if self.left:
                return self.left.search(item)
            else:
                return False
        if item > self.data:
            if self.right:
                return self.right.search(item)
            else:
                return False
            
    def find_min(self):
        if self.left:
            return self.left.find_min()
        else:
            return self.data
        
    def find_max(self):
        if self.right:
            return self.right.find_max()
        else:
            return self.data
    
    def sum(self):
        result = self.data
        if self.left:   
            result += self.left.sum()
        if self.right:
            result += self.right.sum()
        
        return result

    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)        
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left

            max_val = self.left.find_max()
            self.data = max_val
            self.left = self.right.left(max_val)
    
        return self

def build_tree(list):
    root = TreeNode(list[0]) 

    for i in range(1, len(list)):
        root.add_child(list[i])
    return root


list = [54,65,27,3,77,6,41,27,0,2,1,4,3,886,66,12,-12,-32,-55,22,29,28,5,63,44,51,21,34,36]

tree = build_tree(list)
print(tree.InOrderTraversal())
tree.delete(886)
print(tree.InOrderTraversal())