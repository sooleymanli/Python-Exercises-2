
# 41
# Daxilən edilən viza (30%), fərdi fəaliyyət(20%) və final(50%) balına görə tələbənin dərsi keçib-keçmədiyini print etdirin

a=int(input("1. Qimət daxil edin: "))*0.3
b=int(input("2. Qimət daxil edin: "))*0.2
c=int(input("3. Qimət daxil edin: "))*0.5

if (a+b+c)>50:
    print("Imtahandan keçdiniz  {}".format(a+b+c))
else:
    print("Kəsildiniz")
    