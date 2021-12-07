word = input()
count = word
if word[::-1] == count[::1]:
    print("yes")
else:
    print("no")

