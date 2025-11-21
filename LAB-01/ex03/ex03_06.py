def xoa_phan_tu(dictionary, key):
    if key in dictionary:
        del dictionary[key]
        return True
    else:
        return False
    
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
key_to_delete = 'b'
result = xoa_phan_tu(my_dict, key_to_delete)
if result:
    print("Đã xóa phần tử với khóa " , key_to_delete ,". Từ điển sau khi xóa: " , my_dict)
else:   
    print("Khóa" , key_to_delete, " không tồn tại trong từ điển.")