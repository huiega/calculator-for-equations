print("Добро пожаловать в мой калькулятор по вычислению корней уравнений с трёхчленом!")
print("Пожалуйста, введите значения a,b,c как в уравнении ax^2+-bx+-c")
a = float(input("Значение переменной a:"))
b = float(input("Значение переменной b:"))
c = float(input("Значение переменной c:"))
if a == float(0):
    a = float(input('давай по-новой, а = '))
elif b == float(0):
    b = float(input('давай по-новой, b = '))
elif c == float(0):
    c = float(input('давай по-новой, c = '))
else:
    print('')
D = (b ** (2)) - (4 * a * c)
if D == float(0):
        print("Здесь только один корень", f"x1 = {(-b + D ** (0.5)) / (2 * a):.3f}")
elif D < float(0):
    print("Сори, корней нет")
else:
    sqrt: float = D ** (0.5)
    x1 = (-b + sqrt) / (2 * a)
    x2 = (-b - sqrt) / (2 * a)
    print("Ответ: ", f"x1 = {x1:.3f}", f"x2 = {x2:.3f}")


# print('try again')
# print("Добро пожаловать в мой калькулятор по вычислению корней уравнений с трёхчленом!")
# print("Пожалуйста, введите значения a,b,c как в уравнении ax^2+-bx+-c")
#
# a = float(input("Значение переменной a:"))
# b = float(input("Значение переменной b:"))
# c = float(input("Значение переменной c:"))
#
# while a != 0 or b != 0 or c != 0:
#     D = (b ** (2)) - (4 * a * c)
#     if D == float(0):
#         print("Здесь только один корень", f"x1 = {(-b + D ** (0.5)) / (2 * a):.3f}")
#     elif D < float(0):
#         print("Сори, корней нет")
#     else:
#         sqrt: float = D ** (0.5)
#         x1 = (-b + sqrt) / (2 * a)
#         x2 = (-b - sqrt) / (2 * a)
#         print("Ответ: ", f"x1 = {x1:.3f}", f"x2 = {x2:.3f}")
# else:
#     print('try again')
#     a = float(input("Значение переменной a:"))
#     b = float(input("Значение переменной b:"))
#     c = float(input("Значение переменной c:"))