# 1
temp = 38
f_temp = temp * 1.8 + 32

temp = f_temp

print(temp)

x = 9.5
y = 6
x = x + y
print(x)

x = 6
x += x - x
print(x)

print(4 * --------8)
# 8 = students
print((((3 ** 6))))

print(-(-(-(-(9)))))


# print(3+=5/2)

# abs

def abs_diff(a, b):
    return abs(a - b)


print(abs_diff(-3, -7))


def avg_grade(g1, g2, g3):
    return (g1 + g2 + g3) / 3


print(avg_grade(100, 50, 30))


def avg_top_3(g1, g2, g3, g4):
    list = [g1, g2, g3, g4]
    list.sort()
    # print(list)
    top_3 = list[1:]
    return avg_grade(top_3[0], top_3[1], top_3[2])


print(avg_top_3(40, 20, 30, 40))

x = 4
y = 11.5

print("The rabbit is ", x, ".")
print("The rabbit is ", x, " years old.")
print(str(y) + " is average")

# num = input("Enter a float number:")
# print(num)

pH = float(input("Enter pH level: "))
if pH < 4.0:
    print("Strong Acid")
elif pH < 7.0:
    print("Acidic")
