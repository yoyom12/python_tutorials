questions =  [
    ["whih os systm i am using","winowa","ma","linux","ops",1],
    ["whih os systm i am using","winowa","ma","linux","ops",1],
    ["whih os systm i am using","winowa","ma","linux","ops",1],
    ["whih os systm i am using","winowa","ma","linux","ops",1]
]

levels = [1000,2000,3000,5000,10000,20000,40000,100000,150000,250000,500000,1000000]
money = 0
for i in range(0, len(questions)):
    print("the question is",questions[i][0])
    print(f"1. {questions[i][1]}   2. {questions[i][1]}")
    print(f"3. {questions[i][3]}   4. {questions[i][4]}")
    rply = int(input("ntr th option"))
    if(rply == questions[i][-1]):
        print(f"you win lvl {i+1} for Rs {levels[i]} \n ")
        if ((i+1)==1):
            money = 1000
            
        elif ((i+1)==4):
            money = 11000
        
    else:
        print("you ANS is wrong\n")
        break

print(f"you win {money}")