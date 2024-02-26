from rgbmatrix import graphics, RGBMatrix, RGBMatrixOptions
import time

options = RGBMatrixOptions()
options.rows = 32
options.cols = 64
options.multiplexing = 0
options.row_address_type = 0
options.chain_length = 1
options.parallel = 1
options.brightness = 100
options.led_rgb_sequence = "RGB"
options.hardware_mapping = "adafruit-hat"
options.gpio_slowdown = 4
options.pwm_lsb_nanoseconds = 130
options.disable_hardware_pulsing = True
options.scan_mode = 1
options.pwm_bits = 1
options.show_refresh_rate = 0
options.daemon = 0
options.drop_privileges = 0
options.pixel_mapper_config = "U-mapper;Rotate:0"

matrix = RGBMatrix(options = options)
canvas = matrix.CreateFrameCanvas()

font = graphics.Font()
font.LoadFont("../../../fonts/7x13.bdf")
color = graphics.Color(0,255,0)
pos = canvas.width

while True:
    canvas.Clear()
    len = graphics.DrawText(canvas, font, pos, 10, color, "LUCA LUCA")
    pos -= 1
    if (pos + len < 0):
        pos = canvas.width

    time.sleep(0.05)
    canvas = matrix.SwapOnVSync(canvas)
