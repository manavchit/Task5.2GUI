import tkinter as tk
import RPi.GPIO as GPIO

# GPIO setup
GPIO.setmode(GPIO.BCM)  # Use BCM pin numbering
red = 18  # GPIO pin for Red LED
yellow = 23  # GPIO pin for Yellow LED
blue = 24  # GPIO pin for Blue LED

GPIO.setup(red, GPIO.OUT)  # Set Red pin as output
GPIO.setup(yellow, GPIO.OUT)  # Set Yellow pin as output
GPIO.setup(blue, GPIO.OUT)  # Set Blue pin as output

# PWM setup
redpwm = GPIO.PWM(red, 1000)  # Initialize PWM on Red pin at 1kHz
yellowpwm = GPIO.PWM(yellow, 1000)  # Initialize PWM on Yellow pin at 1kHz
bluepwm = GPIO.PWM(blue, 1000)  # Initialize PWM on Blue pin at 1kHz

redpwm.start(0)  # Start Red PWM with 0% duty cycle
yellowpwm.start(0)  # Start Yellow PWM with 0% duty cycle
bluepwm.start(0)  # Start Blue PWM with 0% duty cycle

# GUI function to update LED intensities
def update_intensities(event):
    # Get current slider values for each LED
    redintensity = int(redslider.get())
    yellowintensity = int(yellowslider.get())
    blueintensity = int(blueslider.get())

    # Update PWM duty cycle for each LED based on slider value
    redpwm.ChangeDutyCycle(redintensity)
    yellowpwm.ChangeDutyCycle(yellowintensity)
    bluepwm.ChangeDutyCycle(blueintensity)

# GUI creation
root = tk.Tk()  # Create the main window
root.title("LED Intensity Control")  # Set the window title
root.geometry("400x300")  # Set window size

# Red LED intensity slider
redslider = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, command=update_intensities, label="Red")
redslider.pack(pady=10)  # Add padding for spacing

# Yellow LED intensity slider
yellowslider = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, command=update_intensities, label="Yellow")
yellowslider.pack(pady=10)  # Add padding for spacing

# Blue LED intensity slider
blueslider = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, command=update_intensities, label="Blue")
blueslider.pack(pady=10)  # Add padding for spacing

# Exit button
exitbutton = tk.Button(root, text="Exit", command=root.quit)  # Button to exit the GUI
exitbutton.pack(pady=20)  # Add padding for spacing

# Start the GUI event loop
root.mainloop()

# Cleanup GPIO when program exits
GPIO.cleanup()  # Reset GPIO settings
