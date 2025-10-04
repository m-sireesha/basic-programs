
def is_palindrome(s):
    s = s.lower()  # optional: ignore case
    start = 0
    end = len(s) - 1
    while start < end:
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1
    return True

# Example
text = "Madam"
print(text, "is palindrome?", is_palindrome(text))
