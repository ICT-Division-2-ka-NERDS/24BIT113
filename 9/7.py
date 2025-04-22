def ispalindrome(text):
    text = text.lower()
    text = text.replace(" ", "")
    if text == text[::-1]:
        return True
    else:
        return False

print(ispalindrome("nurses run"))
print(ispalindrome("hello"))
