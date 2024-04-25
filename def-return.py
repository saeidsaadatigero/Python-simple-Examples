def display_letters(word):
    result = ' '.join(letter.lower() for letter in word)
    return result

# استفاده از تابع
user_input = input("لطفا یک کلمه وارد کنید: ")
output = display_letters(user_input)
print(output)
