
def update(string):
    i = j = 0
    while i < len(string):
        j = i
        while j < len(string) and string[i] == string[j]:
            j += 1
        if j - i >= 3:
            string = string[:i] + string[j:]
            i = 0
        else:
            i = j
    return string

print(update("YBYFFFYYBBYY"))