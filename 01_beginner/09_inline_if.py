# * sometimes called Ternary operator
score = 89
print("A" if score >= 90 else "F")  # we can use this inside print directly, which the classical one will not work

grade = "A" if score >= 90 else "B" if score >= 80 else "C" #! we can't use elif, but we can use else to get same res.
print(grade)

#? We use inline if for quick stuff, but for complex statements it is recommended to use classical if

# ! MATCH - CASE -- modern way // can be used only for matching values
# * evaluate a value against multiple values

country = "United Kingdom"
# if country == "United Kingdom":
#     print("UK")
# elif country == "Italy":
#     print("It")
# elif country == "Germany":
#     print("Ger")
# elif country == "France":
#     print("Fr")
# else:
#     print("Unknown")      # normal conditions

match country:
    case "United Kingdom":
        print("US")
    case "Italy":
        print("It")
    case "France":
        print("Fr")
    case _:                 # * for default use _
        print("other")
