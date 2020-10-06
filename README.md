## Binary Clock
This projects in an implementation of a [binary clock](https://en.wikipedia.org/wiki/Binary_clock) using a [Raspberry PI](https://en.wikipedia.org/wiki/Raspberry_Pi) and a [Unicorn Pi Hat](https://shop.pimoroni.com/products/unicorn-hat). I've built this project using an Rpi3 but any version that accepts the Unicorn Hat will work. [WebIOPI](http://webiopi.trouch.com/) is utilized as a framework to provide a web interface as well. 

The code in this project is an adaption of the [binary clock example](https://github.com/pimoroni/unicorn-hat/blob/master/examples/binary_clock.py) code listed in the Unicorn Hat Github repository. It does have some significant differences from the example code that are pointed out below.

### Differences From Original

I tried to add several enhancements from the original design. Both to make it easier to use and a bit more customizable. 

1. The layout of the LEDs is modified from the original. Each row represents it's own time period (month, day, hour, etc) instead of combining rows. This makes more space at the bottom for the "alarm" functionality. 
2. Added a web interface via the WebIOPI framework. This makes it easier to run as a service and can modify settings on the fly. 
3. Can utilize either 24 or 12 hour clock. The 12 hour variant utilizes different LED colors to differentiate AM from PM 
4. Added ability to customize the colors for each time period. This is done via the web interface settings.

## Using the Binary Clock

Refer to the INSTALL.md document for information on how to get it all 
working. Once the program is running on your Rpi refer to the guide 
below.

### Reading The Clock

This clock displays 5 different time periods in binary. From the top 
down here is the order: 

* Row 1 - Current Month 
* Row 2 - Day of the month 
* Row 3 - blank 
* Row 4 - Hour of the day (12 or 24 hr format) 
* Row 5 - Minutes of the hour 
* Row 6 - Seconds of the minute 
* Rows 7-8 - flashes when the alarm is triggered

### Setting the Alarm

To set the alarm load the web interface (port 8000 by default). There is 
a text box to set the alarm time at the bottom of the page. The alarm 
time must be in the 24 hour time format. Example _15:30_.

### Adjusting the settings

When you load the web interface (port 8000 by default) you can visit the Settings page to adjust the color of each row, as well as toggle the 24 hour clock on/off. 
