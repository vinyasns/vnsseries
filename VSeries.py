import math


class Vector:
    def __init__(self, x, y, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return "({0},{1},{2})".format(self.x, self.y, self.z)

    def add(self, vector):
        self.x += vector.x
        self.y += vector.y
        self.z += vector.z

    def subtract(self, vector):
        self.x -= vector.x
        self.y -= vector.y
        self.z -= vector.z

    def negate(self):
        self.x = -self.x
        self.y = -self.y
        self.z = -self.z

    def scalar_multiply(self, n):
        self.x *= n
        self.y *= n
        self.z *= n

    def get_unit_vector(self):
        magnitude = self.get_magnitude()
        x = self.x / magnitude
        y = self.y / magnitude
        z = self.z / magnitude
        return Vector(x, y, z)

    def get_magnitude(self):
        return math.sqrt(math.pow(self.x, 2) + math.pow(self.y, 2) + math.pow(self.z, 2))


class VSeries:
    def __init__(self, edge_length, delta, delta_angle=60):
        self.delta = delta
        self.edge = edge_length
        self.delta_angle = math.radians(delta_angle)

    def get_series(self, num):
        v1 = Vector(self.edge*math.cos(self.delta_angle), -self.edge*math.sin(self.delta_angle))
        v2 = Vector(-self.edge, 0)
        v_series = []
        v_series.append(v1)
        v_series.append(v2)

        for i in range(2, num):
            v = Vector(0, 0)
            v.add(v_series[i - 2])
            v.add(v_series[i - 1])
            v.negate()
            delta_vector = v.get_unit_vector()
            delta_vector.scalar_multiply(self.delta)
            v.add(delta_vector)
            v_series.append(v)

        v_num_series = [x.get_magnitude() for x in v_series]
        return v_num_series


def main():
    s = VSeries(4, 1)
    ss = s.get_series(50)
    print(ss)


main()
