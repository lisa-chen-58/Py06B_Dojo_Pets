class Pet:

    #  implement __init__( name , type , tricks ):
    def __init__(self, pet_name, pet_type, pet_tricks, pet_health, pet_energy):
        self.name = pet_name;
        self.type = pet_type;
        self.tricks = pet_tricks;
        self.health = pet_health;
        self.energy = pet_energy;

    # sleep() - increases the pets energy by 25
    def sleep(self):
        self.energy += 25
        print(f"{self.name}'s has slept")
        return self;

    # eat() - increases the pet's energy by 5 & health by 10
    def eat(self):
        self.energy += 5
        self.health += 10
        print(f"{self.name} has eaten!")
        return self;

    # play() - increases the pet's health by 5
    def play(self):
        self.health += 5
        print(f"{self.name} has played!")
        return self;


    # noise() - prints out the pet's sound
    def noise(self):
        print(f"{self.name} makes a noise! Thunder Cats HOOOOO")
        return self;