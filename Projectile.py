from Units import Unit
from Game import animation


class Projectile(Unit):
    def __init__(self):
        Unit.__init__(self, x, y, r=10, shooting_range=150, speed=10, visual=None, colour='red')

    def proj_calc(self, target):
        slipX = target.x - self.x
        slipY = target.y - self.y
        braker = 1
        side = True
        check_shot = True
        if slipX < 0:
            slipX *= -1
        if slipY < 0:
            slipY *= -1
        if slipX > slipY:
            braker = slipY / slipX
            side = True
        elif slipX < slipY:
            braker = slipX / slipY
            side = False
        elif slipX == 0 and slipY == 0:
            check_shot = False
        if target.x > self.x:
            speedX = 1
        elif target.x < self.x:
            speedX = -1
        else:
            speedX = 0
        if target.y > self.y:
            speedY = 1
        elif target.y < self.y:
            speedY = -1
        else:
            speedY = 0
        self.proj_mot(check_shot, speedX, speedY, braker, side)

    def proj_mot(self, check_shot, speedX, speedY, braker, side):
        if self.shooting_range and check_shot:
            animation.delete_obj(self)
            if side:
                self.x += speedX
                self.y += speedY * braker
                animation.draw(self)

            else:
                self.y += speedY
                self.x += speedX * braker
                animation.draw(self)

            self.shooting_range -= 1
            animation.screen.after(10, self.proj_mot, check_shot, speedX, speedY, braker, side)

        else:
            animation.delete_obj(self)
            Shots.remove(self)