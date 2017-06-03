def reverse_string(argument):
    temp = []
    counter = 1
    while counter <= len(argument):
        temp.append(argument[-counter])
        counter += 1
    return ''.join(temp).lower
    # print(''.join(temp).lower)
