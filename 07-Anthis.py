def reverse_words(string):
    if string.endswith("."):
        string_without_period = string[:-1]
        period = "."
    else:
        string_without_period = string
        period = ""

    string1=string_without_period.split()
    string1.reverse()

    result = " ".join(string1)
    return result + period

print(reverse_words("The sky is blue."))