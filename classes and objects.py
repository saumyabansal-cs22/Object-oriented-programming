class person:
    name="saumya"
    occupation="web developer"
    coursee="btech"
    def info(self):
        print(f"{self.name} is a {self.occupation}")
        # self means that object for which the function is being called
k=person()
print(k.name)
print(k.occupation)
k.info()
k.name="Kartikey"
k.occupation="Flutter developer"
print(k.name)
print(k.occupation)
k.info()
v=person()
v.occupation="HR"
v.info()

