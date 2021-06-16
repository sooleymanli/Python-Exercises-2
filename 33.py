# 33
# Daxil edilən n ədədinin bütün müsbət bölənlərini print etdirin.
n = int(input("Ədəd daxil edin:  "))
for i in range(1,n+1):
    if n%i==0:
       print(i)
       