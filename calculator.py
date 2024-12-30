"""Program of Basic Calculator"""
class Calculator:
    """Basic Operations in Calculator"""
    def add(self, a, b):
        """Adding 2 Values"""
        return a + b

    def subtract(self, a, b):
        """Subtracting 2 Values"""
        return a - b

    def multiply(self, a, b):
        """Multiplying 2 Values"""
        return a * b

    def divide(self, a, b):
        """Dividing 2 Values"""
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b

# def add(a, b):
#     return a + b

# def subtract(a, b):
#     return a - b

# def multiply(a, b):
#     return a * b

# def divide(a, b):
#     if b == 0:
#         raise ValueError("Cannot divide by zero")
#     return a/b  

# print(add(2,3))
# print(subtract(5,3))
# print(multiply(4,3))
# print(divide(6,3))