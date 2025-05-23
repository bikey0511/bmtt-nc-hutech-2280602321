def tao_tuple_tu_list(lst):
    return tuple(lst)

input_list = list(map(int, input("Nhập danh sách các số, cách nhau bằng dấu phẩy: ").split(',')))
my_tuple = tao_tuple_tu_list(input_list)
print("List:", input_list)
print("Tuple từ List:", my_tuple)