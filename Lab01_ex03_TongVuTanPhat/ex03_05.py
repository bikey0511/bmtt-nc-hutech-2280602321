def dem_so_lan_xuat_hien(lst):
    count_dict = {}
    for item in lst:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    return count_dict

# Nhập danh sách từ người dùng
input_string = input("Nhập danh sách các số, cách nhau bằng dấu phẩy: ")
word_list = input_string.split(',')

# Đếm và in kết quả
so_lan_xuat_hien = dem_so_lan_xuat_hien(word_list)
print("Số lần xuất hiện của mỗi phần tử:", so_lan_xuat_hien)