#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """Print the first x elements of a given list that are exclusively integers
    Args:
    my_list(list): the list from which the elements will be printed from
    x(int): the number of elements in the my_list which are to be printed.
    Return:
    the number of elements being printed
    """
    ret = 0
    for i in range(0, x):
        try:
            print"{:d}".format(my_list[i]), end="")
            ret += 1
        except (ValueError, TypeError):
            continue
        print("")
        return(ret)
