from jb.python_training.oop_example.dog_object import DogObject


class MainAnimals:
    dog_1 = DogObject("Rexy",4)
    dog_2 = DogObject("Lucky",6)

    dog_1.make_noise()
    dog_2.make_noise()
    dog_1.calculate_distance(4,2)