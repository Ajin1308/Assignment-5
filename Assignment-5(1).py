class Point:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def sqSum(self):
        square_sum=self.x**2 + self.y**2 + self.z**2
        return square_sum

obj_square_sum = Point(1,2,3)
result_square_sum=obj_square_sum.sqSum()
print(f'Square of sum of {obj_square_sum.x},{obj_square_sum.y} and {obj_square_sum.z} is {result_square_sum}')