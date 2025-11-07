def main():
    time = input("Meal time: ").lower()

    if 7 <= convert(time) <= 8:
        print("breakfast time ")

    elif 12 <= convert(time) <= 13:
        print("lunch time")

    elif 18 <= convert(time) <= 19:
        print("dinner time")

    


def convert(time):

    if (time.endswith(("a.m", "am"))):

        for suffix in (("a.m", "am")):
            if (time.endswith((suffix))):
                time = (time.removesuffix(suffix)).strip()
                break

        
        hours, minutes = time.split(":")
    
        hours = float(hours)
        minutes =float(minutes)

        minutes = round(minutes / 60, 2)
        time = hours + minutes

        if  0 <= time < 12 :
            return time
        else:
            return (time -12)
        

    elif (time.endswith(("p.m", "pm"))):

        for suffix in (("p.m", "pm")):
            if (time.endswith((suffix))):
                time = (time.removesuffix(suffix)).strip()
                break
        
        hours, minutes = time.split(":")
    
        hours = float(hours)

        minutes =float(minutes)

        minutes = round(minutes / 60, 2)
        time = hours + minutes


        if  0 <= time <= 11 :
            return (time +12 )

        else:
            return time
        
    else:
        hours, minutes = time.split(":")
    
        hours = float(hours)
        minutes =float(minutes)

        minutes = round(minutes / 60, 2)
        time = hours + minutes

        return time
        

    

    


if __name__ == "__main__":
    main()