class Rhombus:
    def __init__(self, side_a, angle_a):
        self.side_a = side_a
        self.angle_a = angle_a

    def __setattr__(self, name, value):
        if name == "side_a":
            if value <= 0:
                raise ValueError("Side must be greater than 0")

        elif name == "angle_a":
            if not (0 < value < 180):
                raise ValueError("Angle must be between 0 and 180")

            super().__setattr__("angle_b", 180 - value)

        elif name == "angle_b":
            raise AttributeError("angle_b is calculated automatically and cannot be set directly")

        super().__setattr__(name, value)

rhombus = Rhombus(5, 60)

print(rhombus.angle_a)  # 60
print(rhombus.angle_b)  # 120
