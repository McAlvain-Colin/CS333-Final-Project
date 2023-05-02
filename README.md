CS333 Final Project: Automated Testing and Deployment of "UNO by 'bennuttall'"
------------------------------------------------------------------------------

This project impliments the automated testing and building processes for a digital version of a UNO game, written primarily in Python by the github user "bennuttall." The GitHub repository link for the software is provided in the credits. The main objective of this project is to automate the software's building and deployment processes. This is achived using a YAML file in github to run test files written using unittest and using docker called by the same YAML file inside of github triggered on a repository push. The software underwent 77% unit testing, and five integration tests.

Table of Contents
-----------------

Overview
Table of Contents
Installation
Usage
Features
Automated Testing
Automated Deployment
Class Code for Demo
Credits
Contact

Installation
------------

update linux system
    sudo apt-get update
install git 
    sudo apt-get install git
install coverage
    sudo apt-get install python3-pip
    pip install coverage
install docker
    sudo apt-get install docker-ce docker-ce-cli containerd.io
check installation 
    git --version
    coverage --version
    docker --version

Usage
-----

Instructions for how to use the project, including any command line options or arguments.

Features
--------

This code is written in Python programming language and uses the UnoGame 
class from the "uno" module to simulate a game of Uno. 

The program generates a random number of players between 2 and 15 and creates a 
new instance of the UnoGame class with that number of players. 

The program loops while the game is still active according to the rules defined by the 
wiki-site. Within the loop, the code keeps track of the number of turns played and identifies the 
current player. If the current player can play a card, the code checks if any of the cards in the 
player's hand are playable on the current card. If so, it selects the first playable card, and if it is 
a black card, it randomly selects a color for the card to be played. The code then prints a 
message indicating the card played by the player and updates the game accordingly by playing 
the selected card. If the current player cannot play any card, the code prints a message 
indicating that the player is picking up a card and updates the game by playing a null card. 
The loop continues until the game is no longer active. Once the game is over, the code 
prints a message indicating the number of players in the game and the number of cards played 
during the game. 

Classes: 
    • UnoGame: This class contains the necessary attributes and methods to simulate a game 
        of Uno. It includes methods for shuffling and dealing cards, playing cards, and checking 
        game status. 
    • UnoPlayer: This class represents a player in the game and has properties like player ID, 
        hand, and methods like checking if the player has any playable cards. 
    • UnoCard: This class represents a single card in the game and has properties like color, 
        card type, color short, card type short, and methods like a check for valid card, check if 
        card is playable. 
    • ReversibleCycle: This class represents an interface to an iteratoratable list which can be 
        infinitely cycled and reversed. It includes a method for next, and attributes for position 
        and direction.  
    • AIUnoGame: This class represents a full Uno game that includes an UnoGame, players, 
        hand, and choices. It includes methods to run through a full game of Uno and lets to 
        user play with the system.   

The code imports Python’s random and itertools libraries. It defines some constants like the 
list of colors, all colors, numbers, special card types, color card types, black card types, and card 
types. Then it defines the UnoCard class, which has methods to validate and represent the card. 
It also defines the UnoPlayer class, which has a method to check if the player has any playable 
cards. Finally, it defines the UnoGame class, which represents the game and has methods like 
dealing the cards, creating the deck, iterating over the players, and checking if a player has won 
the game. 

NOTE: This github repo has a testing file included from the original author. These files will 
not be used for the CS333 final project but will be turned in with the rest of the program for 
transparency. This test code will not be used for this project. All unit tests in provided in 
reference to this project will be written by the authors of this paper and will be original to this 
project. Correlating tests may exist due to the nature of the testing process.  

Overall, this code randomly generates a game of Uno with a random number of players and 
plays through the game until it is complete. 
Functionality and Technologies: 

