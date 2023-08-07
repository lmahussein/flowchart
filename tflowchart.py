Name = input("Full Name")
Number = input("Mobile Number")
YearOfBirth = input("Year Of Birth ")
YearOfBirth = int(YearOfBirth)
CurrentYear = 2023
Age = CurrentYear - YearOfBirth
print(Name)
print(Age)
Number = Number.replace(Number[3:11],"*-****-***")
print(Number.split("-"))
