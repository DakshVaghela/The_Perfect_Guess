import random 
n=random.randint(1,100)
cou=1
a=-1
while(a!=n):
    a=int(input("Guess the number: "))
    if(a<n):
        print("Go Higher")
        cou+=1
    elif(a>n):
        print("Go Lower")
        cou+=1
print(f"You have guessed the number {n} correctly in {cou} attempts")