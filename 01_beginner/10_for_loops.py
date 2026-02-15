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

# ! for-else  -- different from if else, here the else will run after the for loop is completed
# * it is completely useless, for real usage combine with break to check errors

names = ['jone','maria','anik',None,'ram']
for name in names:
    if name is None :
        print("Problem")
        break
    print(name)
else:
    print("All name available")