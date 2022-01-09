"""
Implement the RandomizedSet class:

RandomizedSet() Initializes the RandomizedSet object.
bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
You must implement the functions of the class such that each function works in average O(1) time complexity.
"""





"""
    user array to append element at index
    store val as key index as val in dict

    at delete
    move value to last element of array
    delete last element of array

    in dict update last_val index as deleted element index

    random
        use random.randrange(0, len(arr))


"""


class RandomizedSet:

    def __init__(self):
        self.arr = []
        self.hashd = {}

    def insert(self, val: int) -> bool:

        index = self.hashd.get(val, None)
        if index!=None:
            return False

        ind = len(self.arr)
        self.arr.append(val)
        self.hashd[val] = ind
        return True

    def remove(self, val: int) -> bool:

        index = self.hashd.get(val, None)
        if index == None:
            return False

        last = len(self.arr) - 1
        last_val = self.arr[last]

        self.arr[index], self.arr[last] = self.arr[last], self.arr[index]

        self.arr.pop(-1)


        self.hashd[last_val] = index
        del self.hashd[val]

        return True

    def getRandom(self) -> int:
        index = random.randrange(0, len(self.arr))
        return self.arr[index]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
