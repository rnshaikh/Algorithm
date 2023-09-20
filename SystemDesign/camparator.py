from functools import cmp_to_key


class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        
    def __repr__(self):
        return self.name + "-" + str(self.score)
    
    def comparator(a, b):
        
        if a.score > b.score:
            return -1
        
        if a.score < b.score:
            return 1
        
        if a.name < b.name:
            return -1
        
        if a.name > b.name:
            return 1
        return 0
    

obj1 = Player("Abc", 20)
obj2 = Player("john", 100)
obj3 = Player("doe", 200)
obj4 = Player("anam", 500)
obj5 = Player("hadah", 10)
obj6 = Player("myra", 500)
obj7 = Player("riz", 500)
obj8 = Player("vidya", 200)
obj9 = Player("ketaki", 300)
obj10 = Player("shital", 300)

list1 = [obj1, obj2, obj3, obj4, obj5, obj6, obj7, obj8, obj9, obj10]

data = sorted(list1, key=cmp_to_key(Player.comparator))

for i in data:
    print(i)



