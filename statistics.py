def mean(list):
    return sum(list) / len(list)

def median(list):
    list = sorted(list)
    median = len(list) // 2

    if len(list) % 2 == 1:
        return list[median]

    return mean([list[median-1], list[median]])

list = [1,2,4,5,6]

print(median(list))
