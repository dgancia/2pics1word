import images
import os



def gameStart():
    os.system('cls')
    print("")
    print("|","="*102,"|")
    print("|                                       === 2 Pis 1 Word! ===                                            |")
    print("|","="*102,"|")
    print("|                                                                                                        |")


    inputStart = input("| => Should we should start?(y or n) ")
    

    if(inputStart == "y" or "Y"):  
        print("|","")
        print("|","="*102,"|")
        print("|","| Instruction:                                                                                       |","|")
        print("|","|     It will show two images and what you to do is to guess the hidden word you the given images    |","|") 
        print("|","|                    To answer you must enter the guessed word in the blank                          |","|")
        print("|","|                                                                                                    |","|")
        print("|","|                    ( !! WARNING: YOU ONLY HAVE A ONE CHANCE TO ANSWER !! )                         |","|")
        print("|","="*102,"|")
        understandable = input("| => Is that clear?(y or n) ")

        if(understandable == "y" or "Y"):

            os.system('cls')
            print(images.ballpen())
            player_answer = input("==> ")
                        
            if player_answer == "ballpen":
                print("")
                print("Right answer!, Next question")
                print(images.carpet())
                player_answer = input("==> ")

                if player_answer == 'carpet':
                    print("")
                    print("Right answer!, Next question")
                    print(images.cupcake())
                    player_answer = input("==> ")

                    if player_answer == "cupcake":
                        print("")
                        print("Right answer!, Next question")
                        print(images.facebook())
                        player_answer = input("==> ")

                        if player_answer == "facebook":
                            print("")
                            print("Right answer!, Next question")
                            print(images.congrats())
                            player_answer = input("Press enter to go back to menu... ")
                            import main
                            main()


                        else:
                            print("")
                            print(images.lose())
                            player_answer = input("Press enter to try again... ")
                            gameStart()

                    else:
                        print("")
                        print(images.lose())
                        player_answer = input("Press enter to try again... ")
                        gameStart()
                else:
                    print("")
                    print(images.lose())
                    player_answer = input("Press enter to try again... ")
                    gameStart()
            else:
                print("")
                print(images.lose())
                player_answer = input("Press enter to try again... ")
                gameStart()
