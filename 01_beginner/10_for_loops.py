# ! FOR LOOP
for i in range(5):  # * range(start,stop,step)
    print(i)

# EG
files = ['Report.csv','DATA.csv','final.txt']
for file in files:
    file = file.strip().lower().replace("txt","csv")    # ? Clean first, transform 2nd always execute in this order
    print(file)

# 1. Print 7 times table
num = 7
for i in range(1,11):
    print(f"{num} x {i} = {num*i}")

# 2. print left-aligned star pyramid using 6 rows
n = 6
for i in range(1,n+1):
    star = '*'
    print(star*i)

