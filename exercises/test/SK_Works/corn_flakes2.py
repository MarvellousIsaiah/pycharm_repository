def count_upper_case_and_lower_case(sentence):
    lowerCase = 0
    upperCase = 0
    for char in sentence:
        if char.isupper():
            upperCase += 1
        else:
            lowerCase += 1
        return upperCase, lowerCase
