name = input("what's your name?>>")
print("hy, {} welcome to the treasure hunt !!".format(name))
age = int(input("what's your age?"))
if age > 30:
    print("you are too old to play this game :/")
    exit()
elif age < 10:
    print("you are too young to play this game :/")
    exit()
else:
    print("great you can play the game")

health = 1


agree = input(">>Do you wanna play ? <>")
if agree == "yes":
    print('''
>>Great, lets start the game ;)
you have {} healths'''.format(health))



    q1 = input('''
>> You have two ways (left/right),
what do you choose?? ''')

    if q1 == "left":
        box = input('''
you have found a box typ (open)
to open ''')
        health += 1
        print('''
congrats {} you have got 1 more health life,
your total health is {}'''.format(name,health))


        q2 = input('''
>> Now you can go up towards hill or try to cross the
river, What do you chose(hill/river)''')

        if q2 == "hill":
            health -= 1
            print('''
unfortunately, you have slipped form hill,
your current health is {}'''.format(health))


            q3 = input('''
>> By climbing up at top of the hill, you met an
old man, and when you show him map he said its
the wrong way for your destiny, old man offered
you help, would you follow old man??(yes/no) ''')
            if q3 == "yes":
                health -= 1
                print('''
>>The old man was witch, you again lost your 1
health, current health {}'''.format(health))
                print("GAME OVER !!")
                exit()

            elif q3 == "no":
                print('''
>>Congrats you have found 1000 yrs old
treasure, by {} healths'''.format(health))

        elif q2 == "river":
            health -= 1
            print('''
>>Unfortunately, you have been eaten by a shark,
your current health is {}'''.format(health))
            q4 = input('''
>> You have now reached river bank and you saw some
huts , you felt hungry you can smell some good food
cooking, would you go to then and take help?
(yes/no) ''')

            if q4 == "yes":
                health -= 1
                print('''
unfortunately, those tribal peoples were man
eaters you were cooked next morning, your current health is {}'''.format(health))
                print("GAME OVER !!")
                exit()


            elif q4 == "no":
                print('''
congrats, {} you just found 1000 yrs old treasure with {} health'''.format(name,health))



    elif q1 =="right":
        health -= 1
        print('''
>>Opps, {} you have been caught by a group
of aggressive hippos, your current health is {} '''.format(name,health))
        print("GAME OVER!!")
        exit()
elif agree == "no":
    print("No prob dude")
    exit()

