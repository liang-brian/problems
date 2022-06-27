# return True if permutation, False if not
def checkPermutation(a, b):
    chars = {}
    for c in a:
        if c in chars.keys():
            chars[c] += 1
        else:
            chars[c] = 1

    for c in b:
        if c in chars.keys():
            chars[c] -= 1
        else:
            return False
    
    for k, v in chars.items():
        if v != 0:
            return False

    return True

print(checkPermutation('asdff', 'fdsa'))
