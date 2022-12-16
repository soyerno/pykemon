import objects, random, time, os
from objects import pokemon, pokemon_skill, trainer 

class Game:
    def __init__(self):
        self.pokemon_skills = {}
        self.pokemons = {}
        self.trainers = {}

    def create_pokemon_skills(self):
        self.pokemon_skills["Tackle"] = pokemon_skill.Pokemon_skill("Tackle", "Normal", 40, 100)
        self.pokemon_skills["Thunder"] = pokemon_skill.Pokemon_skill("Thunder", "Electric", 60, 100)

    def create_pokemons(self):
        self.pokemons["Pedrito"] = pokemon.Pokemon("Pikachu", "Pedrito", "Electric", [self.pokemon_skills["Thunder"]], 1)

        self.pokemons["Matias"] = pokemon.Pokemon("Ratata", "Matias",  "Normal", [self.pokemon_skills["Tackle"]], 1)
    
    def create_trainers(self):
        self.trainers["Juan"] = trainer.Trainer("Juan", "Perez", "Jamón", [self.pokemons["Pedrito"]])
        self.trainers["Hernan"] = trainer.Trainer("Hernan", "Gomez", "Azalea", [self.pokemons["Matias"]])

    def battle(self, trainer1, trainer2):
        trainer1_pokemon_selected = self.choose_pokemon(trainer1)
        trainer2_pokemon_selected = self.choose_pokemon(trainer2)

        print(f"{trainer1.name} choose {trainer1_pokemon_selected} and {trainer2.name} choose {trainer2_pokemon_selected}")
        print("The battle begins!")

        player_start = random.choice([trainer1.name, trainer2.name])
        print(f"{player_start} start the battle!")
        self.trainers[player_start].set_turn()

        while self.trainers[trainer1.name].selected_pokemon.hp > 0 and self.trainers[trainer2.name].selected_pokemon.hp > 0:
            if self.trainers[trainer1.name].turn:
                trainer2.selected_pokemon.getDamage(trainer1.selected_pokemon.attack())
                self.trainers[trainer1.name].set_turn()
                self.trainers[trainer2.name].set_turn()
            else:
                trainer1.selected_pokemon.getDamage(trainer2.selected_pokemon.attack())
                self.trainers[trainer1.name].set_turn()
                self.trainers[trainer2.name].set_turn()

        if self.trainers[trainer1.name].selected_pokemon.hp <= 0:
            print(f"{trainer1.selected_pokemon.nickname} is down!")
            print(f"{trainer2.name} Won!")
        if self.trainers[trainer2.name].selected_pokemon.hp <= 0:
            print(f"{trainer2.selected_pokemon.nickname} is down!")
            print(f"{trainer1.name} Won!")
        
    def choose_pokemon(self, trainer):
        print(f"{trainer.name} choose your pokemon!")
        trainer.list_pokemons()

        # pokemon_list = []
        # for pokemon in trainer.pokemons:
        #     pokemon_list.append(pokemon.nickname)
        # selected_pokemon = input("Choose your pokemon: ")
        # while selected_pokemon not in pokemon_list:
        #     selected_pokemon = input("Pokemon not found choice an other: ")

        selected_pokemon = input("Choose your pokemon: ")
        while selected_pokemon not in [pokemon.nickname for pokemon in trainer.pokemons]:
            selected_pokemon = input("Pokemon not found choice an other: ") 

        print (f"{trainer.name} choose {selected_pokemon}")
        trainer.select_pokemon(selected_pokemon)

    def start(self):
        self.create_pokemon_skills()
        self.create_pokemons()
        self.create_trainers()
        print("Welcome to the world of Pokemon!")
        self.trainers["Juan"].Gretting()
        self.trainers["Hernan"].Gretting()
        self.battle(self.trainers["Juan"], self.trainers["Hernan"])


        