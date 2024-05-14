def oxford_comma(items):
    if len(items) < 2:
        return "".join(items)
    last_element = items[-1]
    add_and = "and " + last_element
    items[-1] = add_and
    if len(items) == 2:
        return " ".join(items)
    else : return ", ".join(items)
    

print(oxford_comma(["fiddleheads", "okra", "kohlrabi"]))