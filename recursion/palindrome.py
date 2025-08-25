str = input("Write a string know if its a palindrome: ")
word = str.lower()

def message(string):
    if string == word:
        return f"{word} It's a palindrome."
    else:
        return f"{word} It's not a palindrome."

def palindrome(string):
    if len(string) == 0:
        return string[1:1]
    
    return string[-1] + palindrome(string[:len(string) - 1])

palindrome_str = palindrome(word)

print(message(palindrome_str))