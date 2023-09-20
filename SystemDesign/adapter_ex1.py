"""

The adapter pattern convert the interface of a class into another interface clients expect. 
Adapter lets classes work together that couldn’t otherwise because of incompatible interfaces.

"""


class Bird:

    def fly(self):
        pass

    def make_sound(self):
        pass

class Sparrow(Bird):

    def fly(self):
        print("Fly...")

    def make_sound(self):
        print("Chirp, Chirp")



class ToyDuck:

    def squeak(self):
        pass


class PlasticToyDuck(ToyDuck):

    def squeak(self):
        print("Squeak, Squeak")




class BirdAdapter(ToyDuck):

    def __init__(self, obj):
        self.obj = obj

    def squeak(self):
        self.obj.make_sound()



if __name__ == "__main__":

    sparrow = Sparrow()
    plastic_duck = PlasticToyDuck()
    bird_adapter = BirdAdapter(sparrow)

    print("sparrow...")
    print(sparrow.fly())
    print(sparrow.make_sound())

    print("Duck...")
    print(plastic_duck.squeak())

    print("BirdAdapter...")
    print(bird_adapter.squeak())











