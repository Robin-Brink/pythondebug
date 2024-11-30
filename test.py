import GPIO
import time

encoder_value = 0

last_clk_state = 0

CLK = 5   # GPIO 5 (Pin 29)
DT = 6    # GPIO 6 (Pin 31)
SW = 16   # GPIO 16 (Pin 36)

try:
    print("Rotary encoder test running. Press Ctrl+C to stop.")
    while True:
        clk_state = GPIO.input(CLK)
        dt_state = GPIO.input(DT)

        # Detect rotation
        if clk_state != last_clk_state:
            if dt_state != clk_state:
                encoder_value += 3
                print("Rotary Encoder Value:", encoder_value)
            else:
                encoder_value -= 3
                print("Rotary Encoder Value:", encoder_value)

        last_clk_state = clk_state

        # Check for button press
        if GPIO.input(SW) == GPIO.LOW:
            print("Switch Pressed")
            time.sleep(0.2)  # Debounce the button press

        time.sleep(0.01)  # Small delay to prevent high CPU usage

except KeyboardInterrupt:
    print("\nTest stopped by user.")

finally:
    GPIO.cleanup()
    print("GPIO cleaned up.")

