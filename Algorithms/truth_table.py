a_bool = True
b_bool = True

print("________________________________________________________")
print("|A\t|B\t|not A\t|not B\t|A and B\t|A or B\t|")
print(f"|{a_bool}\t|{b_bool}\t|{not a_bool}\t|{not b_bool}\t|{a_bool and b_bool}\t\t|{a_bool or b_bool}\t|")
a_bool = False
b_bool = False
print(f"|{a_bool}\t|{b_bool}\t|{not a_bool}\t|{not b_bool}\t|{a_bool and b_bool}\t\t|{a_bool or b_bool}\t|")
a_bool = True
print(f"|{a_bool}\t|{b_bool}\t|{not a_bool}\t|{not b_bool}\t|{a_bool and b_bool}\t\t|{a_bool or b_bool}\t|")
b_bool = True
a_bool = False
print(f"|{a_bool}\t|{b_bool}\t|{not a_bool}\t|{not b_bool}\t|{a_bool and b_bool}\t\t|{a_bool or b_bool}\t|")
print("________________________________________________________")

a_set = {1, 2, 3, 4}
b_set = {3, 4, 5, 6}
print("_________________________________________________________________________________")
print("|A\t\t|B\t\t|And\t\t|Or\t\t\t|Not\t|")
print(f"{a_set}\t|{b_set}\t|{a_set.intersection(b_set)}\t\t|{a_set.union(b_set)}\t|{a_set.difference(b_set)}\t|")
print("_________________________________________________________________________________")


def list_intersection(a, b):
    result = []
    for i in range(len(a)):
        for y in range(len(b)):
            if a[i] == b[y]:
                result.append(a[i])
                break
    return result


def list_difference(a, b):
    del_a = []
    del_b = []
    for i in range(len(a)):
        for y in range(len(b)):
            if a[i] == b[y]:
                del_a.append(i)
                del_b.append(y)
                break
    for i in range(len(del_a)):
        a.pop(del_a[i] - i)
    return a


def list_union(a, b):
    return list_difference(a, b) + b


a_list = [1, 2, 3, 4]
b_list = [3, 4, 5, 6]

print("_________________________________________________________________________________")
print("|A\t\t|B\t\t|And\t\t|Or\t\t\t|Not\t|")
print(f"{a_list}\t|{b_list}\t|{list_intersection(a_list, b_list)}\t\t|{list_union(a_list, b_list)}\t|{list_difference(a_list, b_list)}\t|")
print("_________________________________________________________________________________")