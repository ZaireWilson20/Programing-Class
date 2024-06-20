# Sarina Canelake
# height_example.py

# Problem Statement:
# If you're taller than 56", you can ride Space Mountain at Disneyland.
# If you're shorter, you cannot.
# Additionally if you are greater than 150 inches, you are super tall and
#  deserve a witty message.
'''
# Get user's height
height = int(input("How tall are you? "))
weight = int(input("How much do you weigh? "))
healthyBmi = 4


actualBMI = abs(height - weight)

# Do this if statement first
if height > 150 or weight > 200:
    print("wow you a big mf!")
elif actualBMI > healthyBmi:
    print("you don't meet america's standards")
else: 
    print("thanks for being normal")

if not(height > 150 or actualBMI > healthyBmi):
    print("wow you a big mf!")

if actualBMI > healthyBmi:
    print("you don't meet america's standards")



while(weight > 160):
    if(weight >= 160):
        answer = input("do you want to work out ")
        if answer == "yes":
            weight -= 10
            print("Nice, after working out, you now weigh " + str(weight))
        else:
            print("ok u fat fk, idgaf about you anymore")
    elif (weight == 163):
        print("Aight you can get out early")
        break
'''

# [1,2,3,4,5,6,7,8,9]
boobookaka = ["boo", "boo", 1, 2 , 3, "ka"]
startCountDown = 3
endCountDown = 1
for i in range(endCountDown, startCountDown):
    print("step " + str(i))



i = 0 
while(i < 10):
    print(i)
    i = i + 1

print("good job on finally caring about yourself")


# Do this one second - so people who are tall get the witty message
#  AND get permission to ride the ride
'''
if height >= 56:
    print("ok")

else:
    print("too short")
'''
