# coding=utf-8
import random as rnd


class Child(object):
    def __init__(self, age, name):
        assert isinstance(age, int)
        self.age = age
        assert isinstance(name, str)
        self.name = name

    def info(self, id=0):
        id += 1
        print "\tID: #" + str(id) + " Name: " + self.name + ", Age: " + str(self.age)


class Kindergarten(object):
    def __init__(self, number_of_applicants, number_of_places, input_names, input_second_names):
        self.queue = []
        self.number_of_applicants = number_of_applicants
        self.number_of_places = number_of_places
        assert isinstance(number_of_applicants, int)
        for g in range(number_of_applicants):
            self.queue.append(Child(rnd.randint(2, 5),
                                    rnd.choice(input_names) + " " +
                                    rnd.choice(input_second_names)))
        self.nursery = []
        self.younger = []
        self.middle = []
        self.senior = []

    def sort_all_queue(self):
        for i in range(self.number_of_places):
            if i < len(self.queue):
                element = self.queue[i]
                if element.age == 2:
                    self.nursery.append(element)
                elif element.age == 3:
                    self.younger.append(element)
                elif element.age == 4:
                    self.middle.append(element)
                elif element.age == 5:
                    self.senior.append(element)

    def show(self):
        print "Queue:"
        for h in range(len(self.queue) - 1):
            self.queue[h].info(h)

        print "Nursery group:"
        for h in range(len(self.nursery) - 1):
            self.nursery[h].info(h)

        print "Younger group:"
        for h in range(len(self.younger) - 1):
            self.younger[h].info(h)

        print "Middle group:"
        for h in range(len(self.middle) - 1):
            self.middle[h].info(h)

        print "Senior group:"
        for h in range(len(self.senior) - 1):
            self.senior[h].info(h)

    def __len__(self):
        return self.number_of_places

    def __del__(self):
        print("Deleted object Kindergarten")

    def __getitem__(self, item):
        return self.queue[item]

    def __setitem__(self, key, value):
        self.queue[key] = value


names = ["John", "Chloe", "Jack", "Samuel", "Joseph",
         "Harry", "Thomas", "Olivia", "Jessica", "Lily",
         "Scarlett", "Lily", "Isabella", "Emily", "Amelia"]

second_names = ["Johnson", "Smith", "Williams", "Brown", "Jones",
                "Miller", "Davis", "Garcia", "Rodriguez", "Wilson",
                "Martinez", "Anderson", "Taylor", "Thomas", "Moore"]

kindergartens = []
n = int(input("Choose number of kindergartens: "))
for i in range(n):
    kindergartens.append(Kindergarten(rnd.randint(10, 40), rnd.randint(10, 30), names, second_names))

for k in range(len(kindergartens)):
    kindergartens[k].sort_all_queue()
    print "Number of applicants: " + str(kindergartens[k].number_of_applicants - 1)
    print "Number of places: " + str(kindergartens[k].number_of_places - 1)
    kindergartens[k].show()
