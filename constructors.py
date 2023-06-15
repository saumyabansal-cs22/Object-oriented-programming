class person():
    def __init__(self,n,o):
        print("hey i am here!")
        self.name=n
        self.occupation=o
    def info(self):
        print(f"{self.name} is a {self.occupation}")
a=person("saumya","developer")
b=person("tanmay","coder")
a.info()
b.info()