class Animal(object):
    def __init__(self,name):
        self._name=name

    def get_name(self):
        return self._name

    def set_name(self,value):
        self._name=value

    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print(self.get_name()+' is making sound wang wang wang...')

class Cat(Animal):
    def make_sound(self):
        print(self.get_name()+' is making sound miu miu miu...')

if __name__=='__main__':
    dog=Dog('koira')
    cat=Cat('kissä')
    dog.make_sound()
    cat.make_sound()
    animals=[Dog('D1'),Cat('C1'),Dog('D2'),Cat('C2')]
    for animal in animals:
        animal.make_sound()
