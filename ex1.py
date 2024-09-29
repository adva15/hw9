import random
random_temp: list[float]=[]
temp: float=float(input("enter number:"))
SENTINEL=-999

for _ in range(50):
    if temp == SENTINEL:
        break
    temp: float = random.randint(-50, +50)
    random_temp.append(temp)
print(random_temp)
#c
temp: list[float] = [29.5, -45.3, 36.9, -20.4]
end_Add_temperatures:list[float]=[18.5 ,39.1 -20.0]
print('temp[-29.5, -45.3, 36.9, -20.4] + [18.5 ,39.1 -20.0]) =', temp + [12.5 ,38.1 ,-22.0])
random_temp.extend(end_Add_temperatures)
print(temp.extend([18.5 ,39.1, -20.0]))
print("end Add temp", temp)
#d
#פעולת extend משנה את הרשימה הנוכחית ללא החזרת תשובה נקבל "NONE". היא משנה רק בבטן
# לעומת זאת פעולת ה"+" מחזירה תשובה ותפקידה לחבר בין שתי רשימות שיהיו יחד ולא לחוד
#e
print(f"max value temperature == {max(temp)}")
print(f"min value temperature == {min(temp)}")
#f
temp: list[float] = [29.5, -45.3, 36.9, -20.4]
if 18.5 in temp:
    print('[18.5, 39.1, -20.0].index(18.5):', [18.5, 39.1, -20.0].index(18))
    print('[18.5, 39.1, -20.0].index(18.5):', temp.index(18.5))
print(18.5 in temp)
#g
print('[29.5, -45.3, 36.9, -20.4, 18.5, 39.1, -20.0].count(-20.0):', [29.5, -45.3, 36.9, -20.4, 18.5, 39.1, -20.0].count(-20.0))
#h
print(f"avg == {sum(temp) / len(temp)}")
#i
print(f"for-each letter in 'temp' --> ", end="")
for letter in "temp":
    print(temp, end="  ")
print()
#j
if 39.1 in temp:
    print(temp.index(39.1))
random_temp.append(39.1)
print()

if 39.1 in temp:
    print('[18.5, 39.1, -20.0].index(39.1):', temp.index(39.1))
print(temp.index)
#k
del temp[0]
del temp[: : ]
print('after del temp[0],del temp[: : ]', temp)
#l
del temp[: :2]
print('after del temp[0],del temp[: : ]', temp)
#m
temp:list[float] = [29.5, -45.3, 36.9, -20.4]
print(temp)
temp.remove(18.5)
print('after list1.remove(99)', temp)
#n
tamp_last:list[float]=[]
print(tamp_last)
print('pop -- ', tamp_last.pop())
print('list1 after pop last , pop index last: ', tamp_last)
#o
new_temp:list[float]=[29.5, -45.3, 36.9, -20.4]
tamp_last = new_temp.copy()
print(f"new_list'{new_temp}")
temp.sort()
print('after sort', temp)
print('after sort, save temp', new_temp)
#p
new_temp = temp.copy()
print("temp.copy")
temp.sort()
print('after sort', new_temp)
print('after sort, reverse=True', new_temp)