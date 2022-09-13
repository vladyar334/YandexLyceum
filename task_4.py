class Scales:
    def __init__(self, max_value):
        self.max_value = max_value
        self.left_scale = 0
        self.right_scale = 0

    def add_left(self, value):
        if self.left_scale + value <= self.max_value:
            self.left_scale += value
            return
        print("value is too heavy")

    def add_right(self, value):
        if self.right_scale + value <= self.max_value:
            self.right_scale += value
            return
        print("value is too heavy")

    def remove_items(self):
        self.right_scale = 0
        self.left_scale = 0

    def __str__(self):
        return f"max allowed weight is {self.max_value}"

    def __call__(self):
        return "R" if self.right_scale > self.left_scale else "L" if self.left_scale > self.right_scale else "="
