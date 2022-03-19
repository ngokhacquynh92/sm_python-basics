
from math import sqrt, dist
from unittest import result


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
    
    sorted_list= sorted(list_cheapest_hotels, key=lambda price: price[1])
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

def calculate_euclidean_distance_between_points():
    pass
#???????????????????????????


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

str_teset = 'one two three four five'

a = list(str_teset.split())
result = ""

for i in range(0, len(a)):
    if i % 2 == 0:
        print(i)
        result += str(a[i]).upper()
    else:
        result += str(a[i]).lower()
print(result)