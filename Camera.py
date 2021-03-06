from World import world, spawn, camera_size, hero_speed


class Camera:

    def __init__(self, width=camera_size['width'], height=camera_size['height'], speed=hero_speed):
        self.x = spawn['x'] - width//2
        self.y = spawn['y'] - height//2
        self.w = width  # spawn['x'] + width//2
        self.h = height  # spawn['y'] + height//2
        self.speed = speed

    def camleft(self):
        if self.x - self.speed <= world['x']:
            self.x = world['x']
        else:
            self.x -= self.speed

    def camright(self):
        if self.x + self.w + self.speed >= world['width']:
            self.x = world['width'] - self.w
        else:
            self.x += self.speed

    def camup(self):
        if self.y - self.speed <= world['y']:
            self.y = world['y']
        else:
            self.y -= self.speed

    def camdown(self):
        if self.y + self.h + self.speed >= world['height']:
            self.y = world['height'] - self.h
        else:
            self.y += self.speed
