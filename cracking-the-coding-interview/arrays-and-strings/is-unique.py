def isUnique(s) -> bool:
    chars = []
    for c in s:
        if c in chars:
            return False
        else:
            chars += [c]
        
    return True

def isUniqueNoDS(s) -> bool:
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            print(s[i], s[j])
            if s[i] is s[j]:
                return False

    return True

print(isUnique("tes"))
print(isUniqueNoDS("tes"))