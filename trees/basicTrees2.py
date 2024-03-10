class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def getLevels(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent    
        return level    

    def print_tree(self, level):
        l = self.getLevels()
        spaces = ' ' * l * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.children and l < level:
            for child in self.children:
                child.print_tree(level)    

def buildtree():
    root = TreeNode("Global")

    gujarat = TreeNode("Gujarat")
    gujarat.add_child(TreeNode("Ahmedabad"))
    gujarat.add_child(TreeNode("Baroda"))
    karnataka = TreeNode("Karnataka")
    karnataka.add_child(TreeNode("Banglore"))
    karnataka.add_child(TreeNode("Mysore"))


    newjersey = TreeNode("New Jersey")
    newjersey.add_child(TreeNode("Princton"))
    newjersey.add_child(TreeNode("Trenton"))

    california = TreeNode("California")
    california.add_child(TreeNode("Santa Clara"))
    california.add_child(TreeNode("San Jose"))
    california.add_child(TreeNode("Irvine"))
    
    india = TreeNode("India")
    india.add_child(gujarat)
    india.add_child(karnataka)

    usa = TreeNode("USA")
    usa.add_child(newjersey)
    usa.add_child(california)
    
    root.add_child(india)
    root.add_child(usa)

    return root

if __name__ == "__main__":
    root = buildtree() 
    # root.print_tree(1)  
    root.print_tree(2)     
    # root.print_tree(3)     
