# Jacob Meadows
# Computer Programming, 4th Period
# October 18th, 2017
"""
You will be creating a spaceship game over the next few days. The first step will be to create a game that does the following:
Greets the user and tells them the point of the game
Ask the user's name
Shows a menu with an option to 'Start Game' or 'Enter Planet Code'
(for now only allow Start Game as an option)
When the user starts game, tell them what planet they are on (which is Earth to start with)
Ask the user the ship weight
Ask the user how fast they want to go
[this will be enough for now]

You will now be asking the user what speed they want to go to get off the planet, and compare that to what the escape velocity is for Earth.
This needs to be a function, you can do it as an 'escape_planet' or just 'escape_earth' (which you would then have to create a function for each planet).
Use a global variable for their name so it can be used in every function. If they do not put high enough speed, crash them.
If it is right or within a realistic number above, congratulate them and tell them the new planet they are on. If they are too high, crash them.

Make sure all planets are in program
Have an option of quitting
Give planet codes each time the person lands
Up to you if the person has to start over completely or just start over on that planet if they crash

Have the game keep track of points for the user, and show them how many points they got when they die.
Person can now enter a planet code and start on that planet.
Reset score and planet when they die.
Use either .lower(), .upper(), or .title() to make their input more user friendly
CLEAN GAME AND CLEAN CODE, commented correctly with good grammar and easy for someone, who has no idea what this is, to play.
"""
planet = "earth"
menuchoice = ""
score = 0
aopgt = 0
def beginning(): # Runs all of the functions that are needed to start the game.
    global planet
    global menuchoice
    global score
    greetingsandpog()
    menu(menuchoice, planet)
def greetingsandpog(): # Greets the user and tells them the point of the game.
    print("Welcome to 'Spaceship Game!'\nThe point of the game is to escape the planet you're on by determining how fast you believe you need to go.")
    name = askforname()
def askforname(): # Asks for the user's name.
    name = input("Name: ")
    return name
def menu(menuchoice, planet): # Gives the user the choice of starting the game, entering a planet's code, or quitting and going down those said paths.
    if menuchoice == "":
        try:
            menuchoice = int(input("1. Start Game\n2. Enter Planet Code\n3. Quit\n"))
        except ValueError:
            print("Sorry, there's either an error or I misunderstood you; please check what you wrote and/or try again.")
            menu(menuchoice, planet)
    if menuchoice == 1:
        print("You begin on planet %s." %planet.title())
        choice1 = choice1ofmenuchoiceroute()
        choice2 = choice2ofmenuchoiceroute()
        choice3 = choice3ofmenuchoiceroute()
        planet = checkplanet(choice2, choice3, planet)
        menu("1", planet)
    elif menuchoice == "1":
        choice2 = choice2ofmenuchoiceroute()
        choice3 = choice3ofmenuchoiceroute()
        planet = checkplanet(choice2, choice3, planet)
        menu("1", planet)
    elif menuchoice == 2:
        try:
            choice1, choice2, choice3, planet = codecheck().split(", ")
            choice2 = float(choice2)
            planet = checkplanet(choice2, choice3, planet)
            menu("1", planet)
        except ValueError:
            print("Sorry, there's either an error or I misunderstood you; please check what you wrote and/or try again.")
            codecheck()
    elif menuchoice == 3:
        quit()
    else:
        print("Sorry, there's either an error or I misunderstood you; please check what you wrote and/or try again.")
        menu("", planet)
def choice1ofmenuchoiceroute(): # Asks the user for the ship's weight.
    try:
        choice1 = int(input("What's the ship's weight?: "))
        return choice1
    except ValueError:
        print("Sorry, there's either an error or I misunderstood you; please check what you wrote and/or try again.")
        choice1 = choice1ofmenuchoiceroute()
        return choice1
def choice2ofmenuchoiceroute(): # Asks the user how fast they want to go.
    try:
        choice2 = float(input("How fast do you want to go? (km/s): "))
        return choice2
    except ValueError:
        print("Sorry, there's either an error or I misunderstood you; please check what you wrote and/or try again.")
        choice2 = choice2ofmenuchoiceroute()
        return choice2
def choice3ofmenuchoiceroute(): # Asks the user where they want to go to.
    y = input("Where do you want to go to?: ")
    try:
        if y.lower() == "earth" or y.lower() == "mars" or y.lower() == "mercury" or y.lower() == "venus" or y.lower() == "saturn" or y.lower() == "jupiter" or y.lower() == "the moon" or y.lower() == "pluto" or y.lower() == "uranus" or y.lower() == "neptune":
            return y
        else:
            print("The planet you inputted doesn't exist, please try again.")
            choice3 = choice3ofmenuchoiceroute()
            return choice3
    except ValueError:
        print("The planet you inputted doesn't exist, please try again.")
        choice3 = choice3ofmenuchoiceroute()
        return choice3
