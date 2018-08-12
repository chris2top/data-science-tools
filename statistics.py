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
        print(max_count)

    return max_count[0]


list = [1,2,2,3,3,4,4,5,5,5,6]

print(median(list))

print(mode(list))
