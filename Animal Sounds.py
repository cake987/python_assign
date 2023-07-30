class Animal:
    def make_sound(self):
        print("Generic animal sound")


class Dog(Animal):
    def make_sound(self):
        print("Bark")


class Cat(Animal):
    def make_sound(self):
        print("Meow")


def animal_sound_in_zoo(animal_obj):
    animal_obj.make_sound()


def main():
    print("Animal Sounds")
    dog_instance = Dog()
    cat_instance = Cat()

    print("Dog in the zoo:")
    animal_sound_in_zoo(dog_instance)

    print("\nCat in the zoo:")
    animal_sound_in_zoo(cat_instance)


if __name__ == "__main__":
    main()
