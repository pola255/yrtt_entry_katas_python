# In this Kata, you will be given an array of numbers in which two numbers occur once and the rest occur only twice. 
# Your task will be to return the sum of the numbers that occur only once.
# For example, repeats([4,5,7,5,4,8]) = 15 because only the numbers 7 and 8 occur once, and their sum is 15.
# More examples in the test cases below.

# Good luck!

def repeats(arr):
    count_numbers = {}
    sum_unique = 0
    for number in arr:
        if number in count_numbers:
            count_numbers[number] += 1
        else:
            count_numbers[number] = 1
    for n, count in count_numbers.items():
        if count == 1:
            sum_unique = sum_unique + n
    return sum_unique
