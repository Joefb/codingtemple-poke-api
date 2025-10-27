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

    def add_pokemon(self, pokemon):
        """Takes in a pokemon object and adds it to the team if there is room"""
        if len(self.team) < 6:
            self.team.append(pokemon)
            print(f"{pokemon.name} has been added ot the team!")
            return
        else:
            print("The team is full, remove a pokemon to make space.")
            return

    def remove_pokemon(self, index):
        """Remove a Pokemon from the collection by index"""
        if len(self.team) and index >= 0 and index < len(self.team):
            pokemon = self.team.pop(index)
            print(f"{pokemon.name} has been released!")
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

    def choose_starter(self):
        print("Choose your starting Pokemon!")
        print("1. Bulbasaur")
        print("2. Charmander")
        print("3. Squirtle")

        name = input("Enter your pokemon's name: ")
        poke_dict = player.get_pokemon_data(name)
        if poke_dict:
            pokemon = Pokemon(**poke_dict)
            player.add_pokemon(pokemon)
        else:
            print("Invalid Pokename, please try again")

        self.main_game_loop()

    def main_game_loop(self):
        """Main game loop menu"""
        while True:
            print("""
============== Menu ================
1.) Search for a Pokemon
2.) View our team
3.) Remove Pokemon from team
4.) Quit game
""")
            choice = int(input("(1-4): "))
            if choice == 4:
                print("Thanks for playing!")
                return  # Quit out the game

            if choice == 1:
                pass  # Go look for pokemon to catch
            elif choice == 2:
                player.show_collection()  # View all the pokemon in the player's team
            elif choice == 3:
                player.remove_pokemon()
                pass  # remove a pokemon from our team using its index

    def intro_screen(self):
        """
        print the intro screen and get player name
        """

        os.system("clear")
        print("Welcome to Pokemon CLI Adventure!")
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
        player.choose_starter()

    def go_hunting(self):
        pass

    def try_catch_pokemon(self):
        pass

    def remove_pokemon_menu(self):
        pass


def main():
    pokemon_game = PokemonGame()
    pokemon_game.intro_screen()


if __name__ == "__main__":
    main()
