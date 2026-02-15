person = ['Raj','Data Analyst',25,'India']
name, role, age, place = person         # ! Python unpacking // list of variables seperated with a comma

print(role)     # out : Data Analyst

# ? Rest collector (*)
# * asterisk collects leftover value, so its fine if there is nothing, it will create empty list
name, *details, place = person
print(details)      # out : ['Data Analyst', 25]

name, *details = person
print(details)      # out : ['Data Analyst', 25, 'India']

#! underscore (_) // to skip the indexes we dont need to store
new_name, _ , new_age, _ = person
print(new_name)

# ? we can also use name, *_ = person // *_ will discard everything after name