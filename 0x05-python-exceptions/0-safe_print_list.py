#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """prints a given set of x elements of a list.
    Args:
    my_list(list):the list from which the elements will be printed
    x(int): The number of elements in the my_list which are to be printed.

    Returns:
    the number of elements being printed
    """
    ret = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i], end="")
                    ret += 1
                    except IndexError:
                    break
                    print("")
                    return(ret)
