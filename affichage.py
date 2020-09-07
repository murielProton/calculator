#!/usr/bin/env python3.6
import math
import numbers
import decimal

class Affichage():
    _number_float = float
    argument = None
    def convert_into_float(self,argument):
        if type(self.argument)==float:
            self._number_float=self.argument
            pass
        if type(self.argument)==int:
            self._number_float=float(self.argument)
        return self._number_float

# str.isnumeric(argument) ou isinstance(argument) ou math.isnan(argument)
    def are_you_number(self,argument):
        if  math.isnan(self.argument):
            raise Exception ("I am a scientific calculator ! I need numbers.")
        elif isinstance(self.argument, number.Number):
            self.convert_into_float(self.argument)
            #parcours self._recieve_from qui est un string
    
#si j'attrape un nombre je fais si non j'affiche une erreur.
    def __init__(self):
        print(" + for addition\n - for substraction\n * for multiplication\n / for division")
        print(" ^ for power\n r for root\n '%' for modulus\n pie for Pie")
        print(" e for E\n sin for sinus\n cos for cossinus\n tan for tan")
        print(" ! for factorial\n ln for natural log")
        print("Enter your first number :")
        self.first_number = input()
        self.first_number_float = self.are_you_number(self.first_number)
        print("Enter your operator :\n")
        self.operator = input()
        print("Enter your second number :\n")
        self._second_number = input()
        self._second_number_float = self.are_you_number(_second_number)