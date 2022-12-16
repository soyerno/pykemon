#los argument con valor por defeacto van al final de la lista de argumentos
class Pokemon:
    def __init__(self, name:str, nickname:str, type:str, skills:list, level:int=1):
        self.nombre = name
        self.nickname = nickname
        self.level = level
        self.type = type
        self.skills = skills
        self.hp = 100

    def Gretting(self):
        print(f"Hola {self.nickname}")

    def list_skills(self):
        print(f"{self.nickname} this are your skills:")
        for skill in self.skills:
            print(f"  {skill.name}")

    def getDamage(self, hit):
        print(f"{self.nickname} recive {hit} damage")
        print(f"{self.nickname} has {self.hp} hp")
        self.hp = self.hp - hit

    def attack(self):
        self.list_skills()
        skill_selected = input("Choose your skill: ")
        while skill_selected not in [skill.name for skill in self.skills]:
            skill_selected = input("Skill not found choice an other: ")
        print(f"{self.nickname} use {skill_selected}")
        # skill
        skill = [skill for skill in self.skills if skill.name == skill_selected][0]
        return skill.power