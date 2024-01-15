def reverse_string(str):
    new_str = ''
    for i in str:
        new_str = i + new_str
    return new_str