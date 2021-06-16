# 32    
# n ədədi daxil edilir və ən böyük rəqəmini ekrana yazdırın.
a = int(input("Ədəd daxil edin: "))
a_copy=a
list=[]
while a>=10:
    list.append(a%10)
    a=a//10
list.append(a)

c = list[0]

for i in list:
    if i>c:
        c=i
print("""
      Daxil etdiyiniz ədəd: {}
      Ən böyük rəqəm: {}""".format(a_copy,c))       