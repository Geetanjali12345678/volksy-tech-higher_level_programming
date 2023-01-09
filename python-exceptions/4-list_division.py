#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    return_list = []
    for i in range(list_length):
        try:
            result = (my_list[1] / my_list_2[i])
        except TypeError:
            print("Wrong type")
            result = 0
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        finally:
            return_list.append(result)
        return return_list
