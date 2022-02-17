n = int(input())
print(bin(n)[2:])
print(oct(n)[2:])
print(hex(n)[2:].upper())

def test_substring(full_string, substring):
    assert substring in full_string, \
    f"expected '{substring}' to be substring of '{full_string}'"

def test_substring1(full_string, substring):
    if substring in full_string:
        print(f"expected '{substring}' to be substring of '{full_string}'")