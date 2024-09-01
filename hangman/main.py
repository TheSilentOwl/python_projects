import random as rd
word_list = [
    "apple", "banana", "orange", "grape", "carrot", "broccoli", "pizza", "bread", "pasta", "cheese",
    "hamburger", "salmon", "oatmeal", "chocolate", "butter", "yogurt", "pancake", "omelette", "biscuit", "sushi",
    "table", "chair", "sofa", "cabinet", "lamp", "bed", "curtain", "mirror", "carpet", "shelf",
    "brick", "concrete", "cement", "steel", "timber", "plaster", "insulation", "wiring", "plumbing", "paint",
    "engine", "gearbox", "piston", "crankshaft", "valve", "turbine", "propeller", "circuit", "transistor", "resistor",
    "scalpel", "syringe", "stethoscope", "thermometer", "bandage", "antibiotic", "vaccine", "insulin", "aspirin", "diagnosis",
    "lathe", "drill", "hammer", "wrench", "anvil", "welder", "crane", "forklift", "compressor", "generator",
    "algorithm", "database", "network", "protocol", "encryption", "compiler", "bytecode", "variable", "function", "loop",
    "solar", "windmill", "battery", "generator", "thermostat", "furnace", "radiator", "airfilter", "chimney", "ductwork",
    "anatomy", "biology", "chemistry", "physics", "geology", "astronomy", "meteorology", "psychology", "sociology", "anthropology"
]

graph_list = [
"""  +---+
  |   |
      |
      |
      |
      |
=========""",
"""  +---+
  |   |
  O   |
      |
      |
      |
=========""",
"""  +---+
  |   |
  O   |
  |   |
      |
      |
=========""",
"""  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
"""  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========""",
"""  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========""",
"""  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========""",
]

# -------------------------------
# functions
# -------------------------------
def show():
    print(graph_list[current_graph])
    print(str(display))

def update_tries(the_tries):
    the_tries -= 1
    return the_tries

def update_graph(the_tries):
    the_current_graph = 7 - tries
    return the_current_graph

# -------------------------------
# setup
# -------------------------------
chosen_word = rd.choice(word_list)
tracker = list(chosen_word) # letters that are have not yet been guessed
display = list("_" * len(chosen_word)) # letters that have been guessed
tries = 7
current_graph = 7 - tries
print(chosen_word)

# -------------------------------
# logic
# -------------------------------
while display != list(chosen_word) and tries > 1:
    print("\n--------------------------------------\n")
    guess = input("What letter is in the word? 🤔\n")
    if guess in chosen_word and len(guess) == 1:
       if guess in tracker:
           print("you guessed right!")
           letter_index = tracker.index(guess)
           tracker[letter_index] = "_"
           display[letter_index] = guess


       elif guess in display:
           print("This letter has already been guessed!")
    else:
        print("you guessed wrong!")

        tries = update_tries(tries)
        current_graph = update_graph(tries)

    show()
    # print(display, list(chosen_word), tries)



if tries > 1:
    print("you have nailed it. Good job! ☺")
else:
    print("You have failed this time 😭, Good luck on the next one!")




