import pygame

class cartas:
    estado = False
    tamanio = (10, 10)
    
    def __init__(self, pantalla, tamanio=(80, 120), posicion=(0, 0), valor=0, estado=False, relleno=None, img=None, color=(255, 255, 255), color_activo=(0, 255, 0), duracion_animacion=0.2) -> None:
        ancho = tamanio[0]
        alto = tamanio[1]
        x = posicion[0]
        y = posicion[1]
        self.estado = estado
        self.valor = valor
        self.relleno = relleno
        self.img = pygame.image.load(img) if img else None
        self.reverso = pygame.image.load('img/Reverso.jpeg')
        self.color = color
        self.color_activo = color_activo
        self.rect = pygame.Rect(x, y, ancho, alto)
        self.pantalla = pantalla
        self.clickeable = True
        self.animando = False
        self.tiempo_inicio = 0
        self.duracion_animacion = duracion_animacion  # Duración de la animación
        self.progreso_animacion = 0  # Progreso de la animación

    def dibujar(self):
        if self.animando:
            # Animación de volteo
            t = (pygame.time.get_ticks() - self.tiempo_inicio) / (self.duracion_animacion * 1000)  # Tiempo en segundos
            
            if t >= 1:  # Animación completada
                t = 1
                self.animando = False
                print(self.animando)
            
            # Escalar en el eje X para crear el efecto de voltear
            if self.estado:
                # Mostrar imagen frontal
                #print('ejecutando animacion frontal')
                escala_x = 1 - t  # Comprimir en el eje X
                img_redimensionada = pygame.transform.scale(self.img, (int(self.rect.width * escala_x), self.rect.height))
                self.pantalla.blit(img_redimensionada, (self.rect.x + (self.rect.width * (1 - escala_x) / 2), self.rect.y))
            else:
                # Mostrar reverso
                #print('ejecutando animacion reverso')
                escala_x = t  # Expandir en el eje X
                reverso_redimensionado = pygame.transform.scale(self.reverso, (int(self.rect.width * escala_x), self.rect.height))
                self.pantalla.blit(reverso_redimensionado, (self.rect.x + (self.rect.width * (1 - escala_x) / 2), self.rect.y))
        else:
            # Si no está animando, dibujar normalmente
            if self.estado:
                # Dibuja la imagen frontal
                img_redimensionada = pygame.transform.scale(self.img, (self.rect.width, self.rect.height))
                self.pantalla.blit(img_redimensionada, (self.rect.x, self.rect.y))
            else:
                # Dibuja el reverso
                reverso_redimensionado = pygame.transform.scale(self.reverso, (self.rect.width, self.rect.height))
                self.pantalla.blit(reverso_redimensionado, (self.rect.x, self.rect.y))

    def colisionaConPuntos(self, pos_mouse):
        if self.clickeable:
            return self.rect.collidepoint(pos_mouse)
        return False
    
    def cambiarEstado(self):
        if self.clickeable and not self.animando:
            self.animando = True
            self.tiempo_inicio = pygame.time.get_ticks()  # Marca el tiempo de inicio
            self.progreso_animacion = 0
            self.estado = not self.estado

    def resetear(self):
        self.clickeable = True
        self.estado = False
