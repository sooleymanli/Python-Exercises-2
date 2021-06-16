

# 34
# Daxil edilən n ədədin mükəmməl olub olmadığını print edin.
# Ədənin özü xaric müsbət bölənlərinin cəmi özünə bərabərdirsə belə ədədə mükəmməl ədəd deyilir.
# Məsələn, 1,2 və 3    6-nin bölənləridir cəmləri də 6-ya bərabərdir. 
n = int(input("Ədəd daxil edin:  "))
m=0
for i in range(1,n):
    if n%i==0:
       m=m+i
       
if m==n:
    print("Mükəmməl ədəddir")
else:
    print("Mükəmməl ədəd deyil")
    
    