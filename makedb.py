from person import Person, Manager
import shelve

bob = Person('Bob smith')
sue = Person('Sue Jones', job='dev', pay = 10000)
tom = Manager('Tom Jones', 50000)

with shelve.open('persondb') as db:
    for object in (bob,sue,tom):
        db[object.name] = object
