"""
You are presented with an integer number larger than 5. Your goal is to identify the longest side
possible in a right triangle whose sides are not longer than the number you are given.

For example, if you are given the number 15, there are 3 possibilities to compose right triangles:

1. [3, 4, 5]
2. [6, 8, 10]
3. [5, 12, 13]

The following function shows one way to solve the problem but the code is not ideal or efficient.
Refactor the code based on what you have learned about code simplicity and efficiency.
"""
"""Looking backwards avoids the use of a second statement."""
"""I have change also the name of the variable for one more meaninfully"""

def my_function(length):
    for x in range(length, 5, -1):
        for y in range(length, 4, -1):
            for z in range(length, 3, -1):
                if x*x == y*y + z*z:
                  return x


max_len = input("What is the maximal length of the triangle side? Enter a number: ")

print("The longest side possible is " + str(my_function(int(max_len))))
