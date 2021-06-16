#24
#3 ədəd daxil  edin ortancılı print etsin.
a=int(input("Birinci ədədi daxil edin: "))
b=int(input("İkinci ədədi daxil edin: "))
c=int(input("Üçüncü ədədi daxil edin: "))

if a>b and a<c:
    average_number=a
elif b>a and b<c:
    average_number=b
elif c>a and c<b:
    average_number=c

print("Ortancıl ədəd: {}".format(average_number))