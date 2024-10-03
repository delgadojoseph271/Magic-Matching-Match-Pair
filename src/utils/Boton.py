import pygame

class Boton:
    def __init__(self, x, y, width, height, color, texto):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.texto = texto
        self.texto_superficie = pygame.font.Font(None, 36).render(self.texto, True, (1,1,1))

    # Método para dibujar el botón
    def dibujar(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        # Centra el texto dentro del botón
        screen.blit(self.texto_superficie, (self.rect.x + (self.rect.width - self.texto_superficie.get_width()) // 2,
                                            self.rect.y + (self.rect.height - self.texto_superficie.get_height()) // 2))

    # Método para detectar si se ha hecho clic en el botón
    def es_presionado(self, posicion_mouse):
        return self.rect.collidepoint(posicion_mouse)