import requests
import random
import os


class Pokemon:
    def __init__(self, name, id, hp, attack, sprite_url, type):
        self.name = name
        self.id = id
        self.hp = hp
        self.attack = attack
        self.sprite_url = sprite_url
        self.type = type

    def display_info(self):
        print(f"=============== {self.name}'s Info ===============")
        print(f"ID: {self.id}")
        print(f"Stats: HP - {self.hp} Attack - {self.attack}")
        print(f"Type: {self.type}")
        print(f"Sprite: {self.sprite_url}")


class Player:
    def __init__(self):
        self.name = ""
        self.team = []  # List of pokemon objects No more than 6 at a time

    def add_pokemon(self, pokemon):
        """Takes in a pokemon object and adds it to the team if there is room"""
        if len(self.team) < 6:
            self.team.append(pokemon)
            print(f"{pokemon.name} has been added to the team!")
            return
        else:
            print("The team is full, remove a pokemon to make space.")
            return

    def remove_pokemon(self, index):
        """Remove a Pokemon from the collection by index"""

        if len(self.team) >= 0 and index >= 0 and index <= len(self.team):
            pokemon = self.team.pop(index)
            return pokemon
        else:
            return None

    def show_collection(self):
        print(f"{self.name}'s Pokemon Collection:")
        i = 1
        for pokemon in self.team:
            print(f"{i}. {pokemon.name} (ID: {pokemon.id}) - {pokemon.type}")
            i += 1


class PokemonGame:
    def __init__(self):
        pass

    def get_pokemon_data(self, pokemon_identifier):
        """
        Get Pokemon data from PokeAPI and extract game-relevant information

        Args:
            pokemon_identifier: Pokemon name (str) or ID (int)

        Returns:
            dict: Pokemon information with keys: name, id, hp, attack, sprite_url, type
            None: if Pokemon not found or error occurred
        """

        url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_identifier}"

        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()  # Converts to Python

            pokemon = {
                "name": data["name"],
                "id": data["id"],
                "hp": data["stats"][0]["base_stat"],
                "attack": data["stats"][1]["base_stat"],
                "sprite_url": data["sprites"]["front_default"],
                "type": data["types"][0]["type"]["name"],
            }
            return pokemon

        else:
            print(f"Failed to catch {pokemon_identifier}")
            return None

    def choose_starter(self, player):
        print("Choose your starting Pokemon!")
        print("1. Bulbasaur")
        print("2. Charmander")
        print("3. Squirtle")

        name = input("Enter your pokemon's name: ")
        poke_dict = self.get_pokemon_data(name)
        if poke_dict:
            pokemon = Pokemon(**poke_dict)
            player.add_pokemon(pokemon)
        else:
            print("Invalid Pokename, please try again")

        self.main_game_loop(player)

    def main_game_loop(self, player):
        """Main game loop menu"""
        while True:
            print("""
============== Menu ================
1.) Go Pokemon Hunting!
2.) View our team
3.) Remove Pokemon from team
4.) Quit game
""")
            try:
                choice = int(input("(1-4): "))
                if choice < 1 or choice > 4:
                    print("Invalid input, please enter a number between 1 and 4.")
                    continue
            except ValueError:
                print("Invalid input, please enter a number between 1 and 4.")
                continue

            if choice == 4:
                print("Thanks for playing!")
                return  # Quit out the game

            if choice == 1:
                self.go_hunting(player)
            elif choice == 2:
                player.show_collection()  # View all the pokemon in the player's team
            elif choice == 3:
                self.remove_pokemon_menu(player)

    def intro_screen(self):
        """
        print the intro screen and get player name
        """

        os.system("clear")
        print("Welcome to Pokemon CLI Adventure!")
        name = ""
        try:
            name = str(input(("What is your name, trainer? ")))
            if len(name) <= 0:
                print("No name given.")
                input("Press Enter to try again...")
                self.intro_screen()

        except TypeError:
            print("Please enter valid input...")
            input("Press Enter to try again...")
            self.intro_screen()

        player = Player()
        player.name = name.title()

        print(f"Hello {player.name}!! Lets go hunting!")
        print(f"Ok {player.name} lets get you set up with a starter Pokemon!")
        self.choose_starter(player)

    def go_hunting(self, player):
        """
        Generate ran num for pokemon id
        Call get_pokemon_data and pass in ran num
        Assign returned data to Var
        Ask user if want to keep
        If so call try_catch_pokemon
        """
        ran_pokemon_id = random.randint(1, 151)
        ran_pokemon = self.get_pokemon_data(ran_pokemon_id)

        if ran_pokemon:
            pokemon = Pokemon(**ran_pokemon)
            # player.add_pokemon(pokemon)

        print("You and your team go hunting far and wide for a pokemon.")
        print(f"Suddenly a wild {pokemon.name} appears! They glower at you.")

        while True:
            print("What do you do!?...")
            print("1. Try to catch!")
            print("2. Run like the wind!")

            try:
                action = int(input("-> "))
                if action < 1 or action > 2:
                    print("Enter 1 or 2.")
                    continue
                else:
                    break

            except ValueError:
                print("Enter 1 or 2.")
                continue

        if action == 1:
            self.try_catch_pokemon(player)

        elif action == 2:
            print("You flee like the little sissy that you are!")
            print("Your team laughs at you...")
            return

    def try_catch_pokemon(self, player):
        pass

    def remove_pokemon_menu(self, player):
        print("Release the pokemon back to nature!")
        print("What pokemon will you release?")
        player.show_collection()

        if len(player.team) == 0:
            print("You dont have any pokemon! Go capture some!")
            return

        index = None
        while True:
            try:
                index = int(input("Enter Number->"))
                if index < len(player.team) or index > len(player.team):
                    print("Invalid number.")
                    continue
            except ValueError:
                print("Invalid Number.")
                continue

            break

        poke_removed = player.remove_pokemon(index - 1)

        print(f"You release the {poke_removed.name}!")
        print(
            f"Look how happy {poke_removed.name} is now that they are not forced to fight and die for you!"
        )


def main():
    pokemon_game = PokemonGame()
    pokemon_game.intro_screen()


if __name__ == "__main__":
    main()
