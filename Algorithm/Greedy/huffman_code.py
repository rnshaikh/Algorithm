# huffman code algorithm for prefix free variable length encoding character depend on frequencies.



"""

    if there is 2 character then create tree with two leaf node with 0 and 1 weight
    else:
       call recursive function with char_list
       in recursive function
            check if there is 2 char:
                call compute tree with 2 char
            else:
                sort charcter list with frequency
                pop first 2 char merge them and merge frequnecy and append in sort_character list
                recursively call recur function with new char list
                call compute_tree with left char and right char
    time complexity is O(n2) :
        for sorting time complexity O(n logn)
        we sorting for n-2 * O(n log n)
        O(n2)

    we can reduced time complexity
    to O(n log n) by taking 2 queues 1st for initial sorting char list and another for merge char list

    so once will sort char in 1 st queue
    and every iteraion merge char will store in 2nd queue
    and will pop char from first queue and 2 nd queue will chost merging character accordingly.

"""

class Node:

    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        self.left_weight = None
        self.right_weight = None


class Huffman:

    def __init__(self):

        self.head = None

    def compute_tree(self, char_left, char_right):
        left_char = Node(char_left)
        right_char = Node(char_right)

        if self.head == None:
            node = Node('head', None, None)
            node.left = left_char
            node.left_weight = 0
            node.right = right_char
            node.right_weight = 1
            self.head = node
        else:
            node = self.head
            while(node.right != None):
                node = node.right

            node.left = left_char
            node.left_weight = 0
            node.right = right_char
            node.right_weight = 1

    def huf_calulate(self, chars_sorted):

        if len(chars_sorted) == 2 :
            self.compute_tree(chars_sorted[0][0], chars_sorted[1][0])
        else:
            chars_sorted = sorted(chars_sorted, key=lambda item:item[1])
            first_char = chars_sorted.pop(0)
            second_char = chars_sorted.pop(0)
            merge_char = first_char[0] + second_char[0]
            merge_freq = first_char[1] + second_char[1]
            chars_sorted.append([merge_char, merge_freq])
            self.huf_calulate(chars_sorted)
            self.compute_tree(first_char[0], second_char[0])

    def huf(self, chars):

        if len(chars) == 2:
            tree = self.compute_tree(chars)
        else:
            self.huf_calulate(chars)
        print(self.head.left.data)


if __name__ == "__main__":

    chars_l = [['A', 55], ['B', 20], ['C', 15], ['D', 10]]

    hu = Huffman()
    hu.huf(chars_l)
