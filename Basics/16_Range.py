# my_list = list(range(10))
# print(my_list)
#
# even = list(range(0,10,2))
# odd = list(range(1, 10, 2))
#
# print(even)
# print(odd)

# my_string = "abcdefghijklmnopqrstuvwxyz"
# print(my_string.index('s'))
# print(my_string[4])
#
# small_decimals = range(0,10)
# print(small_decimals)
# print(small_decimals.index(3))
#
# odd = range(1, 10000, 2)
# print(odd)
#
# print(odd[985])
#
# sevens = range(7, 10000, 7)
# x = int(input("Please enter a number from 1 - 10000\n"))
# if x in sevens:
#     print("{} is divisible by seven".format(x))
#
# print(small_decimals)

decimals = range(1,100)
print(decimals)

my_range = decimals[3:40:3]
print(my_range)

for i in my_range:
    print(i)

print('=' * 40)

for i in range(3, 40, 3):
    print(i)

print(my_range == range(3, 40, 3))


