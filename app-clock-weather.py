from rgbmatrix import graphics, RGBMatrix, RGBMatrixOptions
from datetime import datetime
from weather import GetCurrentWeather
import requests
from io import BytesIO
from PIL import Image
import time
import sys
import schedule


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
#line color
linecolor = graphics.Color(15,30,15)

def GetWeather():
    #get weather
    currentWeather = GetCurrentWeather()
    temp = str(currentWeather[0])

    #remove F
    temp = temp.replace("F", "")

    #shift the weather over for over 100 degree temps
    weatherPos = 30
    print(temp)
    if int(temp)>99:
        weatherPos = 26

    #add degree sign
    degree_sign = u'\N{DEGREE SIGN}'
    temp = temp + degree_sign

    #get condition
    #condition = currentWeather[1]
    condition = currentWeather[2]
    print(condition)
    response = requests.get("http:" + condition)
    image = Image.open(BytesIO(response.content))
    return temp, weatherPos, image

temp, weatherPos, image = GetWeather()

def Setmatrix():
    
    #get the time and date 
    now = datetime.now()


    #day of week
    graphics.DrawText(canvas, font, 48, 7, color, now.strftime('%a'))
    #month
    graphics.DrawText(canvas, font, 48, 22, color, now.strftime('%b'))
    #day
    graphics.DrawText(canvas, font, 52, 30, color, now.strftime('%d'))
    #time
    graphics.DrawText(canvas, timeFont, 2, 30, color, now.strftime('%-I:%M'))
    #temp
    graphics.DrawText(canvas, font, weatherPos, 22, color, temp)
    #draw straight line
    graphics.DrawLine(canvas,45,0,45,50,linecolor)
    #condition image
    image.thumbnail((30, 30), Image.ANTIALIAS)

    matrix.SwapOnVSync(canvas)
    matrix.SetImage(image.convert('RGB'), -5,-10)

#while True:
SetWeatherAndTime()
schedule.every(1).minutes.do(SetWeatherAndTime)
schedule.every(30).minutes.do(GetWeather)
    #time.sleep(5)

    
#def SetWeatherAndTime(setWeather):
     
    #get weather
 #   currentWeather = GetCurrentWeather()
  #  temp = str(currentWeather[0])

    #remove F
   # temp = temp.replace("F", "")

    #shift the weather over for over 100 degree temps
    #weatherPos = 30
    #print(temp)
    #if int(temp)>99:
    #    weatherPos = 26

    #add degree sign
    #degree_sign = u'\N{DEGREE SIGN}'
    #temp = temp + degree_sign

    #get condition
    #condition = currentWeather[1]
    #condition = currentWeather[2]
    #print(condition)
    #response = requests.get("http:" + condition)
    #image = Image.open(BytesIO(response.content))

    #get the time and date 
    #now = datetime.now()


    #day of week
    #graphics.DrawText(canvas, font, 48, 7, color, now.strftime('%a'))
    #month
    #graphics.DrawText(canvas, font, 48, 22, color, now.strftime('%b'))
    #day
    #graphics.DrawText(canvas, font, 52, 30, color, now.strftime('%d'))
    #time
    #graphics.DrawText(canvas, timeFont, 2, 30, color, now.strftime('%-I:%M'))
    #temp
    #graphics.DrawText(canvas, font, weatherPos, 22, color, temp)
    #draw straight line
    #graphics.DrawLine(canvas,45,0,45,50,linecolor)
    #condition image
    #image.thumbnail((30, 30), Image.ANTIALIAS)

    #matrix.SwapOnVSync(canvas)
    #matrix.SetImage(image.convert('RGB'), -5,-10)