Functionality: 
    1. This code functions as a digital Uno game. 
    2. This code can simulate 2-15 players. 
    3. This code has self-play functionality with computer generated game play for NPC. 
    4. This code simulates a deck of cards that mirrors the uno deck.  
        a. If this deck runs out of cards it is shuffled and put back into play. 
        b. Cards in play are not regenerated.  
    5. This code has a graphic user interface with visible cards that have images of official Uno 
        cards with a black back.  
        Technologies: 
    1. Libraries Used 
        a. Shuffle 
        b. Choice 
        c. Product 
        d. Repeat 
        e. Chain  
        f. Unittest 
        g. Tread 
        h. Sleep 
        i. Random 
        j. itertools 
    2. Outside Software 
        a. Github 
        b. Python Unittest 
        c. Python3 
        d. Github 
        e. Docker

Source Code Centralization:
    This project uses Github for source code centralization and test automazation, implementing a master, dev, and feature branch approach, to segment workflow processes.  
    
Build and Deployment Automation: 
    This project uses Docker for automation of building. 

Automated Testing
-----------------

To automate testing, the github repo was outfited with a YAML file. This file is located inside a .github/workflow folder. 

The name of this YAML file is "Uno".

The YAML file contains a workflow that will be triggered on a push event.

The workflow consists of two jobs: "UnitAndIntegrationTests" and "Docker".

The "UnitAndIntegrationTests" job runs on the latest version of Ubuntu and uses a matrix strategy to test the Python code against different versions of Python (3.7 to 3.11).

The job contains a set of steps that:
    Checkout the code using the GitHub Actions checkout action.
    Set up the specified version of Python and cache pip.
    Install the "ruff" package using pip.
    Install the "coverage" package using pip.
    Run linting checks using "ruff".
    Run unit tests using "coverage".

Automated Deployment
--------------------
To automate testing, the github repo was outfited with a YAML file. This file is located inside a .github/workflow folder. 

The name of this YAML file is "Uno".

The YAML file contains a workflow that will be triggered on a push event.

The workflow consists of two jobs: "UnitAndIntegrationTests" and "Docker".

The "Docker" job runs on the latest version of Ubuntu and depends on the successful completion of the "UnitAndIntegrationTests" job.

The job contains a set of steps that:
    Checkout the code using the GitHub Actions checkout action.
    Login to Docker Hub using the docker/login-action.
    Set up Docker Buildx using the docker/setup-buildx-action.
    Build and push a Docker image using the docker/build-push-action.
    The Docker image is tagged with the username and the name of the image as specified in the secrets of the repository.

This is dependant on the githib repo containing two secretes for the Docker username 
    and token.

Class Code for Demo
-------------------

check test coverage
    coverage run tests_uno.py
    coverage report -m
create a new image
    git add .
    git commit -m "Added a new file"
    git push
        -McAlvain_Colin
        -get Token
run docker image
    docker pull cmcalvain/uno:latest
    docker images
    docker run -ti cmcalvain/uno

Credits
-------
uno.py: bennuttall
pgz_screenshot.png: bennuttall
random_game.py: bennuttall
uno_tests.py: bennuttall 
    -Note: this test is included for transparency only.It is created by the original uno.py writer, bennuttall. It is not part of the CS333 Final Project. Testing Coverage is attained thorugh tests_uno.py alone.

CS333: Final_Project_Design_Document-McAlvain_Colin McAlvain_Colin
Dockerfile: McAlvain_Colin
README: McAlvain_Colin
requirements.txt: McAlvain_Colin
tests_uno.py: McAlvain_Colin

Bennuttall. (2017, August 31). Bennuttall/Uno: Python implementation of the card game uno. 
GitHub. Retrieved April 25, 2023, from https://github.com/bennuttall/uno  

Wikimedia Foundation. (2023, March 28). Uno (card game). Wikipedia. Retrieved April 25, 
2023, from https://en.wikipedia.org/wiki/Uno_(card_game)#Official_rules

Configure CI/CD for your application. Docker Documentation. (2023, May 2). Retrieved May 2, 2023, from https://docs.docker.com/language/python/configure-ci-cd/ 

Contact
-------
McAlvain Colin
    github: McAlvain_Colin
    email: cmcalvain@nevada.unr.edu
