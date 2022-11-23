# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 22:34:18 2022

@author: PC
"""

import random

def guess(num):
    random_number = random.randint(1,num)
    guess = 0
    while guess != random_number:
        guess = int(input("Guess the number:"))
        if guess < random_number:
            print("Too low.")
        elif guess > random_number:
            print("Too high.")
    print("Congrats.",guess,"is the right number.")
guess(10)