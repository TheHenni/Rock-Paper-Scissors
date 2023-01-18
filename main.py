import random
import os
import time
import math

register_shape("Stein.gif")
register_shape("Schere.gif")
register_shape("Papier.gif")


 
def clear():
    pass
 
def rps_instructions():
 
    print()
    print("Regeln für Schere, Stein, Papier : ")
    print()
    print("Stein zertrümmert Schere")
    print("Schere zerschneidet Papier")
    print("Papier bedeckt Stein")
    print()
    print("Gewinnst du, bekommst du einen Punkt. Verlierst du, hast du wieder 0 punkte")
    print()
 
def rpsls_instructions():
 
    print()
    print("Regeln für Schere, Stein, Papier, Echse, Spock : ")
    print()
    print("Schere zerschneidet Papier")
    print("Papier bedeckt Stein")
    print("Stein zerquetscht Echse")
    print("Echse vergiftet Spock")
    print("Spock zerstört Schere")
    print("Schere köpft Echse")
    print("Echse isst Papier")
    print("Papier wiederlegt Spock")
    print("Spock verdampft Stein")
    print("Stein zertrümmert Schere")
    print()
    print("Gewinnst du, bekommst du einen Punkt. Verlierst du, hast du wieder 0 punkte")
    print()
 
def rps():
     
    global rps_table
    global game_map
    global name


    print("--------------------------------------")
    print("\t\tMenü")
    print("--------------------------------------")
    print("Schreib \"Hilfe\" für eine Einweisung")
    print("Schreib \"Stein\",\"Papier\",\"Schere\" um zu spielen")
    print("Schreib \"Beenden\" um das Spiel zu stoppen")
    print("--------------------------------------")
 
    print()

    x = 0
    while True:
        inp = input("Schere, Stein oder Papier? ")
 
        if inp.lower() == "hilfe":
            clear()
            rps_instructions()
            continue
        elif inp.lower() == "beenden":
            clear()
            break  
        elif inp.lower() == "stein":
            player_move = 0
        elif inp.lower() == "papier":
            player_move = 1    
        elif inp.lower() == "schere":
            player_move = 2
        else:
            clear()
            print("Falsche Eingabe!!")
            rps_instructions()  
            continue
 

        comp_move = random.randint(0, 2)

        print("Der Bot wählt: ", game_map[comp_move].upper())

        winner = rps_table[player_move][comp_move]

        if winner == player_move:
            print(name, "HAT GEWONNEN!!!")
            x = x+1
            print("Score=" + str(x))
        elif winner == comp_move:
            print("BOT HAT GEWONNEN!!!")
            x = x-1
            print("Score=" + str(x))
        else:
            print("UNENTSCHIEDEN!")
            print("Score=" + str(x))
 
        print()
        time.sleep(2)
        clear()
 
def rpsls():
     
    global rpsls_table
    global game_map
    global name

    x = 0
    print("--------------------------------------")
    print("\t\tMenu")
    print("--------------------------------------")
    print("Schreib \"Hilfe\" für eine Einweisung")
    print("Schreib \"Stein\",\"Papier\",\"Schere\",\"Echse\", \"Spock\" um zu spielen")
    print("Schreib \"Beenden\" um das Spiel zu stoppen")
    print("--------------------------------------")
         
    print()

    while True:
        inp = input("Schere, Stein, Papier, Echse oder Spock? ")
 
        if inp.lower() == "hilfe":
            clear()
            rpsls_instructions()
            continue
        elif inp.lower() == "beenden":
            clear()
            break  
        elif inp.lower() == "stein":
            player_move = 0
        elif inp.lower() == "papier":
            player_move = 1    
        elif inp.lower() == "schere":
            player_move = 2
        elif inp.lower() == "echse":
            player_move = 3
        elif inp.lower() == "spock":
            player_move = 4
        else:
            clear()
            print("Falsche Eingabe!!")
            rps_instructions()  
            continue
 
 
        comp_move = random.randint(0, 4)
 
        print("Der Bot wählt: ", game_map[comp_move].upper())
 
        winner = rpsls_table[player_move][comp_move]
        print()
        if winner == player_move:
            print(name, "HAT GEWONNEN!!!")
            x = x+1
            print("Score=" + str(x))
        elif winner == comp_move:
            print("BOT HAT GEWONNEN!!!")
            x = x-1
            print("Score=" + str(x))
        else:
            print("UNENTSCHIEDEN!")
            print("Score=" + str(x))       
        print()
        time.sleep(2)
        clear()

if __name__ == '__main__':
 
    game_map = {0:"stein", 1:"papier", 2:"schere", 3:"echse", 4:"Spock"}
 
    rps_table = [[-1, 1, 0], [1, -1, 2], [0, 2, -1]]
 
    rpsls_table = [[-1, 1, 0, 0, 4],[1, -1, 2, 3, 1], [0, 2, -1, 2, 4], [0, 3, 2, -1, 3], [4, 1, 4, 3, -1]]
 
     
    name = input("Wie heisst du?")
 
    while True:
 
        print()
        print("Los gehts!!!")
        print("Welche Version von Schere-Stein-Papier möchtest du spielen?")
        print("Schreib 1 um Schere-Stein-Papier zu du spielen")
        print("Schreib 2 um Schere-Stein-Papier-Echse-Spock zu du spielen")
        print()
 
        try:
            choice = int(input("Was möchtest du tun? = "))
        except ValueError:
            clear()
            print("Falsche Eingabe!!")   
            continue
 
        if choice == 1:
            x = 0
            rps()
 
        elif choice == 2:
            x = 0
            rpsls()
      
 
        else:
            clear()
            print("Falsche Eingabe. Lies dir die Aufgabenstellung nochmal genau durch.")
 
                            
