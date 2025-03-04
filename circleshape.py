import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # update later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius
        

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def update(self, dt):
        pass

    def collision(self, CircleShape):
        distance = pygame.math.Vector2.distance_to(self.position, CircleShape.position)
        if distance < (self.radius + CircleShape.radius):
            return True
        else:
            False