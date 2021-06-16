#47
# İstifadəçi bir ədəd daxil etsin bu bu ədəddən 1-ə qədər olan ədədlərin cəmini tapan rekursiv funksiya yazın.
input1=int(input("Reqem daxil edin: "))
def total(e):
    cem=0
    for i in range(1,e):
        cem=cem+i
    print("Reqemlerin cemi: {}".format(cem))
total(input1)
