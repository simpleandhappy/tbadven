class Room(object):
    def __init__(self, name, description, entrances, objects):
        self.name = name
        self.description = description
        self.entrances = entrances
        self.objects = objects

    def __repr__(self):
        return f"{self.name}"

    def examine(self):
        return self.description

