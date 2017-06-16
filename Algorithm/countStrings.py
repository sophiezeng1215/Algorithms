# 是input一组string，逗号相隔，数有多少个不同的string，大小写忽略，标点符号啥的不忽略 

strings = input().strip().split(', ')
def countStrings(strings):
    count = {}
    strings = map(str.lower, strings)
    for string in strings:
        if string in count:
            count[string] += 1
        else:
            count[string] = 1
    return len(count)
print(countStrings(strings))
