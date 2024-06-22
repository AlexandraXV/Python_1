lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]

filtered_numbers = []
for number in lst:
  if number < 30 and number % 3 == 0:
    filtered_numbers.append(number)

print(filtered_numbers)