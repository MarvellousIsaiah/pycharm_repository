def count_letters_and_digits(sentence):
    letters = 0
    digits = 0
    for char in sentence:
        if char.isalpha():
            letters += 1
        elif char.isdigit():
            digits += 1
    return letters, digits

# def main():
# sentence = input("Enter a sentence: ")
# letter_count, digit_count = ("count_letters_and_digits(sentence)")
# print("Number of letters:", letter_count)
