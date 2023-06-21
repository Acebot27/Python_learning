# #1 - testing data type of certain variables
programming_languages = "Python", "Java", "C++", "C#"
programming_languages_0 = ("Python", "Java", "C++", "C#")

print("Data Type of Variable:", type(programming_languages))
print("Contents of Variable:", programming_languages)
print("Data Type of Variable_0:", type(programming_languages_0))
# #Note - In the above way we can declare and assign values to a Tuple

print("\n#########################################################################################################\n")

# #2 - for loop example
for language in programming_languages:
    print(language)
# #Note - In the above way we can access each contents of the List or Tuple

print("\n#########################################################################################################\n")

# #3 - check unique id of an object/variable in python
print(id(programming_languages))  # mostly like allocation address

print("\n#########################################################################################################\n")

# #4 - Quizzes on variable declaration and mutability
x1 = 1


def demo_test1():
    x1 = 2


demo_test1()
print("Quiz 1's output: x =", x1)

x2 = 1


def demo_test2():
    global x2
    x2 = 2


demo_test2()
print("Quiz 2's output: x =", x2)

x3 = [1]


def demo_test3():
    x3 = [2]


demo_test3()
print("Quiz 3's output: x =", x3)

x4 = [1]


def demo_test4():
    global x4
    x4 = [2]


demo_test4()
print("Quiz 4's output: x =", x4)

x5 = [1]


def demo_test5():
    x5[0] = 2


demo_test5()
print("Quiz 5's output: x =", x5)

print("\n#########################################################################################################\n")

# #5 - string concatenation using join operator
nick_names = ['Marimo', 'Anya', 'Baka', 'Akuma', 'Kuma', 'Daki']
print('NICKNAMES: ' + ' | '.join(nick_names))

print("\n#########################################################################################################\n")

# #6 - join operator with os package's open method
import os

dir_location = './notes'
file_name = 'basics_notes.txt'
with open(os.path.join(dir_location, file_name)) as f:
    print(f.read(6))

print("\n#########################################################################################################\n")

# #7 - uses of ArgsParser package for reading arguments through CLI
import argparse
import sys


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--x', type=float, default=1.0,
                        help='What is the first number?')
    parser.add_argument('--y', type=float, default=1.0,
                        help='What is the second number?')
    parser.add_argument('--operation', type=str, default='add',
                        help='What operation? Can choose add, sub, mul, or div')
    args = parser.parse_args()
    sys.stdout.write("Output of 7th rough work part CALC(Default addition of 1 + 1): " + str(calc(args)) + "\n")


def calc(args):
    if args.operation == 'add':
        return args.x + args.y
    elif args.operation == 'sub':
        return args.x - args.y
    elif args.operation == 'mul':
        return args.x * args.y
    elif args.operation == 'div':
        return args.x / args.y


main()
'''
    usage in CLI: python rough_work_code.py [-h] [--x X] [--y Y] [--operation OPERATION]
    
    optional arguments:
      -h, --help            show this help message and exit
      --x X                 What is the first number?
      --y Y                 What is the second number?
      --operation OPERATION
                            What operation? Can choose add, sub, mul, or div
                            
    Eg.: python rough_work_code.py --x 2 --y 5 --operation mul
    It outputs 10.0 as answer.
'''

print("\n#########################################################################################################\n")

# #8 - fibonacci series as generator
print("Output of 8th rough work part -> Fibonacci Series generator:")


def fibonacci_numbers(nums: int = 5):   # this is generator function (generator function have yield instead of return)
    x, y = 0, 1
    for _ in range(nums):
        x, y = y, x + y
        yield x


fib_generator = fibonacci_numbers(10)
fib_generator2 = fibonacci_numbers(10)
print(fib_generator)                    # this is a generator object
print(i for i in fib_generator)         # this is a generator expression
[print(i) for i in fib_generator]       # displaying/accessing/iterating the generator(any object) value
print([i for i in fib_generator2])      # converted each values of generator into list elements and displaying as list

print("\n#########################################################################################################\n")

# #9 - using enumerate for creating a dict of a list

eg_list = ['left', 'right', 'up', 'down']

eg_dict = dict(enumerate(eg_list))
print("Output of 9th rough work part -> List to dict using enumerate() method: \n"
      "List_values are -> ", eg_list, "\nDict -> ", eg_dict)

print("\n#########################################################################################################\n")

# #10 - example of zip() method usage

x = [1, 4, 2, 7]
y = [9, 0, 3, 2]
point_name = ['A', 'B', 'C', 'D']

co_ordinates_dict = dict(
                        zip(point_name, zip(
                                            x, y
                                        )
                            )
                    )

print("Output of 10th rough work part -> Points coordinates dict using zip() method: \n"
      "Co-ordinates DICT: ", co_ordinates_dict)

print("\n#########################################################################################################\n")

# #11 - example of zip() method usage
