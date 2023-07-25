from file.read_file import read_file

def show_item(filename, index_array):
    my_dicts = read_file(filename) 
    str = ""
    str = str + "\nЗаголовок: "
    str = str + my_dicts[index_array]["Header"] + "\n"
    str = str + "Текст заметки: "
    str = str + my_dicts[index_array]["Text"] + "\n"
    return str
