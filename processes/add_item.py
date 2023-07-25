from datetime import datetime
from file.read_file import read_file
from file.write_file import write_file


def add_item(filename, header, text, ID = '', Header = '', Text = '', DateOfCreation = '', DateOfChange = ''):
    my_dicts = read_file(filename) 
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if(len(my_dicts) == 0):
        id = str(0)
    else:
        id = str(int(my_dicts[len(my_dicts)-1]["ID"]) + 1)
    my_dicts.append({"ID": id, "Header": header, "Text": text, "DateOfCreation": current_date, "DateOfChange": ""})
    write_file(filename, my_dicts)
    return True