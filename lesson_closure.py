def print_msg(number):
    def printer():
        "Here we are using the nonlocal keyword"
        nonlocal number
        number=3
        print(number)
    printer()
    print(number)

print_msg(9)


def multiplier_of(n):
    def multiplier(number):
        print(number)
        print(n)
        return number*n
    return multiplier

multiplywith5 = multiplier_of(5)
print(multiplywith5(9))