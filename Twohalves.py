s = input()
x = len(s)
y = (x//2 + x % 2)

print(s[y:] + s[:y])
