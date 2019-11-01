class School:
    def __init__(self, name, roster={}):
        self.name = name
        self.roster = roster
    def add_student(self, name, grade):
        if grade in self.roster:
            self.roster[grade].append(name)
        else:
            self.roster[grade] = [name]
