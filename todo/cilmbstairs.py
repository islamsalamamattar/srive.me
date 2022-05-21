n = int(input("no of steps:   "))
def climbstairs(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    else:
        return climbstairs(n-1) + climbstairs(n-2)

print(climbstairs(n))
