# Control Flow Examples: if, for, while

# if statement
num = 7
if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")

# for loop
print("For loop from 1 to 5:")
for i in range(1, 6):
    print(i)

# while loop
print("While loop counting down from 3:")
count = 3
while count > 0:
    print(count)
    count -= 1
print("Done!")
