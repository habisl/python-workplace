#!/usr/bin/env python3
# Python3 function to check fizzbuzz


def fizz_buzz(num):
    if num % 5 == 0 and num % 3 == 0:
      print("FizzBuzz")
    elif num % 3 == 0:
      print("Fizz")
    elif num % 5 ==0:
      print("Buzz")
    else:
      print(num)

for num in range(1,101):
  fizz_buzz(num)
