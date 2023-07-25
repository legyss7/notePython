from file.read_file import read_file

def  search_id(filename, id): 
    my_dicts = read_file(filename) 
    index_array = 0
    for i in my_dicts:
        if(i["ID"] == id):
            return index_array
        index_array = index_array + 1
    return -1