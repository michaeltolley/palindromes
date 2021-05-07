def is_palindrome(word):
    reversed_word = word[::-1]
    if word == reversed_word:
        return True
    else:
        return False

print("This is palindrome checker.")
user_input = input("Enter something: ")

if is_palindrome(user_input):
    print("Yes, that is a palindrome")
else:
    print("No, that is not a palindrome")