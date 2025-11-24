def output(maxsub1,minsub1,day1,mins,subjects):
    if len(subjects) == 1:
        print(f"you studied {maxsub1} for {day1} minutes today")
    else:
        print(f"you studied {maxsub1} the most and {minsub1} the least and you studied for a total {day1} minutes today")
