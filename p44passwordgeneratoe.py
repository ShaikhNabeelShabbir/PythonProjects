#random password genrator
import random
gen=[]
def random_password(n):
        password =["A","B","C","D","E","F","G","H","I","J","K","L","M","N",
                   "O","P","Q",
                   "R","S","T","U","V","W","X","Y","Z","0","1","2","3","4","5",
                   "6","7","8","9",
                   "a","b","c","d","e","f","g","h","i","j","k",
                   "l","m","n","o","p",
                   "q","s","t","u","v","w","x","y","z",
                   ]
        
        for i in range(0,n):
                rand_int = random.randint(0, len(password)-1)
                random_pass = password[rand_int]
                #print(random_pass)
                gen.append(random_pass)
                
        for g in gen:
                print(g,end=' ')
        
        

X=int(input("how many dgit password you want to generate\n"))
print("your generated password")
random_password(X)