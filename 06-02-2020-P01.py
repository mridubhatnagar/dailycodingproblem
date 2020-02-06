"""
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?

"""


def summation(input_numbers, k):
    result = False
    for x in range(0, len(L)-1):
        for y in range(x+1, len(L)):
            if int(L[x]) + int(L[y]) == k:
                result = True
                break
        if result:
            break
    return result



L = input("Enter a list of integers").split()
print(L, type(L))
k = int(input("Enter the value two numbers from list should add upto"))
result = summation(L, k)
print(result)





