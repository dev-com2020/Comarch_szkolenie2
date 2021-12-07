# height = 7
# z = height - 3
# x = 1
# for i in range(1, (height + height) - 3):
#     if i % 2 != 0:
#         if (i == 1):
#             print('~~' * z + 'o' + '~~' * z)
#         else:
#             print('~~' * z + '* ' * (x - 1) + '*' * 1 + '~~' * z)
#         x += 2
#         z -= 1
# for a in range(height + 1):
#     if a % (height + 1) == 1:
#         test = height - 3
#         print(((test * '~~' + a * '|' + test * '~~') + '\n') * 2)


# for x in range(1, 30, 2):
#     snieg = "~" * ((30 - x) // 2)
#     s = snieg + "#" * x + snieg
#     print(s.center(30))

a = input("Tekst: ")
if a.find("!") >= 0 or a.find("@") >= 0 or a.find("#") >= 0:
    print("Oj!Znak specjalny!")

# print("Witaj!".find("!"))
x = ascii("Mam na imię Tomek")
print(x)