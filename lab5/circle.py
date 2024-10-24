class Circle:
    def __init__(self,radius):
        self.radius=radius

    def get_radius(self):
        return self.radius

    def set_radius(self,new_radius):
        self.radius=new_radius

circle2=Circle(12)
print('Изначальный радиус:',circle2.get_radius())
circle2.set_radius(7)
print('Новый радиус:',circle2.get_radius())