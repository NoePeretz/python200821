name = input("What's your name:")
cname = input("What do you want to name your game console:")
score = 0
print ("Hi" ,name,"!" , "Welcome!")
print ("I AM YOUR GAME CONSOLE", cname,"!""THERE IS AN URGENT MATTER WE NEED TO DISCUSS!")

while True:
        print ("PLAYER ONE, GET READY! THIS IS GOING TO BE ONE HECK OF A RIDE!")
        print ("HERE IS A LIST OF ALL THE DIFFERENT GAMEMODES! PLEASE CHOOSE ONE.")
        print ("1. SOLO. GO SOLO AND FACE YOUR DOOM.")
        print ("2. DUO. FRIEND OR NO FRIEND, YOU WILL DIE ANYWAY.")
        print ("3. MULTIPLAYER. CHOOSE THIS IF YOU MUST.")
        print ("4. LEAVE THIS GAME AND REGRET IT.")
        option = input("WHERE WOULD YOU LIKE TO GO:")
        if option == '4':
            break
        while True:
            if option == '3':
                print ("YOU DON'T HAVE THAT MANY FRIENDS.")
                break
            if option == '1':
                print ("SOLO. WONDERFUL...")
                print("LOADING 20%-------LOADING 45%-------LOADING 60%-------")
                n2 = input("CHOOSE A NAME FOR YOUR CHARACTER:")
                print ("Let's start,", n2)
                print ("YOU ARE LITTLE RED RIDING HOOD. Do you A/ Go to grandmother’s house.")
                print ("Or B/ Go to the bar and drink cause that’s what underrage people do.")
                ans = input("CHOOSE:")
                if ans == 'a':
                    print("You go to your grandmother’s house like a good girl. But then you end up finding a furry wolf instead. What do you do?")
                    print("A/ You throw a knife at him.")
                    print("B/ You call your mom with your grandmother’s phone.")
                    print("C/ You leave the cookies for the wolf and run out of the house, freaking out.")
                    print("D/ You run to the city and buy something to calm yourself down.")
                    print("E/ Talk to the wolf KINDLY and ask where your grandma is.")
                    ans2 = input("CHOOSE:")
                    if ans2 == 'a':
                        print("You run to the kitchen and grab the nearest kitchen knife. You aim furiously at the wolf’s heart. You make the throw and the wolf is dead. You run to your grandma’s closet to find her asleep. You shake her and ask if she is okay. She isn’t able to talk because she has tape on her mouth. You get the tape off of her and she tells the story. You are amazed. Then you help her get out and go to a nearby park to enjoy the cookies. She can’t thank you enough. You are pleased.")
                        score += 5
                        print ("Score =",score)
                        break
                    if ans2 == 'b':
                        print("You take out your phone, quickly enter your password and dial your mom. Once she picks up you yell at her for not picking up quick enough. She asks what's wrong calmly and you tell her about the wolf. She rushes over in five minutes. In the meantime, you pace around quickly as the wolf is slowly waking up from his nap. You are surprised that he didn’t wake up from your yelling. You question yourself on where your grandma might be. You find her in the bathroom and untie the ropes. As you do this, your mom enters the house. She freaks out and grabs the nearest knife and kills the wolf. Once everything is cleared, you, your mom, and your grandma sit down with some tea and enjoy the cookies.")
                        score += 10
                        print ("Score =",score)
                        break
                    if ans2 == 'c':
                        print("You set the cookies down on the bed for the wolf, get your grandma and run back to your home. You found your grandma in her closet tied up. Once you and your grandma get to your home, you bake some fresh cookies with her. Your mom prepares some tea and you enjoy the snack. It turns out your mom is actually the wolf in disguise and he poisoned the cookies. You die in agony.")
                        print ("Score =",score)
                        break
                    if ans2 == 'd':
                        print("You freak out at the wolf, not knowing where your grandma is and hear her yell. You untie her and run to the city. You and your grandma find a boba tea shop and pay for some boba tea. You spend the rest of the day in the city with your grandma and then head home. Your mother is super angry because you didn’t buy some boba tea for her. She stomps off in anger and kills you with a kitchen knife.")
                        print ("Score =",score)
                        break
                    if ans2 == 'e':
                        print("You calmly ask the wolf where your grandma is and he replies and tells you that she is in the bathroom. You ask how he know’s. The wolf said that she and her are friends and she let her take a nap. You and the wolf become friends. When your grandma is done with her business. You then share the cookies with your grandma and the wolf and end up having the best day ever. The wolf betrays you and kills you and your grandma. Your mother comes and finds you and the wolf kills you too. You all go to hell and get eaten by a python, you die once again." )
                        print ("Score =",score)
                        break
                if ans == 'b':
                    print(" You go to the bar with a fake ID.")
                    ans3 = input("Once you are there you see your friend. You go find him. He offers you a chocolate bar, do you accept or decline:")
                    if ans3 == 'accept':
                        print("You start to eat it, and you suddenly feel dizzy. You unconsciously go into a drunken stupor, and soon go upstairs to collapse on your friend. When you wake up, your mom is outside.")
                        print("What will you do:")
                        print("A/ Play with your friend.")
                        print("B/ Jump out the window.")
                        print("C/ Admit mistake and accept your beating.")
                        ans4 = input("CHOOSE:")
                        if ans4 == 'a':
                            print("Your mom thankfully dies, and you get to drink until you're too drunk. Long story short, your health declines fast and soon you die in agonizing pain. AND….. You meet your mom in hell. Your mom is super angry and demands that you apologize. What do you do?")
                            print("A/ Apologize to your mother like a good daughter does.")
                            print("B/ Slaughter your mother and eat her flesh.")
                            print("C/ Recruit an army of dead skeletons....and Hades to take on your mother.")
                            ans5 = input("CHOOSE:")
                            if ans5 == 'a':
                                print("Your mother forgives you and you live happily ever after...in HELL.")
                                score += 3
                                print ("Score =",score)
                                break
                            if ans5 == 'b':
                                print("Her flesh tastes digusting and you die from food poisoning.")
                                print ("Score =",score)
                                break
                            if ans5 == 'c':
                                print("You defeat your mother and Hades and take over the underworld.")
                                score += 15
                                print ("Score =",score)
                                break
                        if ans4 == 'b':
                            print("You die after falling out because you're drunk. You break every part of your body and you're in agonizing pain. Just when you're about to die, some bugs crawl over your body and start to eat your flesh. A handsome knight suddenly appears and “debugs” you...haha just kidding...a knight? Impossible with that face. You die and the bugs eat your corpse.")
                            print ("Score =",score)
                            break
                        if ans4 == 'c':
                            print("*WACK* The beating stings, and leaves a mark on you. You then go study hard and get good grades, go to a NICE college, and soon make a business and become the world's first person with more money then the government AND the economy. You live well and never die until the end of earth, which was 218939182739128739821739718 years after your birth.")
                            score += 10
                            print ("Score =",score)
                    if ans3 == 'decline':
                        print("Your friend makes you go upstairs, and you see your mom coming...")
                        print("What will you do:")
                        print("A/ Use the secret Joestar technique and get the hell out of there with Smokey (aka. Your friend who offered you the chocolate bar.")
                        print("B/ Make her drunk and fall in love with a random dude on the street (because your mom is obviously widowed)")
                        print("C/ Meet up with your mom and go talk and drink boba with her.")
                        ans4 = input("CHOOSE:")
                        if ans4 == 'a':
                            print("You and smokey run to your grandma’s, only to see her rapping like a boss. SECRET ENDING :OOOOOO Mission Passed:Respect 100")
                        if ans4 == 'b':
                            print("You made your mom drunk, and the three of you guys go to 7-11 to get sum Yakults. Your mom soon sobers up and gives you a good beating, but you spent her life savings on Minecraft…. And you soon die from your wounds. Mission Failed.")
                        if ans4 == 'c':
                            print("You drink boba and head over to your grandma’s house, drop off some tea, and you all see the wolf…*DUN DUN DUN* You and your mom search for weapons. Your grandma grows and becomes stronk. They clash it out until they grow too tired to fight. What do you do?") 
                            print("A/ Finish the wolf off.")
                            print("B/ Make peace with him.")
                            ans6 = input("CHOOSE:")
                            if ans6 == 'a':
                                print("You are then raided by his family, which obliterates you guys. What will you do? ")
                                print("Do you, A/ Tactical nuke time.")
                                print("Or B/ Shoot them and epicly default dance.")
                                ans7 = input("CHOOSE:")
                                if ans7 == 'a':
                                    print("You die in the process LOL. You still got the wolves though.")
                                    break
                                if ans7 == 'b':
                                    print("You win! Game over!")
                                    break
                            if ans6 == 'b':
                                print("You were backstabbed. You are eaten and therefore die and suffer LOL.")
                                break


                
                
            if option == '2':
                print ("DUO. I'M SUPRISED YOU EVEN HAVE A FRIEND,", name)
                print("LOADING 20%-------LOADING 45%-------LOADING 60%-------\n")
                n3 = input("PLAYER ONE. CHOOSE A NAME FOR YOUR CHARACTER:")
                n4 = input("PLAYER TWO. CHOOSE A NAME FOR YOUR CHARACTER:")
                print ("THE GAME IS STARTING, GET READY.")
                print ("THIS GAMEMODE IS NOT AVAILABLE. GO PLAY BY YOURSELF")
                break