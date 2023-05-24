#problem 1

def sum_to(n):

    return (n * (n + 1) // 2)

print(sum_to(6))
print(sum_to(10))






#problem 2

def largest(nums):
    return max(nums)


print(largest([1, 2, 3, 4, 0]))
print(largest([10, 4, 2, 321, 91, 54]))



#problem 3



def occurrences(string1, string2):
    return string1.count(string2)


print(occurrences('fleep floop', 'e')) 
print(occurrences('fleep floop', 'p'))
print(occurrences('fleep floop', 'ee'))
print(occurrences('fleep floop', 'fe'))





#problem  4


def product(*args):
    result = 1
    for num in args:
        result *= num
    return result

print(product(-1, 4))
print(product(2, 5, 5))
print(product(4, 0.5, 5))


