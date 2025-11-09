which=input("What are you want to encoding"
            "(text or number or picture)? ")
if which=="picture":
    palette=str(input("Enter your palette(RGB, CMYK, HighColor, Monochrome or your own palette): "))
    length=int(input("Enter the legth of picture(pixsel): "))
    width=int(input("Enter the width of picture(pixsel): "))
    area=length*width

    if palette=="RGB":
        n=24
        last=area*n
        print(last,"bit") 
    elif palette=="CMYK":
        n=32
        last=area*n
        print(last,"bit")
    elif palette=="HighColor":
        n=8
        last=area*n
        print(last,"bit")
    elif palette=="Monochrome":
        n=1
        last=area*n
        print(last,"bit")
    else:
        n=0
        palette=int(palette)
        while 2**n<palette:
            n+=1
        last=area*n
        print(last,"bit")

        


elif which=="number":
    dig=input("Enter a number: ")
    base=int(input("Enter the base of your number: "))
    n=0
    last=0
    while 2**n <base:
        n+=1

    def counting (dig):
        if len(dig)==0:
            return 0
        num=0
        if isinstance(dig, int):
            dig=abs(dig)
            while dig >0:
                dig//=10
                num+=1
            last=num*n
            return last
        else:
            last=len(dig)*n
            return last
    print(counting(dig),"bit")  

else:
    text=str(input("Enter a text: "))
    power=input("Enter number of letters in the alphabet or which timetable you use(ASCII , UNICODE): ")
    n=0
    if power.isdigit():
        while 2**n<int(power):
            n+=1
        last=len(text)*n
        print(last,"bit")
    else:
        match str(power):
            case "ASCII":
                last=len(text)*8
            case "UNICODE":
                last=len(text)*16
        print(last,"bit")

def measure1 (measure ,last):
    match measure:
        case "b":
            last=last//8
            return last,"b"
        case "Kb":
            last=last//pow(2,13)
            return last,"Kb"
        case "Mb":
            last=last//pow(2,23)
            return last,"Mb"
        case "Gb":
            last=last//pow(2,33)
            return last,"Gb"
        case "Tb":
            last=last//pow(2,43)
            return last,"Tb"
        
yesno=input("Do you want it in another measure? ")
if yesno=="yes":
    measure=input("Which one(b , Kb ... Tb)? ")
    result, unit = measure1(measure, last)
    print(result, unit)
