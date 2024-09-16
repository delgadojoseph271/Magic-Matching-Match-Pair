import pygame

class cartas:
    estado = False
    tamanio = (10, 10)
    
    def __init__(self, pantalla, tamanio=(30, 30), posicion=(0, 0), valor=0, estado=False, relleno=None, img=None, color=(255, 255, 255), color_activo=(0, 255, 0)) -> None:
        ancho = tamanio[0]
        alto = tamanio[1]
        x = posicion[0]
        y = posicion[1]
        self.estado = estado  # verdadero o falso según se muestre o no la carta
        self.valor = valor  # el valor que se usará como identificador único
        self.relleno = relleno  # lo que se verá dentro de la carta al estar volteada 
        self.img = img  # la imagen de la carta al estar volteada (por si se necesita)
        self.color = color  # color del reverso de la carta cuando está desactivada
        self.color_activo = color_activo  # color del reverso de la carta cuando está activada
        self.rect = pygame.Rect(x, y, ancho, alto)
        self.pantalla = pantalla

    def dibujar(self):
        # Usa el color según el estado de la carta
        color_dibujar = self.color_activo if self.estado else self.color
        pygame.draw.rect(self.pantalla, color_dibujar, self.rect)
        
        if self.estado:
            # Opcional: dibuja el contenido de la carta si está "activada"
            font = pygame.font.SysFont(None, 24)
            texto = font.render(str(self.valor), True, (0, 0, 0))  # Texto en negro
            self.pantalla.blit(texto, (self.rect.x + 10, self.rect.y + 10))
            
    def colisionaConPuntos(self, pos_mouse):
            #Verifica si el mouse está sobre la carta
            return self.rect.collidepoint(pos_mouse)
    def cambiarEstado(self):
        # Invertir el estado de la carta
        print('El estado de la carta es: {}'.format(self.estado))
        self.estado = not self.estado