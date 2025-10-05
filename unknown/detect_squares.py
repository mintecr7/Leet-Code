class DetectSquares:

    def __init__(self):
        self.points = []


    def add(self, point: list[int]) -> None:
        self.points.append(point)

    def count(self, point: list[int]) -> None:
        # square_count = set()
        x_axis_point = False
        y_axis_point = False
        for i in self.points:
            if i[0] == point[0]:
                x_axis_point = i
            if i[1] == point [1]:
                y_axis_point = i
            if x_axis_point and y_axis_point:
                print(x_axis_point, y_axis_point, point)
                break
        if not( x_axis_point and y_axis_point):
            print("fara")


obj = DetectSquares()
obj.add([3, 10])
obj.add([11, 2])
obj.add([3, 2])
param_2 = obj.count([11,10])
param_2 = obj.count([14,8])
obj.add([11,2])
param_2 = obj.count([11,10])
