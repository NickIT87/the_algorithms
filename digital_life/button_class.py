import pygame


vec = pygame.math.Vector2


class Button:
    def __init__(
        self, surface, x, y, width, height, state='', id='', 
        function=0, colour=(255, 255, 255), hover_colour=(255, 255, 255),
        border=True, border_width=2, border_colour=(255, 255, 255),
        text='', font_name='', text_size=2, text_colour=(255, 255, 255),
        bold_text=False
    )
        self.type = 'button'
        self.x = x
        self.y = y
        self.pos = vec(x, y)
        self.width = width
        self.height = height
        self.surface = surface
        self.image = pygame.Surface((width, height))
        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos
        self.state = state
        self.id = id
        self.function = function
        self.colour = colour
        self.hover_colour = hover_colour
        self.border = border
        self.border_width = border_width
        self.border_colour = border_colour
        self.text = text
        self.font_name = font_name
        self.text_size = text_size
        self.text_colour = text_colour
        self.bold_text = bold_text
        self.hovered = False

    def update(self, pos):
        if self.mouse_hovering(pos):
            self.hovered = True
        else:
            self.hovered = False

    def draw(self):
        if self.border:
            self.image.fill(self.border_colour)
            if self.hovered:
                pygame.draw.rect(self.image, self.hover_colour, (self.border_width, self.border_width,
                                                                 self.width-(self.border_width*2), 
                                                                 self.height-(self.border_width*2)))
            else:
                pygame.draw.rect(self.image, self.colour, (self.border_width, self.border_width,
                                                           self.width-(self.border_width*2), 
                                                           self.height-(self.border_width*2)))
        else:
            self.image.fill(self.colour)
        if len(self.text) > 0:
            self.show_text()
        self.surface.blit(self.image, self.pos)

    def click(self):
        if self.function != 0 and self.hovered:
            self.function()

    def show_text(self):
        font = pygame.font.SysFont(self.font_name, self.text_size, bold=self.bold_text)
        text = font.render(self.text, False, self.text_colour)
        size = text.get_size()
        x, y = self.width//2-(size[0]//2), self.height//2-(size[1]//2)
        pos = vec(x, y)
        self.image.blit(text, pos)

    def mouse_hovering(self, pos):
        pass