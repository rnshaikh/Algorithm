


class Node:

    def __init__(self, data=None, left=None, right=None):

        self.data = data
        self.left = left
        self.right = right


class BST:

    def __init__(self, root=None):
        self.root = root

    def insert(self, data):

        node = Node(data)

        if not self.root:
            self.root = node
            return

        temp = self.root
        prev_temp = self.root

        while(temp != None):

            if temp.data >= data:
                prev_temp = temp
                temp = temp.left

            elif temp.data < data:
                prev_temp = temp
                temp = temp.right

        if prev_temp.data > data:
            prev_temp.left = node
        else:
            prev_temp.right = node


    def recursive_insert(self, root, data):

        if not root:
            root = Node(data)

        elif(root.data<=data):
            root.right = self.recursive_insert(root.right, data)

        elif(root.data>data):
            root.left = self.recursive_insert(root.left, data)

        return root

    def search(self, data):

        temp = self.root

        if not temp:
            return -1

        while(temp != None):

            if temp.data < data:
                temp = temp.right

            elif temp.data > data:
                temp = temp.left

            elif temp.data == data:
                return data

        return -1

    def recursive_search(self, root, data):

        if not root:
            return -1
        elif root.data > data:
            return self.recursive_search(root.left, data)
        elif root.data < data:
            return self.recursive_search(root.right, data)
        elif root.data == data:
            return data

    def find_min(self):

        temp = self.root
        prev = self.root

        if not temp:
            return -1
        while(temp != None):
            prev = temp
            temp = temp.left

        return prev.data

    def find_min_recursively(self, root):

        if not root:
            return -1
        elif root.left == None:
            return root
        return self.find_min_recursively(root.left)

    def find_max(self):

        temp = self.root
        prev = self.root

        if not temp:
            return -1

        while temp != None:
            prev = temp
            temp = temp.right

        return prev.data

    def find_max_recursively(self, root):

        if not root:
            return -1
        elif root.right == None:
            return root.data

        return self.find_max_recursively(root.right)

    def find_height(self, root):

        if not root:
            return 0

        return max(self.find_height(root.left), self.find_height(root.right)) + 1

    def level_order_traversal(self):

        queue = []
        queue.append(self.root)

        while len(queue):

            node = queue.pop(0)
            print(node.data)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    def preorder(self, root):

        if not root:
            return
        print(root.data)
        self.preorder(root.left)
        self.preorder(root.right)

    def inorder(self, root):

        if not root:
            return
        self.inorder(root.left)
        print(root.data)
        self.inorder(root.right)

    def postorder(self, root):

        if not root:
            return

        self.postorder(root.left)
        self.postorder(root.right)
        print(root.data)

    def isBST(self, root, minvalue, maxvalue):

        if root == None:
            return True

        if (root.data>minvalue and root.data<maxvalue and
            self.isBST(root.left, minvalue, root.data) and self.isBST(root.right, root.data, maxvalue)):
            return True
        else:
            return False

    def deleteNode(self, root, data):

        if root == None:
            return root

        elif root.data>data :
            root.left = self.deleteNode(root.left, data)

        elif root.data<data:
            root.right = self.deleteNode(root.right, data)

        else:
            if(root.left == None and root.right==None):
                import pdb
                pdb.set_trace()
                del root
                root = None

            elif(root.left == None):
                import pdb
                pdb.set_trace()
                temp = root
                root = root.right
                del temp

            elif(root.right == None):
                import pdb
                pdb.set_trace()
                temp = root
                root = root.left
                del temp
            else:
                minnode = self.find_min_recursively(root.right)
                root.data = minnode.data
                root.right = self.deleteNode(root.right, minnode.data)
        return root

    def find(self, root, data):

        if not root:
            return None

        elif root.data == data:
            return root

        elif root.data > data:
            return self.find(root.left, data)

        elif root.data < data:
            return self.find(root.right, data)

    def get_successor(self, root, data):

        current = self.find(root, data)

        if not current:
            return -1

        if current.right != None:
            min_node = self.find_min_recursively(current.right)
            return min_node.data
        else:

            successor = None
            ancestor = root
            while(ancestor != current):
                if(ancestor.data > current.data):
                    successor = ancestor
                    ancestor = ancestor.left
                else:
                    ancestor = ancestor.right
            return successor.data


if __name__ == "__main__":

    bst = BST()
    n = int(input("""Enter one of the below option :
                    1) Insert
                    2) Search
                    3) recursive_insert
                    4)recursive_search
                    5)Find Min
                    6)Find Max
                    7)Find Min Recurs.
                    8)Find Max Recurs.
                    9)Height
                    10)level order traversal
                    11)preorder
                    12)inorder
                    13)postorder
                    14)IsBST
                    15)Delete Node
                    16) Inorder Successor
                    17)Exit"""))

    while(True):

        if n == 1:
            data = int(input("Enter a data:"))
            bst.insert(data)

        if n == 2:
            data = int(input("Enter a data to be search:"))
            print(bst.search(data))

        if n == 3:
            data = int(input("Enter a data to be insert recursively:"))
            bst.root = bst.recursive_insert(bst.root, data)
            print("Root:", bst.root.data)

        if n == 4:
            data = int(input("Enter a data to be search recursively:"))
            print(bst.recursive_search(bst.root, data))

        if n == 5:
            print(bst.find_min())

        if n == 6:
            print(bst.find_max())

        if n == 7:
            print(bst.find_min_recursively(bst.root))

        if n == 8:
            print(bst.find_max_recursively(bst.root))

        if n == 9:
            print(bst.find_height(bst.root))

        if n == 10:
            bst.level_order_traversal()

        if n == 11:
            bst.preorder(bst.root)

        if n == 12:
            bst.inorder(bst.root)

        if n == 13:
            bst.postorder(bst.root)

        if n == 14:
            print(bst.isBST(bst.root, -9999, 9999))

        if n == 15:
            data = int(input("Enter a data to be deleted:"))
            bst.deleteNode(bst.root, data)

        if n == 16:
            data = int(input("Enter a data to be inorder successor:"))
            print(bst.get_successor(bst.root, data))

        if n == 17:
            print("Good Bye!!!")
            break;

        n = int(input("""Enter one of the below option :
                    1) Insert
                    2) Search
                    3) recursive_insert
                    4) recursive_search
                    5) Find Min
                    6) Find Max
                    7) Find Min Recurs.
                    8) Find Max Recurs.
                    9) Height
                    10)level order traversal
                    11)preorder
                    12)inorder
                    13)postorder
                    14)IsBst
                    15)Delete
                    16)Inorder Successor
                    17) Exit
                    """))

