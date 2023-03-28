class vowels:
    all_vowels = ['a', 'e', 'i', 'o', 'u', 'y']

    def __init__(self, text):
        self.text = text
        self.vowels = [v for v in self.text if v.lower() in vowels.all_vowels]
        self.iteration = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.iteration == len(self.vowels):
            raise StopIteration
        index = self.iteration
        self.iteration += 1
        return self.vowels[index]


my_string = vowels('Abcedifuty0o')

for char in my_string:
    print(char)
