def highest_even(*args):
    local_highest_even = float("-inf")
    for item in args:
        if item % 2 == 0 and item > local_highest_even:
            local_highest_even = item
    return local_highest_even


print(highest_even(10,20,15, 65, 98, 99))