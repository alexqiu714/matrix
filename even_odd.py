numbers = []
even = []
odd = []

for i in range(1, 51):
    numbers.append(i)
    if i%2 == 0:
        even.append(i)
    if i%2 == 1:
        odd.append(i)

print(numbers)
print(even)
print(odd)