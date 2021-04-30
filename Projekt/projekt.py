#!/usr/bin/env python
from basesetup import BaseSetup


class SimpleSquare(BaseSetup):
    def __init__(self, *args, **kwargs):
        super(SimpleSquare, self).__init__(*args, **kwargs)


    def run(self):
        offset_canvas = self.matrix.CreateFrameCanvas()
        while True:
            # for x in range(0, self.matrix.width):
                # offset_canvas.SetPixel(x, x, 255, 255, 255)
                # Diagnonal lila od. weiss
                # offset_canvas.SetPixel(offset_canvas.height - 1 - x, x, 255, 0, 255)
                # Diagnonal lila od. weiss

            for x in range(0, offset_canvas.width):
                offset_canvas.SetPixel(x, 0, 255, 0, 0)
                # Oben rot
                #offset_canvas.SetPixel(x, offset_canvas.height - 1, 255, 255, 0)
                # Untne gelb
            # for y in range(0, offset_canvas.height):
                # offset_canvas.SetPixel(0, y, 0, 0, 255)
                # Links blau
                # offset_canvas.SetPixel(offset_canvas.width - 1, y, 0, 255, 0)
                # Rechts gruen
            offset_canvas = self.matrix.SwapOnVSync(offset_canvas)
    def einzelnesFeld():
        höheLänge = 3
        xStart = 10
        yStart = 10
        
        for x in range(xStart, xstart + höheLänge)
            offset_canvas.SetPixel(x, offset_canvas.height - 1, 255, 255, 0)
        
# Main function
if __name__ == "__main__":
    simple_square = SimpleSquare()
    if (not simple_square.process()):
        simple_square.print_help()
