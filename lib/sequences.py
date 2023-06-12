#!/usr/bin/env python3

def print_fibonacci(length):
    fib_list = [0, 1]
    if length == 0:
       print([])
    elif length == 1:
        print([0])
    elif length == len(fib_list):    
        print(fib_list)
    else:
        for i in range(1, length-1):
            fib_list.append(fib_list[i] + fib_list[i - 1])
        print(fib_list)


print_fibonacci(100)
