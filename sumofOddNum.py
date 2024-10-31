def sum_of_odd(x):
    sum_num = 0
    for i in range (x):
      if not i % 2 == 0:
          sum_num += i
    return sum_num

x = int(input("Enter x: "))
odd_num = sum_of_odd(x)
print(f"The sum of all the odd number from 0 to {x} is {odd_num}")