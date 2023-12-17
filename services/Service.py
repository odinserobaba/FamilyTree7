import pickle


class FamilyTreeSerializer:
    @staticmethod
    def serialize(family_tree, filename):
        with open(filename, 'wb') as file:
            pickle.dump(family_tree, file)

    @staticmethod
    def deserialize(filename):
        with open(filename, 'rb') as file:
            family_tree = pickle.load(file)
        return family_tree
