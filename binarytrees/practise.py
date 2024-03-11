class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return
        if data < self.data:
            if self.left:
                return self.left.add_child(data)
            else:
                self.left = BinarySearchTree(data)
        else:
            if self.right:
                return self.right.add_child(data)
            else:
                self.right = BinarySearchTree(data)    

    def inorderTraversal(self):
        elements = []
        if self.left:
            elements += self.left.inorderTraversal()
        elements.append(self.data) 
        if self.right:
            elements += self.right.inorderTraversal()
        return elements       
    
    def search(self, val):
        if val == self.data:
            return True
        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False    

    def minimum(self):
        # infinity = float("inf")
        # minimum = min(infinity, self.data)
        # if self.left:
        #     return self.left.minimum()
        # return minimum
    
        if self.left is None:
            return self.data
        return self.left.minimum()
    
    def maximum(self):
        # infinity = float("-inf")
        # maximum = max(infinity, self.data)
        # if self.right:
        #     return self.right.maximum()
        # return maximum

        if self.right is None:
            return self.data
        return self.right.maximum()
    
    def findSum(self):
        # s = 0
        # s += self.data
        # if self.left:
        #     s += self.left.findSum()
        # if self.right:
        #     s += self.right.findSum()    
        # return s    

        leftSum = self.left.findSum() if self.left else 0
        rightSum = self.right.findSum() if self.right else 0
        return self.data + leftSum + rightSum
    
    def preOrdertraversal(self):
        elements = []
        elements.append(self.data)
        if self.left:
            elements += self.left.preOrdertraversal()
        if self.right:
            elements += self.right.preOrdertraversal()
        return elements        
    
    def postOrdertraversal(self):
        elements = []
        if self.left:
            elements += self.left.postOrdertraversal()
        if self.right:
            elements += self.right.postOrdertraversal()    
        elements.append(self.data)
        return elements

    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        if val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left

            # min_value = self.right.minimum()
            # self.data = min_value 
            # self.right = self.right.delete(min_value)

            max_value = self.left.maximum()
            self.data = max_value
            self.left = self.left.delete(max_value)

        return self                   

            
def BuildTree(elements):
    root = BinarySearchTree(elements[0])
    for i in range(1, len(elements)):
        root.add_child(elements[i])
    return root

if __name__ == "__main__":
    elements = [17, 4, 1, 20, 9, 23, 18, 34]
    tree = BuildTree(elements)    
    tree.delete(20)

    print(tree.inorderTraversal())
    print(tree.search(4))
    print(tree.minimum())
    print(tree.maximum())
    print(tree.findSum())
    print(tree.preOrdertraversal())
    print(tree.postOrdertraversal())
    

        
