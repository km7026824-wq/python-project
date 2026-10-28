import random
def spin_row() :
    your_emoji =["❤" , "🌹" , "🔴"]
    result=[]
    
    for emoji in range(3) :
        result.append(random.choice(your_emoji))
    return result    
        
def print_row(row) :
    print(" | ".join(row))

def get_payout(row , bet) :
    if row[0] == row[1] == row[2] :
       if row[0] == "❤" :
           return bet + 10
       elif row[0] == "🌹" :
           return bet + 20
       elif row[0] == "🔴" :
           return bet * 4
    return 0     

def main() :
    balance = 100
    print(" ##### hello in python slot ##### ")
    print(" ##### your emoji : ❤ 🌹 🔴 ####")
    
    while balance > 0 :
        print(f"your balance is : {balance : .2f}")
        bet = input("enter your money to play : ")
        if not bet.isdigit() :
            print("please inter your number")
            continue
        bet =int(bet)
        if bet > balance :
            print("that is not allow !!")
            continue
        if bet <= 0 :
            print("that is negative !!")
            continue
        balance = balance - bet  
        row = spin_row()
        print("spining .....")    
        print_row(row)  
        payout = get_payout(row , bet)
        
        if payout > 0 :
            print(f"you are win ${payout}")
        else :
            print("good luck")   
        balance = balance + payout    
    
if __name__ =="__main__" :
    main()    