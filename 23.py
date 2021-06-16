# 23
# Bir ədəd daxil edin və rəqəmlərinin sayını print etdirin.
new_number=int(input("Ədəd daxil edin:"))
number_times = 1
while new_number >=10:
    new_number=new_number//10
    number_times=number_times+1

print("Rəqəmlərin sayı: {}".format(number_times))