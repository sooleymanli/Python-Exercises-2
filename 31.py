
# 31
# Ayın nömrəsi daxil edilir və ilin fəsli ekrana yazdırılır.
a = int(input("Ayın nömrəsini daxil edin:  "))
if a<2 or a==12:
    print("Qış ayıdır")
elif 2<a<6:
    print("Yaz ayıdır")
elif 5<a<9:
    print("Yay ayıdır")
else:
    print("Payız ayıdır")