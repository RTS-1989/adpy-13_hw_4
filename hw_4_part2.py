import hashlib
from hw_4_part1 import logger

@logger('C:\\Homework\\log\\')
def get_hash_md5(file_string) -> hex:
    hash_object = hashlib.md5(file_string.encode())
    return hash_object.hexdigest()

@logger('C:\\Homework\\log\\')
def string_hash_generator(file_path):

    strings_list = []
    
    with open(file_path, 'r', encoding='utf8') as fi:
        
        for line in fi.readlines():
            strings_list.append(line)
        start = 0
        end = len(strings_list)-1
        print(len(strings_list))
        while start <= end:
            yield get_hash_md5(strings_list[start])
            start += 1
       
if __name__ == '__main__':  
    for item in string_hash_generator('some_text.txt'):
        print(item)
