from file.read_file import read_file

def show_all_items(filename):
    my_dicts = read_file(filename) 
    str = ""
    str = "{:<20} {:<50} {:<25} {:<25}".format("ID", "Header", "Date Of Creation", "Date Of Change") + "\n"
    for i in my_dicts:
        str = str + "{:<20} {:<50} {:<25} {:<25}".format(i["ID"], i["Header"], i["DateOfCreation"], i["DateOfChange"]) + "\n"
    return str
