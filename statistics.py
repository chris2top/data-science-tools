from math import sqrt
from vector import dot_product

def mean(list):
    return sum(list) / len(list)

def median(list):
    list = sorted(list)
    median = len(list) // 2

    if len(list) % 2 == 1:
        return list[median]

    return mean([list[median-1], list[median]])

def sub_mean(list): #results has mean of 0
    mean1 = mean(list)
    return [element - mean1 for element in list]

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

def variance(list, offset=0): #sometimes counting starts at 0, which results in the variance to be divided by n-1
    n = len(list)
    mean1 = mean(list)

    return sum([(mean1 - element) ** 2 / (n - offset) for element in list])

def standard_deviation(list, n=0):
    return sqrt(variance(list, n))

def covariance(list_a, list_b, offset=0):  #sometimes counting starts at 0, which results in the covariance to be divided by n-1
    if (len(list_a) != len(list_b)):
        raise Exception("lists must be same length")

    n = len(list_a)
    return dot_product([sub_mean(list_a), sub_mean(list_b)]) / n - offset
    
list = [8,7,9,10,6]

print(mean(sub_mean(list)))
print(median(list))

print(mode(list))

print(standard_deviation(list))

print(covariance([100,49,41,40,25],[22,10,10,10,5]))
