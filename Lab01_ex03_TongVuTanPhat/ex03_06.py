def xoa_phan_tu(dictionary, key):
    if key in dictionary:
        del dictionary[key]
        return True
    else:
        return False

# Sử dụng dictionary mẫu
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Nhập key để xóa
key_to_delete = input("Nhập key để xóa: ")

# Xóa và in kết quả
result = xoa_phan_tu(my_dict, key_to_delete)
if result:
    print("Phần tử đã được xóa trong Dictionary.")
else:
    print("Không tìm thấy phần tử để xóa trong Dictionary.")
print("Dictionary sau khi xóa:", my_dict)