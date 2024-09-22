from mosaico import widget, colors
import time

# Constants
WIDTH = 64
HEIGHT = 64
SCALE = 10
STROKE_WIDTH = 2
WAVE_SPEED = 1
AMPLITUDE = 20
Y_OFFSET = 20

# Available colors for the rainbow effect
COLORS = [
 colors.red,
 colors.orange,
 colors.yellow,
 colors.green,
 colors.cyan,
 colors.blue,
 colors.purple,
]

# Faster sine approximation
def fast_sin(x):
 x = x % (2 * 3.14159)
 if x < 3.14159:
  return 4 * (x * (3.14159 - x)) / (3.14159 * 3.14159)
 else:
  x -= 3.14159
  return -4 * (x * (3.14159 - x)) / (3.14159 * 3.14159)


offset = 0

# Pre-calculate color indices
color_indices = [int((x / WIDTH) * len(COLORS)) % len(COLORS) for x in range(WIDTH)]

def loop():
 global offset

 for x in range(WIDTH):
  # Calculate the y position of the wave
  y = int((fast_sin((x + offset) / SCALE) + 1) * (AMPLITUDE / 2)) + Y_OFFSET

  # Draw the stroke
  for stroke in range(STROKE_WIDTH):
   stroke_y = y + stroke - STROKE_WIDTH // 2
   if 0 <= stroke_y < HEIGHT:
    widget.setPixel(x, stroke_y, COLORS[color_indices[x]])

 offset += WAVE_SPEED