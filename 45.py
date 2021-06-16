#45
# İlk 100 ədədin kvadratları cəmi ilə cəmlərinin kvadratı fərqini print etdirin.
sum_list=[]
pow_sum=[]
for i in range(0,101):
    sum_list.append(pow(i,2))
    pow_sum.append(i)
    
total = sum(sum_list)-pow(sum(pow_sum),2)
print(total)