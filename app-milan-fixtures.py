from rgbmatrix import graphics, RGBMatrix, RGBMatrixOptions
from milanjson import GetFixtures
from PIL import Image

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
options.pwm_lsb_nanoseconds = 300
options.disable_hardware_pulsing = True
options.scan_mode = 1
options.pwm_bits = 11
options.show_refresh_rate = 0
options.daemon = 0
options.drop_privileges = 0
options.pixel_mapper_config = "U-mapper;Rotate:0"

matrix = RGBMatrix(options = options)
canvas = matrix.CreateFrameCanvas()

#select font and color
font = graphics.Font()
font.LoadFont("../../../fonts/5x7.bdf")
timeFont = graphics.Font()
timeFont.LoadFont("../../../fonts/6x10.bdf")
color = graphics.Color(255,255,255)


#get fixtures
fixture= GetFixtures()
print(fixture)

#home team
graphics.DrawText(canvas, font, 4, 30, color, fixture[1])
#away team
graphics.DrawText(canvas, font, 32, 30, color, fixture[2])
#date
graphics.DrawText(canvas, font, 30, 8, color, fixture[0])
#time
#graphics.DrawText(canvas, timeFont, 2, 30, color, now.strftime('%-I:%M'))
#temp
#graphics.DrawText(canvas, font, weatherPos, 22, color, temp)
#draw straight line
#graphics.DrawLine(canvas,45,0,45,50,linecolor)
#condition image

image = Image.open("milan.png")
image.thumbnail((matrix.width, matrix.height), Image.ANTIALIAS)
image2 = Image.open("milan.png")
image2.thumbnail((matrix.width, matrix.height), Image.ADAPTIVE)



matrix.SwapOnVSync(canvas)

matrix.SetImage(image.convert('RGB'),-5,-5)
matrix.SetImage(image2.convert('RGB'),40,-5)
