#44
# N natural ədədi verilmişdir. Həmin ədəddə tək rəqəmlərin sayını tapın. (0 tək ədəd sayılmır)
n=input("Ədəd daxil edin:  ")
new_list=[]
for i in range(0,len(n)):
    if n[i].isnumeric()==True: 
        number = int(n[i])
        new_list.append(number)
tek_eded_say=0
tek_eded_list=[]         
for j in range(0,len(new_list)):
    if new_list[j]%2!=0:
        tek_eded_say=tek_eded_say+1
        tek_eded_list.append(new_list[j])       
print(f"""
       Daxil etdiyiniz ədəd: {n}
       Ədəddəki tək rəqəmlər: {tek_eded_list}
       Tək ədədlərin sayı: {tek_eded_say}
       """)
       
       