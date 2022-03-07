#formula for farenheiht is (0°C × 9/5) + 32 = 32°F


# temp = input("enter your temperature in celcius: ").strip()
# if str.isdigit(temp):
#     temp = int(temp)
#     temp_fh = (temp * 9/5) + 32
#     print(int(temp_fh), "°F")
# else:
#     print("only numbers")

#---------------------------------------------------------------

# speed = input("enter your speed in mph: ").strip()
# if str.isdigit(speed):
#     speed = float(speed)
#     speed_km = speed * 1.609
#     print(float(speed_km), "kmph")
# else:
#     print("only numbers")

#---------------------------------------------------------------

# weight = input("enter your weight on earth: ").strip()
# if str.isdigit(weight):
#     weight = float(weight)
#     weight_moon = (weight / 100) * 16.5
#     print(float(weight_moon))
# else:
#     print("only numbers")

#---------------------------------------------------------------

# weight = input("enter your weight: ").strip()
# height = input("enter your height in cm: ").strip()
# if str.isdigit(weight):
#     weight = float(weight)
#     if str.isdigit(height):
#         height = float(height)
#         height = (height / 100)
#         height_sq = height * height
#         BMI = weight / height_sq
#         print("your BMI is", float(BMI))
#         if BMI >= 18.5 and BMI < 25:
#             (print("you are healthy"))
#         else:
#             (print("ur gonna die soon m8"))
# else:
#     print("only numbers")

#-------------------------------------------------------

# fine = 0
# speed = input("perp speed: ").strip()
# if str.isdigit(speed):
#     speed = int(speed)
#     if speed >= 120:
#         fine = ((speed - 100) * 5) + 250
#     if speed > 100 and speed < 120:
#         fine = ((speed - 100) * 5) + 50
#     print(float(fine))
# else:
#     print("only numbers")

#------------------------------------------------------

# value = input("enter the year(1982 - 2048): ").strip()
# value = int(value)
# a = value % 19
# b = value % 4
# c = value % 7
# d = (19 * a + 24) % 30
# e = (2 * b + 4 * c + 6 * d) % 7
# date = 22 + d +e
# if date >= 44 or date <= 31:
#     print("date invalid")
# else:
#     print("valid date easter is", date)

#-------------------------------------------------------

# year = input("is your year a leap one? enter the year: ").strip()
# if year.isdigit():
#     year = float(year)
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 print("it is")
#             else:
#                 print("its not")
#         else:
#             print("it is")
#     else:
#         print("its not")
# else:
#     print("only numbers")

#-------------------------------------------------------

date = input("enter date dd/mm/yy: ").strip()
a = int(date[0:2]) * int(date[3: 5])
b = int(date[6:])
if a == b:
    print("nice, its magic bruv, i knew you'd pick a cool date")
else:
    print("that date sucks man pick a cooler one, maybe a magic one? idk its really up to you")
