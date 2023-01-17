#Grade check

gradeInput = int(input("Enter the grade: "))

if gradeInput < 0:
    print("Impossible")
elif gradeInput == 0:
    print("No mark")
elif gradeInput > 0 and gradeInput <= 49:
    print("Fail")
elif gradeInput > 49 and gradeInput <= 59:
    print("1")
elif gradeInput > 59 and gradeInput <= 69:
    print("2")
elif gradeInput > 69 and gradeInput <= 79:
    print("3")
elif gradeInput > 79 and gradeInput <= 89:
    print("4")
elif gradeInput > 89 and gradeInput <= 100:
    print("5")
elif gradeInput > 100:
    print("Incredible")
