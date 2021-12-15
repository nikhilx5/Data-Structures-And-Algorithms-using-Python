class TrieNode:

    def __init__(self):
        self.children = [None] * 25
        self.is_end_of_word = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def _get_character_index(self, char):
        if char.isupper():
            return ord(char) - ord('A')
        else:
            return ord(char) - ord('a')

    def insert(self, string):
        pointer = self.root
        for char in string:
            # get index of character
            index = self._get_character_index(char)
            if not pointer.children[index]:
                pointer.children[index] = TrieNode()
            pointer = pointer.children[index]
        pointer.is_end_of_word = True
        return

    def search(self, string):
        pointer = self.root
        for char in string:
            # get the index of character
            index = self._get_character_index(char)
            if not pointer.children[index]:
                return False
            pointer = pointer.children[index]

        return pointer.is_end_of_word


obj = Trie()
obj.insert("Data")
print(obj.search("Data"))  # True

obj.insert("structure")
print(obj.search("structure"))  # True

obj.insert("Algorithms")
print(obj.search("Algo"))  # False

obj.insert("PrograMMing")
print(obj.search("programming"))  # True
