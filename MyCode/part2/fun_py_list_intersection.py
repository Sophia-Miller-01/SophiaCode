# fun_py_list_intersection.py

def fun_py_list_intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))

def test_list_intersection():
    list1 = [1, 2, 3, 4, 5]
    list2 = [4, 5, 6, 7, 8]
    print(f"Intersection: {fun_py_list_intersection(list1, list2)}")

if __name__ == "__main__":
    test_list_intersection()
