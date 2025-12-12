def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def get_char_count(text):
    numofchars={}
    for i in text:
        lower=i.lower()
        if lower not in numofchars:
            numofchars[lower]=1
        else:
            numofchars[lower]+=1
    return numofchars

def return_sorted_dict(dictionary):
    new_list = []
    for i in dictionary:
        count = dictionary[i]
        new_list.append({"char":i, "num":count})
    new_list.sort(reverse=True, key=sort_on)
    return new_list


def sort_on(item):
    return item["num"]


