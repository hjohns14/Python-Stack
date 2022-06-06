class Node:
    all_nodes = []

    def __init__(self, val, left=None, right=None):
        self.left = left
        self.right = right
        self.val = val
        Node.all_nodes.append(self)

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

    @classmethod
    def displayNodes(cls):
        print(cls.all_nodes)
    
    @staticmethod
    def checkNodeFull(node):
        if node:
            return True
        else:
            return False



root = Node(2, Node(3), Node(5))
Node.displayNodes()

