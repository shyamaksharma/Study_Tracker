def day():
    sbj = input("Which Subject did you study today? ")
    minu = int(input(f"How many minutes did you study {sbj} today? "))
    subjects = []
    mins = []
    subjects.append(sbj)
    mins.append(minu)
    a = input("Did you study anything else? (Y/N) ")
    if a.lower() in ["yes","y","yep"]:
        b = int(input("How many other subjects did you study? "))
        for i in range (0,b):
            sbj2 = input("What else did you study? ")
            hrs2 = int(input(f"How long did you study {sbj2} for? "))
            subjects.append(sbj2)
            mins.append(hrs2)
    return subjects, mins