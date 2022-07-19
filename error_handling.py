''' Assertion error
We can create our own error from the user
if the statement is not satisfied then it will throw the assertion error to us,
if the statement is satisfied then it will print the number that's it. '''

# d = float(input("Enter the value of d :"))
# if d <18:
#    assert print("You are not eligible to marriage")         #     assert print("You are not eligible to marriage")         #


''' Making your own error using exception'''


v = float(input("Enter the value of v :"))
if v > 40:
    raise Exception ("It is more than 40")                              # Exception: It is more than 40




