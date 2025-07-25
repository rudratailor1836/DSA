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
            if c not in curr.children:
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
        # dfs algo
        words = []
        curr = self.root

        for c in prefix:
            if c not in curr.children:
                return words
            curr = curr.children[c]
        
        def _dfs(curr, path):
            if curr.end_of_word:
                words.append(''.join(path))
            
            for c,child_node in curr.children.items():
                _dfs(child_node, path + [c])
            
        _dfs(curr, list(prefix))
        return words

    def lists_word(self):
        words = []

        def _dfs(curr, path):
            if curr.end_of_word:
                words.append(''.join(path))
            
            for c,child_node in curr.children.items():
                _dfs(child_node, path + [c])
        
        _dfs(self.root, [])

        return words
    
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
        return False
    




if __name__ == '__main__':
    T = Trie()
    T.insert('hello')
    T.insert("henry")
    T.insert('rude')
    T.insert('jay')
    T.insert('minimum')
    T.insert('minimal')
    T.insert('minimalistic')

    print(T.lists_word())

    print(T.has_prefix('mi'))
    print(T.starts_with("he"))

    T.delete('jay')
    print(T.lists_word())

    print(T.search('rude'))


    
         

