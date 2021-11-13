from pygame import*
Background=("background.jpg")
window=display.set_mode((700,500))
class GameSprite(sprite.Sprite): 
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed): 
        super().__init__() 
        self.image = transform.scale(image.load(player_image), (size_x, size_y)) 
        self.speed = player_speed 
        self.rect = self.image.get_rect() 
        self.rect.x = player_x 
        self.rect.y = player_y
class player1(GameSprite): 
    def update(self): 
        keys = key.get_pressed() 
        if keys[K_UP] and self.rect.y > 5: 
            self.rect.y -= self.speed 
        if keys[K_DOWN] and self.rect.y < win_height + 80: 
            self.rect.y += self.speed 
class player2(GameSprite): 
    def update2(self): 
        keys = key.get_pressed() 
        if keys[K_w] and self.rect.y > 5: 
            self.rect.y -= self.speed 
        if keys[K_s] and self.rect.y < win_height + 80: 
            self.rect.y += self.speed
class ball(GameSprite):
    def movement(self):
        

         