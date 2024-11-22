def count_word(string):
    string1=string.strip()
    count = 1
    for i in string1:
        if i ==  " ":
            count += 1
    return count

