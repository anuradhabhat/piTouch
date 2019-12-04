# piTouch
Count Cap1188 touch instances, results displayed in Matplotlib 

DESCRIPTION:
This is a simple python script to count the touch instances on a CAP1188 sensor's pins through the I2C interface and display the cumulative count in a Matplotlib bar graph.

SUGGESTED SYSTEM REQUIREMENTS:
1.Raspberry pi with Jessie
2.CircuitPython
3.MatPlotLib

HELPFUL LINKS:
https://www.raspberrypi.org/blog/raspbian-jessie-is-here/
https://learn.adafruit.com/adafruit-cap1188-breakout/python-circuitpython
https://matplotlib.org/

TROUBLESHOOTING TIPS:
1.LEDs on the CAP1188 are an easy indicator of touch.
2.If touch is not detected by the CAP1188, disconnect/reconnect the red, black, blue and yellow wires.

FUTURE DEVELOPMENT:
1.Once touch is reliably detected, use this py script to control a game or other program.