def codecheck(): # Checks the inputted code to see if it matches with any of the registered planets.
    c = int(input("Please input a valid planet code: "))
    if c == 37492749:
        planet = "earth"
        nextplanet = code_planet(planet)
        return nextplanet
    elif c == 98502842:
        planet = "mars"
        nextplanet = code_planet(planet)
        return nextplanet
    elif c == 77193027:
        planet = "venus"
        nextplanet = code_planet(planet)
        return nextplanet
    elif c == 18363845:
        planet = "mercury"
        nextplanet = code_planet(planet)
        return nextplanet
    elif c == 42904931:
        planet = "uranus"
        nextplanet = code_planet(planet)
        return nextplanet
    elif c == 87401719:
        planet = "neptune"
        nextplanet = code_planet(planet)
        return nextplanet
    elif c == 48204326:
        planet = "jupiter"
        nextplanet = code_planet(planet)
        return nextplanet
    elif c == 68163934:
        planet = "saturn"
        nextplanet = code_planet(planet)
        return nextplanet
    elif c == 38601839:
        planet = "pluto"
        nextplanet = code_planet(planet)
        return nextplanet
    elif c == 19278468:
        planet = "the moon"
        nextplanet = code_planet(planet)
        return nextplanet
def code_planet(x): # Is the path for correct codes.
    print("You begin on planet %s." %x.title())
    choice1 = choice1ofmenuchoiceroute()
    choice2 = choice2ofmenuchoiceroute()
    choice3 = choice3ofmenuchoiceroute()
    choices = str(choice1) + ", " + str(choice2) + ", " + choice3 + ", " + x
    return choices
def checkplanet(x, y, z): # Checks the inputted planet to see if it matches with any of the registered planets, and if so, runs the escape_planet() function with the proper planet's name and escape velocity.
    if str(z).lower() == "earth":
        escapevelocity = 11.186
        planetcode = 37492749
        nextplanet = escape_planet(x, y, z, escapevelocity, planetcode)
        return nextplanet
    elif str(z).lower() == "mars":
        escapevelocity = 5.03
        planetcode = 98502842
        nextplanet = escape_planet(x, y, z, escapevelocity, planetcode)
        return nextplanet
    elif str(z).lower() == "venus":
        escapevelocity = 10.36
        planetcode = 77193027
        nextplanet = escape_planet(x, y, z, escapevelocity, planetcode)
        return nextplanet
    elif str(z).lower() == "mercury":
        escapevelocity = 4.25
        planetcode = 18363845
        nextplanet = escape_planet(x, y, z, escapevelocity, planetcode)
        return nextplanet
    elif str(z).lower() == "uranus":
        escapevelocity = 21.38
        planetcode = 42904931
        nextplanet = escape_planet(x, y, z, escapevelocity, planetcode)
        return nextplanet
    elif str(z).lower() == "neptune":
        escapevelocity = 23.56
        planetcode = 87401719
        nextplanet = escape_planet(x, y, z, escapevelocity, planetcode)
        return nextplanet
    elif str(z).lower() == "jupiter":
        escapevelocity = 60.20
        planetcode = 48204326
        nextplanet = escape_planet(x, y, z, escapevelocity, planetcode)
        return nextplanet
    elif str(z).lower() == "saturn":
        escapevelocity = 36.09
        planetcode = 68163934
        nextplanet = escape_planet(x, y, z, escapevelocity, planetcode)
        return nextplanet
    elif str(z).lower() == "pluto":
        escapevelocity = 1.23
        planetcode = 38601839
        nextplanet = escape_planet(x, y, z, escapevelocity, planetcode)
        return nextplanet
    elif str(z).lower() == "the moon":
        escapevelocity = 2.38
        planetcode = 19278468
        nextplanet = escape_planet(x, y, z, escapevelocity, planetcode)
        return nextplanet
def escape_planet(x, y, z, a, b): # Checks to see if the inputted, predicted escape velocity or speed was fast enough, but not too fast for the planet they wanted to go to.
    global planet
    global score
    global aopgt
    if x >= a and x <= (a * 1.1):
        print("You made it, you're on %s!" %y.title())
        print("{} had the code {}".format(z.title(), b))
        aopgt = aopgt + 1
        score = score + (5 * aopgt)
        print("Your score is now %d" %score)
        nextplanet = y
        return nextplanet
    elif x >= (a * 1.1):
        print("You were going too fast, you crashed!")
        print("Your final score is %d" %score)
        score = 0
        aopgt = 0
        menu(menuchoice, planet)
    elif x < a:
        print("You were going too slow, you crashed!")
        print("Your final score is %d" %score)
        score = 0
        aopgt = 0
        menu(menuchoice, planet)

beginning() # Runs the game.
