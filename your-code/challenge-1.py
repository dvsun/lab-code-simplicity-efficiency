"""
This is a dumb calculator that can add and subtract whole numbers from zero to five.
When you run the code, you are prompted to enter two numbers (in the form of English
word instead of number) and the operator sign (also in the form of English word).
The code will perform the calculation and give the result if your input is what it
expects.

The code is very long and messy. Refactor it according to what you have learned about
code simplicity and efficiency.
"""

trans_dict = {"zero" : 0, "one": 1, "two" : 2, "three" : 3, "four": 4, "five" : 5}
inv_trans_dict = { 0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight",
                   9: "nine", 10: "ten"}
list_var = ["zero", "one", "two", "three", "four", "five", "minus", "plus"]


"""I define two functions to transforms the input values and the final values from words to numbers and reversely"""

def transform(var):
    return trans_dict[var]


def inv_transform(var):
    return  inv_trans_dict[var]


print('Welcome to this calculator!')
print('It can add and subtract whole numbers from zero to five')
a = input('Please choose your first number (zero to five): ')
b = input('What do you want to do? plus or minus: ')
c = input('Please choose your second number (zero to five): ')


"""In order to avoid the last lines, I create a list with all the elements that the user should write. If input is not an element of the list, prints the negative statement."""

if a not in list_var or c not in list_var or b not in list_var:
    print("I am not able to answer this question. Check your input.")
else:
    d = transform(a) + transform(c)
    e = transform(a) - transform(c)

if b == "plus":
    print(f"{a} plus {c} equals {inv_transform(d)}.")
elif b == "minus":
    print(f"{a} minus {c} equals negative {inv_transform(abs(e))}.")

"""Thanks to transform it, I can make the calculation in numbers. I finally return the calculate value in words using the inverse transformation"""

print("Thanks for using this calculator, goodbye :)")
