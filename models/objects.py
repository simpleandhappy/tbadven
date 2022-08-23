class Object(object):
    def __init__(self, name, description, classification, actions):
        self.name = name
        self.description = description
        self.classification = classification
        self.actions = actions

    def __repr__(self):
        return name

    def examine(self):
        return f"a {self.name}, {self.description}"
