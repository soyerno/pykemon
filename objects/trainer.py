class Trainer:
    def __init__(self, name:str, lastname:str, town:str, pokemons:list):
        self.name = name
        self.lastname = lastname
        self.town = town
        self.pokemons = pokemons
        self.selected_pokemon = None
        self.turn = False

    def Gretting(self):
        print(f"Hello, I'm {self.name} {self.lastname} from { self.town } town.")

    def list_pokemons(self):
        print(f"{self.name} this are your pokemons:")
        for pokemon in self.pokemons:
            print(f"  {pokemon.nickname}")
    def select_pokemon(self, nickname):
        self.selected_pokemon = [pokemon for pokemon in self.pokemons if pokemon.nickname == nickname][0]
    def set_turn(self):
        self.turn = not self.turn