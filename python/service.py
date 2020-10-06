import sys
import webiopi
import json
import unicornhat
import datetime

"""This script is adapted from the binary_clock.py example found in the Unicorn hat repository: https://github.com/pimoroni/unicorn-hat/blob/master/examples/binary_clock.py"""

#do this to import local modules
module_path = '/home/pi/binary_clock/python'
if module_path not in sys.path:
    sys.path.append(module_path)

#import custom classes
import constants
from settings import Settings

### START OF GLOBAL VARIABLES

#settings are loaded at startup
settings = None
# how many minutes should the alarm flash for
alarm_flash_time = 1
# the right most pixel (is set in setup)
right_most_pixel = 0

def draw_time_string(time_string, length, offset, row, colour):
    global right_most_pixel
    """Draw the binary time on a specified row in a certain colour.
    :param time_string: string containing time value that will be used for the bit comparison
    :param length: width of the binary string once converted, e.g. 5 bits for day, 6 bits for hour and mi$
    :param offset: left offset - all values are displayed with right alignment as conventional binary dic$
    :param row: row on which to display the time, this is the y-axis
    :param colour: colour to draw in
    """
    # convert the time string to an integer
    value = int(time_string)
    # loop through the pixels from the right to the left
    for i in range(right_most_pixel, right_most_pixel - length, -1):
        # use the & operator to do a bit comparison
        # for example:
        # 1 & 1 = 1 (ie: 0b1 & 0b1 = 0b1)
        # 2 & 1 = 0 (ie: 0b10 & 0b01 = 0b00)
        if value & 1:
            rgb = colour
        else:
            rgb = (0, 0, 0)
        # determine where on the row it should display this LED
        # either at the given location in the loop or shifted over to the left a little
        column = (i - offset)
        # set the pixels colour
        unicornhat.set_pixel(column, row, rgb)
        # use a binary shift to move all the values over to the right
        # for example:
        # 10 = 0b1010 shifted by 1 place becomes 0b0101 = 5
        # 5 = 0b101 shifted by place becomes 0b010 = 2
        value >>= 1

# this function will make use of the remaining space to light up when indicated
def alarm(t, c):
    global settings
    global alarm_flash_time

    alarm_time = settings.getValue(constants.ALARM_TIME)

    # by default we will assume the alarm will not be triggered
    b = '0'
    # grab the hour and minute from the set alarm time
    h = int(alarm_time[:2])
    m = int(alarm_time[3:])
    s = 0
    # create time slot for alarm for today
    at = t.replace(hour=h, minute=m, second=s)
    # create a new time object by adding x minutes to the alarm time
    ft = at + datetime.timedelta(minutes=alarm_flash_time)
    # now check if it's time to flash the alarm or not, by checking if we have passed the time it is mean$
    if t >= at and t < ft:
        # signal the alarm!
        # this will make it flash ON when a second is equal and OFF when it is odd
        if int(t.second % 2) == 0:
            # when converted to binary becomes 0b11, so this will turn ON ALL LEDs
            b = '255'
    # always update the pixels, the logic above will decide if it displays or not
    #draw_time_string(b, 8, 0, 5, c)
    draw_time_string(b, 8, 0, 6, c)
    draw_time_string(b, 8, 0, 7, c)

@webiopi.macro
def getTime():
    global settings
    now = datetime.datetime.now()

    time_string = now.strftime('%H:%M')
    if(settings.getValue(constants.MILITARY_TIME) == 'false'):
        #if using 12 hour clock, convert
        time_string = now.strftime('%I:%M %p')

    return json.dumps({'alarm_time':settings.getValue(constants.ALARM_TIME), 'military_time': settings.getValue(constants.MILITARY_TIME), 'current_time': time_string })

@webiopi.macro
def getSettings():
    global settings

    return json.dumps(settings.getAllValues())

@webiopi.macro
def saveValue(setting_key, setting_value):
    global settings

    settings.setValue(setting_key, setting_value)

    return json.dumps({'message':'Saved!'})

# SETUP - called when webiopi sets up
def setup():
    global settings
    global alarm_flash_time
    global right_most_pixel

    settings = Settings('/home/pi/binary_clock/')

    webiopi.info('setup')
    webiopi.info('Alarm set for %s' % settings.getValue(constants.ALARM_TIME))

    unicornhat.set_layout(unicornhat.AUTO)
    unicornhat.rotation(180)
    # default brightness does not need to be too bright
    unicornhat.brightness(0.5)
    # get the width of the hat because the LEDs are displayed from the righ to the left
    width, height = unicornhat.get_shape()
    right_most_pixel = width - 1


# LOOP - the main program loop
def loop():
    global right_most_pixel
    now = datetime.datetime.now()

    # draw each time string in their specific locations
    draw_time_string(now.month, 4, 0, 0, constants.MAGENTA)

    # Day field is 4 bits (lights) long, and as we don't use 0-indexed
    # days of the month, that means we can only represent 1-15 (0b1 - 0b1111)
    # To solve this, if the day > 15 (0b1111), we change the colour to indidcate
    # that 16 (0b10000) must be added to the displayed value.
    if now.day > 0b1111:
        # Day > 15

        # Truncate the day to only 4 bits, as we only have 4 lights
        # This will remove the bit representing 16, which will
        # be encoded as colour
        day = now.day & 0b1111

        # Encode the missing bit as colour
        day_colour = constants.GREEN
    else:
        # Day is 15 or less so the bit representing 16 is not set and the number can be displayed$
        day = now.day
        day_colour = constants.BLUE

    draw_time_string(day, 4, 0, 1, day_colour)

    # if not using military time adjust the time for a 12 hr clock
    current_hour = now.hour
    hour_color = constants.RED
    if(settings.getValue(constants.MILITARY_TIME) == 'false'):
        #either substract 12 if over 12pm or adjust color to designate AM
        if(current_hour > 12):
            current_hour = current_hour - 12
        elif(current_hour < 12):
            hour_color = constants.ORANGE

    draw_time_string(current_hour, 6, 0, 3, hour_color)
    draw_time_string(now.minute, 6, 0, 4, constants.YELLOW)
    draw_time_string(now.second, 6, 0, 5, constants.GREEN)

    # check if the alarm needs to be signalled or not
    alarm(now, constants.WHITE)

    # we've now set all the LEDs, time to show the world our glory!
    unicornhat.show()
    webiopi.sleep(1)

