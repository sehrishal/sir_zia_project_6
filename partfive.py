# 5. Static Variables and Static Methods
# Assignment:
# Create a class MathUtils with a static method add(a, b) that returns the sum. No class or instance variables should be used.

# solution

class MathUtils:
    @ staticmethod
    def add(a, b):
        return a + b
    
result = MathUtils.add(12 ,6)
print("Sum of my numbers are:", result)