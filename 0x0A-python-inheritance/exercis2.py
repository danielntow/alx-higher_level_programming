#!/usr/bin/python3

class Car:

    def accelerate(self):
        print("Car is accelerating!")


class ElectricCar(Car):
    def accelerate(self):
        print("Electric car is accelerating silently")
