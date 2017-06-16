# input 关于string，给一个string输入，输出每个char出现的次数，包括‘，’，‘！’等。要求和他们出现在string的次序相同

s = input().strip()
def countChar(s):
    count = {}
    seq = []
    for char in s:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
            seq.append(char)
    for char in seq:
        print (char, count[char])
countChar(s)
