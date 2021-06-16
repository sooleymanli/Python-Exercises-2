# 29
# Tərəfləri daxil edilmiş üçbucağın növü müəyyənləşdirilməlidir.
# Bərabərtərəflidirsə ekrana 1, 
# Bərabəryanlıdırsa ekrana 2, 
# Müxtəliftərəflidirsə ekrana 3 yazıslın. 
# Tək sətirdə boşluqla ayrılmış şəkildə 3 tərəf daxil edilir və nəticə ekrana yazdırılır.

ededler = input("Tərəfləri daxil edin: (Boşluqla ayırın)  ")
x=ededler.split()
if x[0]==x[1]==x[2]:
    print(1)
elif x[0]==x[1] or x[0]==x[2] or x[1]==x[2]:
    print(2)
else:
    print(3)   