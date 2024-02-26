from rgbmatrix import graphics, RGBMatrix, RGBMatrixOptions
from PIL import Image, ImageSequence
import requests
from io import BytesIO
from pokemonjson import GetPokemon

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

#background_color = (255,255,255)

#url = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/1.png"
#response = requests.get(url)
#image = Image.open(BytesIO(response.content))
#image = image.convert("RGBA")

# Make image fit our screen.
#image.thumbnail((matrix.width, matrix.height), Image.ANTIALIAS)

#matrix.SetImage(image.convert('RGB'))

#url = GetPokemon()[2]
#url = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-v/black-white/animated/1.gif"
url="http://cdn.weatherapi.com/weather/64x64/day/116.png"
response = requests.get(url)
image = Image.open(BytesIO(response.content))
#image = image.convert("RGB")
num_frames = len(list(ImageSequence.Iterator(image)))
print(num_frames)

# Preprocess the gifs frames into canvases to improve playback performance
canvases = []
print("Preprocessing gif, this may take a moment depending on the size of the gif...")
for frame_index in range(0, num_frames):
    image.seek(frame_index)
    # must copy the frame out of the gif, since thumbnail() modifies the image in-place
    frame = image.copy()
    frame.thumbnail((20,20), Image.ANTIALIAS)
    canvas = matrix.CreateFrameCanvas()
    canvas.SetImage(frame.convert("RGB"))
    canvases.append(canvas)
# Close the gif file to save memory now that we have copied out all of the frames
image.close()

print("Completed Preprocessing, displaying gif")

try:
    print("Press CTRL-C to stop.")

    # Infinitely loop through the gif
    cur_frame = 0
    while(True):
        matrix.SwapOnVSync(canvases[cur_frame], framerate_fraction=10)
        if cur_frame == num_frames - 1:
            cur_frame = 0
        else:
            cur_frame += 1
except KeyboardInterrupt:
    sys.exit(0)
