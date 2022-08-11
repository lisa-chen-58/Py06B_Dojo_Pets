from pet import Pet

class Ninja:
        # implement __init__( first_name , last_name , treats , pet_food , pet )

    def __init__(self, ninja_first_name, ninja_last_name, ninja_treats, ninja_pet_food):
        self.f_name = ninja_first_name
        self.l_name = ninja_last_name
        self.treats = ninja_treats
        self.pet_food = ninja_pet_food
        self.pets = {}

    # creates an instance of pet and adds it to Ninja's pets list
    def adopt_pet(self, name, type, tricks, health, energy):
        pet = Pet(name, type, tricks, health, energy)
        self.pets[name] = pet
        print(f"{self.f_name} has now adopted {pet.name}")
        return self

    # takes an existing pet and adds it to Ninja's pets list
    def adopt_existing_pet(self, obj):
        pet = obj
        self.pets[obj.name] = pet
        print(f"{self.f_name} has now adopted {pet.name}")
        return self

    # walk() - walks the ninja's pet invoking the pet play() method
    def walk(self, pet_name):
        pet_obj = self.pets[pet_name]
        pet_obj.play()
        print(f"{self.f_name}'s pet {pet_name} has played and now has health of {pet_obj.health} and energy of {pet_obj.energy}")
        return self;
    
    # feed() - feeds the ninja's pet invoking the pet eat() method
    def feed(self, pet_name):
        pet_obj = self.pets[pet_name]
        pet_obj.eat()
        print(f"{self.f_name}'s pet {pet_name} has eaten and now has health of {pet_obj.health} and energy of {pet_obj.energy}")
        return self;
    
    # bathe() - cleans the ninja's pet invoking the pet noise() method
    def bathe(self, pet_name):
        pet_obj = self.pets[pet_name]
        pet_obj.noise()
        print(f"{self.f_name}'s pet {pet_name} has been bathed")
        return self;
    
    def printing(self):
        print(self.pet)


# Implement walk(), feed(), bathe() on the ninja class.
thunder_cat = Ninja("Lion","O","leadership","prey")

# Implement sleep(), eat(), play(), noise() methods on the pet class.
Snarf = Pet("Osbert","Snarf","refers to himself in third person",1000,2000)
Snarf.sleep().eat().play().noise()

# Make an instance of a Ninja and assign them an instance of a pet to the pet attribute.
Lisa = Ninja("Lisa","Chen","turkey","food")
Lisa.adopt_pet("Saria","Dog","sleeping",100,100)
Lisa.adopt_existing_pet(Snarf)

# Have the Ninja feed, walk , and bathe their pet.
Lisa.walk("Saria").feed("Saria").bathe("Saria")
Lisa.walk(Snarf.name)

# NINJA BONUS: Use modules to separate out the classes into different files.
# WOOT

# SENSEI BONUS: Use Inheritance to create sub classes of pets.
class ThunderCat(Pet):
    def __init__(self, pet_name, pet_type, pet_tricks, pet_health, pet_energy, attack_power):
        super().__init__(pet_name, pet_type, pet_tricks, pet_health, pet_energy)
        self.att_pow = attack_power;

Taigra = ThunderCat("Taigra", "thunder cat", "swipe", 5000,5000,2000)
