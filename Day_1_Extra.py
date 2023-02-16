
def longest_value(fruits):
    values = list(fruits.items())
    longest_value = max(values, key=len)
    longest_values = [value for value in values if len(value) == len(longest_value)]
    return longest_values[0]

fruits = {'fruit': 'apple', 'color': 'green'}
first_longest = longest_value(fruits)
print(first_longest)
