#!/usr/bin/env python3

# def return_fibonacci(length):
#     if length == 0:
#         fibonacci_list = []
#     elif length == 1:
#         fibonacci_list = [0]
#     else:
#         fibonacci_list = [0, 1]
#     for _ in range(2,length):
#         fibonacci_list.append(fibonacci_list[-1]+fibonacci_list[-2])
#     print(fibonacci_list)
# print(return_fibonacci(9))



def print_fibonacci(length):
    fibonacci_list = [] if length == 0 else [0] if length == 1 else [0, 1]

    for _ in range(2, length):
        next_number = fibonacci_list[-1] + fibonacci_list[-2]
        fibonacci_list.append(next_number)

    print(fibonacci_list)

print(print_fibonacci(9))
