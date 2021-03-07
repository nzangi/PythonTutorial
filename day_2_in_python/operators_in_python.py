numbers = [1,2,3,4,5]

even_number = []
odd_number = []
addition = 0
avarage = 0
product = 1
largest_number = numbers[0] if numbers else None
smallest_number = numbers[0] if numbers else  None

for number in numbers:
    addition = addition + number
    avarage = addition / len(numbers)
    product = product * number
    if number > largest_number:
        largest_number = number
    if number < smallest_number:
            smallest_number = number
    if number % 2 == 0:
        even_number.append(number)

    else:
        odd_number.append(number)

print(f"The addition of the list is: {addition}")
print(f"The avarage of the list is: {avarage}")
print(f"The product of the list is: {product}")
print(f"Largest number in the list is: {largest_number}")
print(f"Smallest number in the list is: {smallest_number}")
print(f"This is a list of all even numbers in your list: {even_number}")
print(f"This is a list of all odd_number numbers in your list: {odd_number}")










