class Scoop:

    def __init__(self, flavor):
        self.flavor = flavor


def create_scoops():

    flavors = ['chocolate', 'vanila', 'persimmon']
    scoops = [Scoop(flavor) for flavor in flavors]

    for scoop in scoops:
        print(f"Each instance has its unique flavor: {scoop.flavor}")


create_scoops()
