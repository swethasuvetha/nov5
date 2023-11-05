s = "Im CSE student"
words = [word for word in s.split() if word]
words.reverse()
reversed_str = ' '.join(words)
print(reversed_str)
