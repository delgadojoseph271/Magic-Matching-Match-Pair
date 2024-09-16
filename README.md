# Juego de Memoria con Pygame
## Descripción
Este es un juego de memoria desarrollado con Pygame, en el que el jugador debe emparejar cartas volteadas en un tablero. El objetivo es hacer coincidir todas las parejas de cartas en el menor tiempo posible. 
## Características
- Tablero de cartas generado aleatoriamente.
- Detecta clics del usuario para voltear cartas.
- Identifica cartas emparejadas y las mantiene volteadas.
- Reinicia el juego cuando todas las parejas han sido encontradas.
## Instalación

1. Clona este repositorio:
```bash
git clone https://github.com/delgadojoseph271/improved-succotash.git
python juego/main.py
```
#### 5. **Uso**
Proporciona instrucciones sobre cómo jugar o utilizar el software. Si el proyecto tiene parámetros o configuraciones importantes, indícalo aquí.

```markdown
## Cómo Jugar

1. Inicia el juego.
2. Haz clic en dos cartas para voltearlas.
3. Si las cartas coinciden, permanecerán volteadas; si no, se voltearán de nuevo.
4. El juego termina cuando emparejas todas las cartas.

```

## Estructura del Proyecto

- `audio/`: Aquí van todos los audios y música del proyecto.
- `img/`: Contiene todas las imágenes y sprites del juego.
- `src/`: Contiene el código fuente del juego.
  - `motor.py`: El archivo principal que ejecuta la parte jugable del juego.
  - `objetos.py`: Define las clases como `cartas`.
  - `settings.py`: Define las constantes del juego (ancho, alto, colores, etc.).
  - `ux/`: Contiene las interfaces de usuario del juego.
  - `utils/`: Contiene funciones auxiliares como `generarMatriz`, `desordenar`, entre otras.
- `main/`: Aquí se unen todas las partes del juego.


## Contribuciones

Si deseas contribuir:
1. Haz un fork del repositorio.
2. Crea una rama nueva (`git checkout -b feature/nueva-funcionalidad`).
3. Haz commit de tus cambios (`git commit -m 'Agrega nueva funcionalidad'`).
4. Haz push a la rama (`git push origin feature/nueva-funcionalidad`).
5. Abre un pull request.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.

## Autores

- Joseph Delgado (Líder de Proyecto,Desarrollador)
- Joselyn De Gracia (Desarrolladora,UX,Graficos)
- Nathalie Lopez (Desarrolladora, audios y sonidos)


