class Node:
    def __init__(self, val, left=None, right=None):
        self.left = left
        self.right = right
        self.val = val

    def set_child_right(self, child):
        self.right = child

    def set_child_left(self, child):
        self.left = child
    
    def __repr__(self) -> str:
        if self.__has_children():
            return "Parent"
        else:
            return "Leaf"

    def __has_children(self):
        if self.right or self.left:
            return True
        else:
            return False


root = Node(2, Node(3), Node(5))
l1_left = root.left
l1_right = root.right

