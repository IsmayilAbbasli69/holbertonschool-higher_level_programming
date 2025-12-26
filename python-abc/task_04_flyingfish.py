#!/usr/bin/env python3

class Fish:

    def swim():
        print("The fish is swimming")

    def habitat():
        print("The fish lives in water")

class Bird:

    def fly():
        print("The bird is flying")

    def habitat():
        print("The bird lives in the sky")


class FlyingFish(Fish,Bird):

    def fly():
        print("The flying fish is soaring!")

    def swim():
        print("The flying fish is swimming!")

    def habitat():
        print("The flying fish lives both in water and the sky!")

f=FlyingFish
f.fly()
f.swim()
f.habitat()
print(FlyingFish.mro())
