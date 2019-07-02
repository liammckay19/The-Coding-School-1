aList = [
    ["Alice", "I love pizza."], # index 0
    ["Bob", "Spongebob rules"],  # index 1
    ["Cece", "Computer science is so cool."]  # index 2
]

# to cast a variable type
# type the name of the variable type we want
# then add parentheses around the variable we want to convert
# variableType(oldVariable)
# - has the type variableType

aTuple = tuple(aList[0])
bTuple = tuple(aList[1])
cTuple = tuple(aList[2])

print(aTuple)
print(bTuple)
print(cTuple)

# object types/variable types
# list = [1, 3, 4]
# boolean = True False bool(1) bool(0)
# dictionary = {"word":1, "word1":"definition", "key":"value"}
# integers = 1, 0, etc.
# float = 1.0, 3.4, 2.5 etc.
# tuples = (1, 3, "a")
# sets = {3,4,5,7}
# strings = "abcasf"