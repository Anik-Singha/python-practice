#TODO

#! No Value
# NoneType -- None

#? Singl Value
'''
    NUMERIC
        1.INT     15
        2.FLOAT   3.5
        3.COMPLEX 3 + 5j

    4. STR (string) eg - 'hello'
    5. BOOL (true or false)
    6. DATE & TIME 
        - date 2026-12-25
        - time 18:05:47
        - datetime 2026-12-25 18:05:47
    
    MULTI - VALUES
        7.LIST [1,2,3]
        8. TUPULE (1,2,3)
        9. SET {1,2,3}
        10. DICT {'A':1,'B':2}
        11. ARRAY ('I','[10,20])
'''

age = 25
height = 165.9
name = 'Anik'
student = True
novalue = None
stu_properties = [age,height,name,student,novalue]
for i in stu_properties:
    print('The value is ',i,type(i))