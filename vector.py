import math

def magnaitudeSquared(self):
    return self.x**2 + self.y**2

def magnitude(self):
    return sqrt(self.magnitudeSquared())

def normalize(self):
    mag = self.magnitude()
    if mag != 0:
        return self._div_(mag)
    return None

def dot(self, other):
    return self.x*other.x, self.y*other.y