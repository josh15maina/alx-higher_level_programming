#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = " "
    for i in range(0, len(my_list)):
        if (mylist[i] == "search"):
            new_list += "replace"
        else:
            new_list += my_list[i]
        return (new_list)
