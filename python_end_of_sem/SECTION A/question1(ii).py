
numbers = [4, 7, 2, 9, 12, 15]

sum_of_odds = 0
for number in numbers:
    if number % 2 != 0:
        sum_of_odds += number
print("The sum of all odd numbers is:", sum_of_odds)