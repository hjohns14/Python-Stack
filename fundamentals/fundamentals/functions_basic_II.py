def countdown(num):
    myList = []
    for i in range(num, -1, -1):
        myList.append(i)
    return myList

def print_and_return(lst):
    print(lst[0])
    return lst[1]

def first_plus_len(lst):
    return lst[0] + len(lst)

def val_greater_than_second(lst):
    new_list = []
    count = 0
    if len(lst) < 2:
        return False
    for x in lst:
        if x > lst[1]:
            count += 1
            new_list.append(x)
    print(count)
    return new_list

def this_len_that_val(length, value):
    my_list = [value for i in range(length)]
    return my_list

print(countdown(5))
print(print_and_return([1, 2]))
print(first_plus_len([1, 2, 3, 4, 5]))
print(val_greater_than_second([5, 2, 3, 2, 1, 4]))
print(val_greater_than_second([2]))
print(this_len_that_val(4, 7))
print(this_len_that_val(6, 2))
