class Point:
    def __init__(self, x, y):
        # x, y가 좌표값이지만 self로 대입해주는게 local -> global과 유사
        self.x = x
        self.y = y
  
# 이 문제에서는 Point만의 기능이 없으므로 상속 굳이 필요 없음
class Rectangle(Point):

    def __init__(self, x, y):
   #     super().__init__(x, y)
        self.x1 = x.x
        self.y1 = x.y
        self.x2 = y.x
        self.y2 = y.y
        # 가로, 세로 미리 셋팅하려면
        # self를 해야 global처럼 생각
        self.length = self.x2 - self.x1

        

    def get_area(self): 
        return abs(self.length) * abs(self.y2 -self.y1)
        #return abs(self.x2 - self.x1) * abs(self.y2 -self.y1)
    
    def get_perimeter(self):
        return (abs((self.x2 - self.x1)) + abs(self.y2 -self.y1)) * 2

    def is_square(self):
        return (self.x2 - self.x1) == abs((self.y2 -self.y1))

p1 = Point(1, 3)
p2 = Point(3, 1)  
r1 = Rectangle(p1, p2)

print(r1.get_area())  # 4
print(r1.get_perimeter())  # 8
print(r1.is_square()) # True

p3 = Point(3, 7)
p4 = Point(6, 4)
r2 = Rectangle(p3, p4)

print(r2.get_area())  # 9
print(r2.get_perimeter())  # 12
print(r2.is_square())  # True