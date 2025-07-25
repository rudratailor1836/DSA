class Node:

    def __init__(self):
        self.children = dict()
        self.end_of_word = False


class Trie:
    def __init__(self):
        self.root = Node()
    
    def insert(self, word):
        curr = self.root
        for c in word:
            if c in curr.children:
                curr.children[c] = Node()
            curr = curr.children[c]
        curr.end_of_word = True



    def search(self, word):
        curr = self.root

        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        
        return curr.end_of_word

    def delete(self, word):
        self._delete(self.root, word, 0)

    def has_prefix(self, prefix):
        curr = self.root

        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        
        return True


    def starts_with(self, prefix):
        pass

    def lists_word(self):
        pass
    
    def _delete(self, curr, word, index):
        if index == len(word):
            if not curr.end_of_word:
                return False
            curr.end_of_word = False

            return len(curr.children) == 0
        c = word[index]
        node = curr.children.get(c)

        if node is None:
            return False
        
        delete_curr_node = self._delete(node, word, index+1)
        if delete_curr_node:
            del curr.children[c]
            return len(curr.children) == 0 and not curr.end_of_word
        return
         

