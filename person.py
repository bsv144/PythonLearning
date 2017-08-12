from classtools import AttrDisplay

class Person(AttrDisplay):
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay
        
    def lastName(self):
        '''
            Метод возвращает фамилию
        '''
        return self.name.split()[-1]
        
    def giveRise(self, percent):
        '''
        Метод изменяет зарплату на указанный процент
        '''
        self.pay = int(self.pay * (1 + percent))

    def __repr__(self):
        return 'Repr: %s: %s -> %s' % (self.__class__.__name__, self.name, self.pay)

class Manager(Person):
    def __init__(self, name, pay):
        Person.__init__(self, name, 'mgr', pay)
    
    def giveRise(self, percent, bonus = .10):
        return Person.giveRise(self, percent + bonus)

if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jons', job='dev', pay=100000)
    tom = Manager('Tom Jones', 50000)
    
    class Departament:
        def __init__(self, *args):
            self.members = list(args)
        def addMember(self, person):
            self.members.append(person)
        def giveRaises(self,percent):
            for person in self.members:
                person.giveRise(percent)
        def showAll(self):
            for person in self.members:
                print(person)
    print('-- class Department --')
    development = Departament(bob,sue)
    development.addMember(tom)
    development.giveRaises(.10)
    development.showAll()
    
    print('--- End ---')
    
    print(bob)
    print(sue)
    print(bob.lastName(), sue.lastName())
    sue.giveRise(.10)
    print(sue)

    tom.giveRise(.10)
    print(tom.lastName())
    print(tom)
    print('--All three--')
    for object in (bob,sue, tom):
        object.giveRise(.10)
        print(object)