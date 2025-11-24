def daily_calc(subjects, mins):
    day1 = sum(mins)
    index1 = mins.index(max(mins))
    maxsub1 = subjects[index1]
    index2 = mins.index(min(mins))
    minsub1 = subjects[index2]
    return maxsub1, minsub1, day1  