old_print = print


def print_up(*args):
    args_upcased = [str(arg).upper() for arg in args]
    old_print(*args_upcased)


print = print_up
print('Нельзя ли потише?')