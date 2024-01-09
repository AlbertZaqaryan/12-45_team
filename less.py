# def func(n):

#     if n == 11:
#         return '11'
#     else:
#         return func(n // 2) + str(n % 2)

# print(func(23))
# -------------------------------------------------
# i = 1
# value = 0
# while i < 32:
#     for j in range(1,i):
#         value = value + 1
#     i = i * 2
#     print(value)
# -------------------------------------------------

# print(round(0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1))
# -------------------------------------------------

# print(5 >> 2)

# print(bin(5))
# -------------------------------------------------


# path = "C:\\Users\\User\\Desktop\\jenkins\\linux1.pem"
# -------------------------------------------------

# with open(path, 'rb') as file:
#     res = file.read()
# print(res)
# -------------------------------------------------

# import os


# os.mkdir('THISISZAVIVKA')

# os.rmdir('ZAVIVKA')


# print(os.system('dir'))

# res = os.listdir()
# print(res)
# -------------------------------------------------

# import sys

# print(f'Im anunn e {sys.argv[1]}\nes unem {sys.argv[2]} boyi jutak')
# -------------------------------------------------


# def func(word, text):
#     return text.count(word)
# print(func('o', 'Hello Rafooo'))
# -------------------------------------------------

# def func(text):
#     count = 0
#     for i in text:
#         if i in 'aeiou':
#             count += 1
# -------------------------------------------------


# with open('myfile.txt', 'r') as file:
#     res = file.read()
# res = res.split('\n')
# x = {i:res.count(i) for i in res}
# with open('x.txt', 'a') as file:
#     for i in x:
#         file.write(f'{i} -- {x[i]}\n')
# -------------------------------------------------

for i in range(10):
  print("My name is EDO")
