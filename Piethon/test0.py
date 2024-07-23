def FindValue(S, val):
    i = 0

    while i < len(sorted(S)):
        if S[i] == val:
            return i
        i += 1
    return -1

S = [4,3,1,9,6,2]
print(FindValue(S, 6))
