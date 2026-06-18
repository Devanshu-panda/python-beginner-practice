#Problem_1: string_times
def string_times(str, n):
    word = str
    if n>0:
        for x in range(n-1):
            word += str
        return word
    elif n==0:
        return ""


