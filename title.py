# a = input()
# if a == a.title():
#     print("YES")
# else:
#     print("NO")


# a = input()
# print(a.swapcase())

# s = input()
# word = "хорош"
# if word in s.lower():
#     print("YES")
# else:
#     print("NO")

# s = input()
# count = 0
# for i in range(len(s)):
#     if s[i].islower():
#         count+=1
# print(count)
#
# s = input()
# print(s.count(" ") + 1)

# genetic = input()
# a = genetic.count("А") + genetic.count("а")
# g = genetic.count("Г") + genetic.count("г")
# c = genetic.count("Ц") + genetic.count("ц")
# t = genetic.count("Т") + genetic.count("т")
# print(f"Аденин: {a}\nГуанин: {g}\nЦитозин: {c}\nТимин: {t}")


# n = int(input())
# count = 0
# for i in range(n):
#     n = input()
#     if n.count("11") >= 3:
#         count += 1
# print(count)


# n = input()
# count = 0
# for i in range(10):
#     count += n.count(str(i))
# print(count)


# n = input()
# if n.endswith(".com") == True or n.endswith(".ru") == True:
#     print("YES")
# else:
#     print("NO")

# s = input()
# a = 0
# b = 0
# for i in s:
#     if s.count(i) >= a:
#         a = s.count(i)
#         b = i
# print(b)

# s = input()
# if s.count("f") == 1:
#     print(s.find("f"))
# elif s.count("f") >= 2:
#     print(s.find("f"), s.rfind("f"))
# else:
#     print("NO")

# s = input()
# first = s.find("h")
# second = s.rfind("h")
# print(s[:first] + s[(second+1):])


# a, b = int(input()), int(input())
# for i in range(a, b + 1):
#     print(chr(i), end=' ')

# s = input()
# for i in s:
#     print(ord(i[::]), end=" ")


# n = int(input())
# c = input()
# for n in c:
#     print(chr(n), end=" ")

# s = input()
# print(s.replace("@", ""))

# s = input()
# if s.count("f") == 1:
#     print(-1)
# elif s.count("f") == 0:
#     print(-2)
# else:
#     s = s.replace("f", "k", 1)
#     print(s.find("f"))

'''Списки, срезы'''
# char = int(input())
# a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# print(a[:char])


# fruits = ['apple', 'apricot', 'banana', 'cherry', 'kiwi', 'lemon', 'mango']
# fruits[2:5] = ['банан', 'вишня', 'киви']
# print(fruits)

# evens = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
# average = sum(evens)/len(evens)
# print(average)


# rainbow = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
# rainbow[3] = "Зеленый"
# rainbow[-1] = "Фиолетовый"
# print(rainbow)
#
# languages = ['Chinese', 'Spanish', 'English', 'Hindi', 'Arabic', 'Bengali', 'Portuguese', 'Russian', 'Japanese', 'Lahnda']
# print(languages[::-1])


# numbers1 = [1, 2, 3]
# numbers2 = [6]
# numbers3 = [7, 8, 9, 10, 11, 12, 13]
#
# print((numbers1 + numbers1) + (numbers2 * 9) + numbers3)


# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# del numbers[::2]
#
# print(numbers)

# numbers = [2, 6, 3, 14, 10, 4, 11, 16, 12, 5, 4, 16, 1, 0, 8, 16, 10, 10, 8, 5, 1, 11, 10, 10, 12, 0, 0, 6, 14, 8, 2, 12, 14, 5, 6, 12, 1, 2, 10, 14, 9, 1, 15, 1, 2, 14, 16, 6, 7, 5]
# print(len(numbers), numbers[-1], numbers[::-1], sep="\n")
# if 5 and 17 in numbers:
#     print("YES")
# else:
#     print("NO")
# print(numbers[1:-1])


# n = int(input())
# s = []
# for i in range(n):
#    s += [input()]
# print(s)

# s = []
# for i in range(26):
#     s.append(chr(ord('a') + i) * (i + 1))
# print(s)


# n = int(input())
# s = []
# for i in range(n):
#     s += [int(input())**3]
# print(s)


# n = int(input())
# s = []
# for i in range(1, n + 1):
#     if n % i == 0:
#         s.append(i)
# print(s)

# x, n = int(input()), int(input())
# s = []
# for i in range(x - 1):
#     n1 = int(input())
#     s.append(n + n1)
#     n = n1
# print(s)


# n = int(input())
# s = []
# for i in range(n):
#     x = int(input())
#     s.append(x)
# del s[1::2]
# print(s)


# n = int(input())
# s = []
# for i in range(n):
#     s.append(input())
# k = int(input())
# al = ''
# for j in s:
#     if len(j) >= k:
#         al += j[k - 1]
# print(al)


# n = int(input())
# s = []
# for i in range(n):
#     s.extend(input())
# print(s)


# body = ['Вода', 'Мышцы', 'Жир']
# body.remove('Жир')
# print(body)

# n = int(input())
# s = []
# for i in range(n):
#     s.append(int(input()))
# for j in s:
#     if j != min(s) and j != max(s):
#         print(j)

# n = int(input())
# sp = []
# for i in range(n):
#     x = input()
#     if x not in sp:
#         sp.append(x)
#         print(x)

# n = [input()
# for x in range(int(input()))]
# x = input().lower()
# for i in n:
#     if x in i.lower():
#         print(i)


# s = [input() for _ in range(int(input()))]
# d = [input() for _ in range(int(input()))]
# for i in s:
#     for j in d:
#         if j.lower() not in i.lower():
#             break
#     else:
#         print(i)


# n = int(input())
# x = [int(input()) for i in range(n)]
# [print(j) for j in x if j < 0]
# [print(j) for j in x if j == 0]
# [print(j) for j in x if j > 0]

# s = input().split()
# print(*s, sep="\n")

# fio = input()
# print(".".join([i[0] for i in fio.split(" ")]) + '.')

# n = input()
# print(*(n.split('\\')), sep='\n')

# n = input().split()
# for i in n:
#     print("+" * int(i))

# s = input().split('.')
# for i in s:
#     if int(i) < 0 or int(i) > 255:
#         print('НЕТ')
#         break
# else:
#     print('ДА')

# s = input()
# print(*s, sep=input())
