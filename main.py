from Input import day
from output import output
from processing import daily_calc
def main():
    Hdays = int(input("How many days you want to track your studies for? "))
    for z in range(1,Hdays+1):
        print(f"Day {z}")
        subjects, mins = day()
        maxsub1, minsub1, day1 = daily_calc(subjects, mins)
        output(maxsub1, minsub1, day1, mins, subjects)

if __name__=="__main__":
    main()