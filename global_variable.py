total = 0


def count():
    global total
    total += 1
    return total


count()
print(count())
print(total)


def count_new(total):
    total += 1
    return total


count_new(total)
print(count_new(total))
print(total)
