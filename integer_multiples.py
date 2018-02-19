"""
If we list all the positive integers below 20 that are multiples of 5 or 7, we get 5, 7, 10, 14 and 15. The sum of these multiples is 51.
Find the sum of all the multiples of 5 or 7 below 1000.
"""

total_sum = 0
for i in range(999):
    if i % 5 == 0 or i % 7 == 0:
        total_sum = total_sum + i
print(total_sum)

#Answer: 156361
