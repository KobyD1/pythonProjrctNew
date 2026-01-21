


class DogObject():
    def __init__(self, name, age):
        print (f"Into dog costructor for {name}")
        self.name = name
        self.age = age


    def go_to_sleep(self,time_to_sleep):
        print (F"going to sleep for {time_to_sleep} seconds")

    def make_noise(self):
        print ("Hao Hao Hao Hao")

    def calculate_distance (self,time,speed):
        distance = time * speed
        if distance <10 :
            print ("The dog is lazzy")

        else :
            print ("the dog is ok")

        return distance
