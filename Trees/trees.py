class tree:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None
    
    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_lvl(self):
        level = 0
        p = self.parent
        while p:
            level+=1
            p = p.parent  
        return level
    
    def print_tree(self):
        space = " "* self.get_lvl()*2
        if self.parent == None:
            prefix = ''
        else:
            prefix = space + "|->"
        print(prefix + self.data)
        for child in self.children:
            child.print_tree()

def build_product_tree():
    root = tree("Electronics")

    laptop = tree("Laptops")
    

    laptop.add_child(tree("Mac"))
    laptop.add_child(tree("Thinkpad"))

    cellphone = tree("Cellphone")
    cellphone.add_child(tree("Iphone"))
    cellphone.add_child(tree("Google Pixel"))
    
    tv = tree("TV")
    tv.add_child(tree("LG"))
    tv.add_child(tree("Samsung"))

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)

    root.print_tree()
    return root

if __name__ == '__main__':
    root = build_product_tree()
    