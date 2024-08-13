# Find min and max numbers in list for using for condition
numbers = [5,6,4,2,20,125,56,74,96,32,3]
max = numbers[0]
min = numbers[0]
for i in range(len(numbers)):
    if numbers[i] > max:
        max = numbers[i]
    elif numbers[i] < min:
        min = numbers[i]

print("max:",max)
print("min:",min)

