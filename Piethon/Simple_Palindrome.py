def reverse(text):
    return text[::-1]


def is_a_palindrome(text):
    return text == reverse(text)


sample = input("Enter text: ")
if is_a_palindrome(sample):
    print("Yes, it is a palindrome")
else:
    print("No, it is not a palindrome")
