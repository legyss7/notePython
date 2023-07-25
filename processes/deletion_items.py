from file.read_file import read_file
from file.write_file import write_file

def  deletion_items(filename, index_array):
    my_dicts = read_file(filename)  
    my_dicts.pop(index_array)
    write_file(filename, my_dicts)
    return True

    
