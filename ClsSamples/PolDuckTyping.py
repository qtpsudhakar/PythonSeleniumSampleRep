

class Amithab:
    def act(self):
        print('Amithab is acting')

class Rajanikath:
    def act(self):
        print('Rajanikanth is acting')

class Movie:
    def action(self,actor):
        actor.act()

r = Rajanikath()
a = Amithab()
movie1 = Movie()
movie1.action(Rajanikath())
movie1.action(a)
movie1.action(Chiranjeevi())
# Movie.action(movie1,r)