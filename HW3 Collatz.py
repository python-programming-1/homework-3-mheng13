# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 18:40:29 2019

@author: Magnus
"""
def collatz(num):  
        if num % 2 == 0:
            print(num // 2)
            return num // 2
        elif num % 2 ==1:
           oddNum = (3 * num) +1
           print(oddNum)
           return oddNum

try:   
    n = int(input("Enter number:"))       
    while n != 1:
        n = collatz(n)
except ValueError:
    print("Oops! You did not enter a valid number!")          