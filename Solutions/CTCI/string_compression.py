# https://leetcode.com/problems/string-compression/

# O(n) time | O(n) space --> strings in python are immutable
def stringCompression(s):
    compressedString = []
    cur = s[0]
    counter = 1
    for l in s[1:]:
        if l == cur:
            counter += 1
        else:
            compressedString.append(cur)
            compressedString.append(str(counter))
            cur = l 
            counter = 1
    compressedString.append(cur)
    compressedString.append(str(counter))
    compressedString = "".join(compressedString)

    if len(compressedString) < len(s):
        return compressedString
    else:
        return s


test_1 = 'aaaabbccdd'
test_2 = 'aabcd'

print(stringCompression(test_1))
print(stringCompression(test_2))