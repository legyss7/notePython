from datetime import datetime
from file.read_file import read_file
from file.write_file import write_file


def change_item(filename, index_array, status_header, header, status_text, text):
    if(status_header == True or status_text == True):
        my_dicts = read_file(filename)
        current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if(status_header == True):
            my_dicts[index_array]["Header"] = header
            my_dicts[index_array]["DateOfChange"] = current_date
        if(status_text == True):
            my_dicts[index_array]["Text"] = text
            my_dicts[index_array]["DateOfChange"] = current_date
        write_file(filename, my_dicts)
        return True
    else:
        return False

