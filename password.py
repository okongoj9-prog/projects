        #password finder
            #  codwSwiftz

import time

password = "1111"

print("Cracking Password....")

for i in range(10000) :
    guess = str(i).zfill(4)
    print("Trying", guess)
    time.sleep(0.05)

    if guess == password:
        print ("password Found  ")
        print("Password is :",guess)
        break