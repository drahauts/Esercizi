def is_palindrome(x: int) -> bool:
    s: str = str(x)
    i: int = 0
    while i < len(s):
        j = len(s) - (i + 1)
        if s[i] != s[j]:
            return False
        i += 1
    return True

x = input()
print(is_palindrome(x))