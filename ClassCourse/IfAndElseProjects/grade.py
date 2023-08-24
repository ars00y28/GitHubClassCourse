grade = int(input("enter your grade"))

if grade >=90 and grade <=100:
    print("a+")
elif grade >=80 and grade <90:
    print("a")
elif grade >=70 and grade <80:
    print("b+")
elif grade >= 60 and grade<70:
    print("b")
elif grade >=50 and grade <60:
    print("c+")
elif grade >=40 and grade<50:
    print("c")
else:
    print("fail")
