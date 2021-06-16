# 30
# Tək sətirdə 3 ədəd daxil edilir və ən böyük və ən kiçiyin hesablanması üçün
# köməkçi funksyalardan istifadə etməklə min( max(x, y), max(y, z), x+y+z)-i müəyyənləşdirin.
# Nətcə vergüldən sonra 2 rəqəm dəqiqliklə ekrana yazdırılsın. 

ededler = input("Tərəfləri daxil edin: (Boşluqla ayırın)  ")
a=ededler.split()
x=float(a[0])
y=float(a[1])
z=float(a[2])
new_number=min(max(x, y),max(y,z),x+y+z)
print("{:.2f}".format(new_number))
                   