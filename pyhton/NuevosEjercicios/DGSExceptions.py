""" Create a Python function called divide_numbers that takes two parameters: the numerator and the denominator.

The function should perform the following tasks:

    1   Check if the denominator is equal to 0. If the denominator is 0, it must raise a custom exception called DivisionByZeroError with the message: "Cannot divide by zero."

    2   If the denominator is not 0, it should perform the division and return the result.

    3   In the main program, invoke the divide_numbers function and handle the custom exception if it occurs, displaying the appropriate error message.

Restrictions and Requirements:

    1   You must create the custom exception class DivisionByZeroError, which should inherit from the Exception class.

    2   The function must include a try-except block to handle the exception if it is raised during execution. """
class DivisionByZeroError(Exception):
    def __init__(self,message):
        self.message = message
        
    def __str__(self):
        return self.message


def divide_numbers (numerator,denominator):
    if denominator==0:
        raise DivisionByZeroError("Cannot divide by zero.")
    else:
        return numerator/denominator
        
try:
  print(f"RESULTADO = {divide_numbers(25,5)}")
  print(f"RESULTADO = {divide_numbers(25,0)}")
except DivisionByZeroError as error:
  print(error)

