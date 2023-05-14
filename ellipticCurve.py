class EllipticCurve:
    def __init__(self, c1, c2, p):
        self.c1 = (c1 % p)
        self.c2 = (c2 % p)
        self.p = p

    def pointAddition(self, point1, point2):
        if point1 is None:
            return point2
        if point2 is None:
            return point1

        x1, y1 = point1
        x2, y2 = point2

        if (x1, y1) == (x2, y2):
            if y1 == 0:
                return None  # Point at infinity
            slope = ((3 * x1**2 + self.c1) * pow(2 * y1, -1, self.p)) % self.p
        else:
            if x1 == x2:
                return None  # Point at infinity
            slope = ((y2 - y1) * pow(x2 - x1, -1, self.p)) % self.p

        x_result = (slope**2 - x1 - x2) % self.p
        y_result = (slope * (x1 - x_result) - y1) % self.p

        return (x_result, y_result)

    def scalarMultiplication(self, k, point):
        result = None
        current = point
        while k > 0:
            if k % 2 == 1:
                result = self.pointAddition(result, current)

            current = self.pointAddition(current, current)
            k = k // 2

        return result
