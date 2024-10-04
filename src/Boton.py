import pygame

class Boton:
    print ("importado correctamente")
    def __init__(self, x, y, width, height, text, color, hover_color, action=None):
        self.rect = pygame.Rect(x, y, width, height)#posicion y tamaño
        self.color = color #color del boton sin interactuar
        self.hover_color = hover_color # color cuando presionan el boton
        self.text = text #lo que se escribe encima del boton
        self.action = action #lo que pasa cuando se presiona
        self.font = pygame.font.SysFont(None, 40)
        
    def dibujar(self, screen):
        # Cambia de color si el cursor está encima del botón
        posicion_del_mouse = pygame.mouse.get_pos()#verifica la posicion del mouse o cursor
        if self.rect.collidepoint(posicion_del_mouse):
            pygame.draw.rect(screen, self.hover_color, self.rect)# si lo esta cambia de color 
        else:
            pygame.draw.rect(screen, self.color, self.rect)
        
        # Renderiza el texto en el botón
        text_surface = self.font.render(self.text, True, (0, 0, 0))
        screen.blit(text_surface, (self.rect.x + (self.rect.width - text_surface.get_width()) // 2, 
                                   self.rect.y + (self.rect.height - text_surface.get_height()) // 2))

    def es_clicleado(self, event):
        #detecta si clickean el boton
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # revisa si es  click izquierdo
            return self.rect.collidepoint(event.pos) #revisa que sea dentro del boton
