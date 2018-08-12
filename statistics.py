from math import sqrt

def mean(list):
    return sum(list) / len(list)

def median(list):
    list = sorted(list)
    median = len(list) // 2

    if len(list) % 2 == 1:
        return list[median]

    return mean([list[median-1], list[median]])

def q(list, p):
    q = int(len(list) * p)
    return sorted(list)[q]

#TODO more than one mode could exist
def mode(list):
    list = sorted(list)
    count = 0
    max_count = (0, 0)
    prev_element = list[0]

    for element in list:
        if element == prev_element:
            count += 1
        else:
            count = 0

        if (count >= max_count[1]):
            max_count = (element, count)
        prev_element = element

    return max_count[0]

def scattering(list):
    return max(list) - min(list)

def variance(list, n=None): #sometimes counting starts at 0, which results in the variance to be divided by n-1
    if n == None:
        n = len(list)

    mean1 = mean(list)

    return sum([(mean1 - element) ** 2 / len(list) for element in list])

def standard_deviation(list, n=None):
    return sqrt(variance(list, n))

list = [8,7,9,10,6]

print(median(list))

print(mode(list))

print(standard_deviation(list))
