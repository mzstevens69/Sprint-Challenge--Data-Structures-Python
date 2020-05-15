class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        
        #if node value is less than go left
        if value < self.value:
            if self.left:
            #if empty put it there
                self.left.insert(value)
            else:
            # less than node put it left
                self.left = BinarySearchTree(value)
        elif self.right:
            self.right.insert(value)
        else:
            self.right = BinarySearchTree(value)
            
    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target): #recursion
        #when we start searching self will be the root
        #compare the target against self.root
        if target == self.value:
        # if target matches self value return true
            return True
        if target < self.value:
            #go left if left is a BST node
            if not self.left:
                return False
            return self.left.contains(target)
        else:
            #go right if right is a BST node
            if not self.right:
                return False
            return self.right.contains(target)