class Person (object):

    def __init__(self, name, gender, birth_year, father=None, mother=None):
        self.name = name
        self.gender = gender
        self.birth_year = birth_year
        self.all_children = []
        self.siblings = []
        if (father and birth_year - father.birth_year >= 18):
            father.all_children.append(self)
            self.father = father
        if (mother and birth_year - mother.birth_year >= 18):
            mother.all_children.append(self)
            self.mother = mother

    def get_siblings(self):
        if hasattr(self, "father"):
            self.siblings.extend(self.father.all_children)
        if hasattr(self, "mother"):
            self.siblings.extend(self.mother.all_children)

    def get_brothers(self):
        self.get_siblings()
        return list({x for x in self.siblings if x is not self
                    and x.gender == 'M'})

    def get_sisters(self):
        self.get_siblings()
        return list({x for x in self.siblings if x is not self
                    and x.gender == 'F'})

    def children(self, gender=None):
        if (gender):
            return [x for x in self.all_children if x.gender == gender]
        else:
            return self.all_children

    def is_direct_successor(self, other):
        return other in self.all_children
