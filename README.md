# **Pokemon CLI Game \- Homework Assignment**

## **Homework Overview**

Complete the Pokemon CLI game by implementing the missing methods in your PokemonGame class. This homework builds upon the foundation we created in class and will result in a fully functional Pokemon catching game.

## **Prerequisites**

- Complete the in-class assignments (Pokemon Data Extractor, Pokemon Class, Player Class)
- Have a working get_pokemon_data() function
- Have a working Pokemon class with info() method
- Have a working Player class with add_pokemon(), remove_pokemon(), and show_collection() methods

---

## **Homework Assignment: Build the Pokemon Hunting System**

### **Task**

Implement the Pokemon hunting system where players can find and catch Pokemon.

### **Requirements**

Add these methods to your PokemonGame class:

```py
import random



def go_hunting(self):
    """
    Player encounters a random wild Pokemon (ID 1-151)
    and can choose to catch or flee
    """

    # YOUR CODE HERE - Part 1: Generate Wild Pokemon
    # 1. Generate a random Pokemon ID between 1 and 151
    # 2. Use get_pokemon_data() to fetch the Pokemon info
    # 3. Create a Pokemon object from the data
    # 4. Store it in self.wild_pokemon

    # YOUR CODE HERE - Part 2: Encounter Menu
    # Display: "A wild {pokemon_name} appeared!"
    # Show the Pokemon's info using pokemon.info()
    # Show options: "1. Try to catch  2. Flee"
    # Get user input and call appropriate method

    pass

def try_catch_pokemon(self):
    """
    Attempt to catch the wild Pokemon
    Base catch rate: 25%
    """

    # YOUR CODE HERE
    # 1. Calculate catch probability (base rate: 50%)
    # 2. Generate random number (0-1)
    # 3. If successful:
    #    - Add Pokemon to player's collection
    #    - Clear wild_pokemon
    #    - Show success message
    # 4. If failed:
    #    - Show failure message
    # 5. Show the catch probability for debugging

    pass

def remove_pokemon_menu(self):
    """Allow player to remove Pokemon from their collection"""

    # YOUR CODE HERE
    # 1. Show current collection using player.show_collection()
    # 2. Get user input for which Pokemon to remove
 #hint: make sure to convert input number to a proper index (1 -> 0)
    # 3. Call player.remove_pokemon() with the index
    # 4. Handle invalid input gracefully

    pass
```

### **Expected Behavior**

```
Welcome to Pokemon CLI Adventure!
What's your name, trainer? Ash

Hello Ash! Time to choose your starter Pokemon!

Choose your starter Pokemon:
1. Bulbasaur (Grass type)
2. Charmander (Fire type)
3. Squirtle (Water type)
Enter 1, 2, or 3: 2

Charmander added to Ash's collection!
You chose Charmander! Great choice!

=== Pokemon Adventure - Ash ===
1. Go hunting (find wild Pokemon)
2. View your collection
3. Remove Pokemon from collection
4. Quit game

What would you like to do? 1

You go hunting for Pokemon...

A wild Pidgey appeared!
Pidgey (ID: 16)
   HP: 40
   Attack: 45
   Type: normal
   Sprite: https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/16.png

1. Try to catch
2. Flee

What do you want to do? 1

You throw a Pokeball...
Catch rate: 25.0%
Gotcha! Pidgey was caught!
Pidgey added to Ash's collection!
```

### **Implementation Hints**

-

#### **For go_hunting():**

- Use random.randint(1, 151\) to generate random Pokemon IDs
- Check if get_pokemon_data() returns valid data before creating Pokemon object
- Handle the case where API request fails gracefully
- Use input() to get user choice and convert to integer
- Call try_catch_pokemon() or handle fleeing based on user input

#### **For try_catch_pokemon():**

- Base catch rate is 25% (0.25)
- Use random.random() to generate a number between 0 and 1
- If random number ≤ catch rate, the catch is successful
- Remember to check if player's collection is full before adding Pokemon
- Clear self.wild_pokemon after successful catch or flee

#### **For remove_pokemon_menu():**

- Show the collection first so user knows what's available
- Get user input for which Pokemon to remove (1-based indexing)
- Convert to 0-based index for the remove_pokemon() method
- Handle invalid input (non-numbers, out-of-range numbers)
