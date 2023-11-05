s = "A man, a plan, a canal: Panama"
s = ''.join(c.lower() for c in s if c.isalnum())
is_palindrome = s == s[::-1]
print(is_palindrome)
