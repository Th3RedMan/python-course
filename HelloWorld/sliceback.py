import math

letters = "abcdefghijklmnopqrstuvwxyz"

backwards = letters[::-1]
print(backwards)

print(letters[16:13:-1])
print(letters[4::-1])
print(letters[:-9:-1])
print(letters[-4:])
print(letters[-1:])
print(letters[:1])
print(letters[0])   # Not best way in case of crashing use line 11


def is_palindrome(s: str):
    new_string = ""
    for char in s.lower():
        if letters.find(char) != -1:
            new_string += char

    for i in range(0, math.floor(len(new_string))):
        if new_string[i] != new_string[(i + 1) * -1]:
            return False
    return True


print(is_palindrome("Are we not pure? “No, sir!” Panama’s moody Noriega brags. “It is garbage!” Irony dooms a man—a prisoner up to new era."))