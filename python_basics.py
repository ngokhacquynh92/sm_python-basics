
from math import sqrt, dist
import roman
# import pygame

# # # Waypoint 1: Say Greeting


def hello():
    """Hello function will print out "Hello <name> !"""
    name = input("What is your name?: ").strip(" ")
    print(f"Hello {name}!")

# hello()


# # # Waypoint 2: Pythagorean theorem

def calculate_hypotenuse(a, b):
    """Caldulate hypotense and the number must be integer or float """
    hypotense = sqrt(a ** 2 + b ** 2)
    print(hypotense)

# calculate_hypotenuse(3, 4)


# # # Waypoint 3: Check are all the conditions True

def are_all_conditions_true(list_booleans):
    """Check all conditons true"""
    if not list_booleans:
        print(None)
    else:
        result = all(list_booleans)
        print(result)


# list_test_true = [True, True, True, True, True]
# are_all_conditions_true(list_test_true)


# # # Waypoint 4: Check at least one condition is True

def is_a_condition_true(list_conditions):
    """
    Check condtions if there is a True return True, else return False,
    empty list will return None
    """
    if not list_conditions:
        print(None)
    elif any(list_conditions):
        print(True)
    else:
        print(False)

# list_conditions = []
# is_a_condition_true(list_conditions)


# # # Waypoint 5: fillter integer

def filter_intergers_greater_than(list, check_num):
    """Filter integers in list where number greater than check_num input"""
    result = []
    for num in list:
        if num > check_num:
            result.append(num)
    print(result)

# list = [0, 3, 5, -2, 9, 8]
# filter_intergers_greater_than(list, 6)


# # # Waypoint 6: Find Cheapest hotels

def find_cheapest_hotels(hotel_daily_rates, maximum_daily_rate):
    """Find cheapest hotels via hotel daily rates and
    maximum daily rate
    """
    list_cheapest_hotels = []
    for price in hotel_daily_rates:
        if price[1] <= maximum_daily_rate:
            list_cheapest_hotels.append(price)
    
    sorted_list = sorted(list_cheapest_hotels, key=lambda price: price[1])
    # print(sorted_list)
    results = []
    for item in sorted_list:
        results.append(item[0])

    print(results)

# hotel_daily_rates = [
#         ('Majestic Saigon Hotel', 93),
#         ('Hotel Grand Saigon', 120),
#         ('Sofitel Saigon Plaza', 123),
#         ('Hotel Continental', 62),
#         ('Caravelle Hotel', 180),
#         ('Sheraton Saigon Hotel', 216),
#         ('Park Hyatt Saigon', 209)
#     ]

# find_cheapest_hotels(hotel_daily_rates, 150)


# # # Waypoint 7: Caculate euclidean distance between 2 points
def calculate_euclidean_distance(x, y):
    """
    Caculate euclidean distance between 2 points,
    p1 and p2 are tuple(X,Y)
    """
    result = dist(x, y)
    print(result)

# x = (1, 1)
# y = (2, 2)

# calculate_euclidean_distance(x, y)


# # # Waypoint 8: Caculate euclidean distance between points

# # # Waypoint 9: Capitalize words

def capitalize_words(s):
    """ Capitalize first character in each words, remove useless space
    and raise Type Error if argument is not a string
    """
    if isinstance(s, str):
        result = " ".join(s.split())
        result.title()
        return result
    else:
        raise TypeError("Not a string")

# number_test = 69
# string_test = 'Không  có gì    quý hơn  độc lập      tự do'
# print(capitalize_words(string_test))


# # # Waypoint 10: Uppercase Lowercase Words

def uppercase_lowercase_words(s):
    """
    Uppercase lowercase words,
    where a word has an index number is Even Number will be uppercase,
    where a word has an index number is Odd Number will be lowercase
    """

    results = []
    if isinstance(s, str):
        convert_str_list = list(s.split())
        for index in range(0, len(convert_str_list)):
            if index % 2 == 0:
                results.append(convert_str_list[index].upper())
            else:
                results.append(convert_str_list[index].lower())
    else:
        raise TypeError("Not a string")

    print(results)

# str_teset = 'Lorem ipsum dolor sit amet'

# uppercase_lowercase_words(str_teset)


# # # Waypoint 11: Factorial

def calculate_factorial(num):
    """
    Input n is an integer and return resutl n!,
    return Type Error if n is not integer,
    return Value Error if n is a negative integer.
    """

    factorial = 1
    if type(num) != int:
        raise TypeError("Not an interger")
    elif num < 0:
        raise ValueError("Not a positive integer")
    elif num == 0:
        print("The factorial of 0 is: 1")
    else:
        for i in range(1, num + 1):
            factorial = factorial * i
        print(f"factorial of {num} is : {factorial}")

# [(n, calculate_factorial(n)) for n in range(6)]
# calculate_factorial(0)

# note: for quickly calculate factorical we can use library math.factorial(num)


# # # Waypoint 12: Convert Character to integer

def char_to_int(c):
    """
    input a character and check if character not a string raise TypeError,
    if character > 1 character or not a digit raise ValueError.
    """
    if type(c) is not str or type(c) is None:
        raise TypeError('Not a string')

    elif c.isdigit() and 1 <= int(c) <= 9:
        # get position c in ASCII
        get_position = ord(c)
        # convert position in ascii to number
        convert_to_num = int(chr(get_position))
        print(convert_to_num)
    else:
        raise ValueError("Not a sigle digit")


# char_to_int('6')


# # # Waypoint 13: String to integer

# def string_to_int(s):
#     """
#     String to integer
#     """

#     result = ''
#     if type(s) is None or type(s) is int:
#         raise TypeError("Not a string")
#     elif not s.isdigit():
#         raise ValueError("Not a positive integer string expression")
#     else:
#         pass

# # # Waypoint 14: Is palindrome


# # # Waypoint 15: Convert Roman numerals to ingeger

def roman_numeral_to_int(roman_num):

    """
    Convert Roman numerals to ingeger
    """
    result = 0

    if type(roman_num) != str:
        raise TypeError("Not a string")
    elif type(roman_num) is None:
        raise ValueError("Not a Roman numeral")
    else:
        check_roman_n = roman.fromRoman(roman_num)
        if check_roman_n:
            result += check_roman_n
            return result

# r_num = 234
# print(roman_numeral_to_int(r_num))


# # # Waypoint 16: Play Music

# pygame.init()
# sound = pygame.mixer.Sound('./duke_nukem_groovy.ogg')
# channel = sound.play()
