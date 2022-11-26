from digitalio import DigitalInOut, Direction, Pull
import microcontroller as uc
import board as brd
pins = tuple([eval(f"brd.{pin}") for pin in dir(uc.pin)[2:]])
pins_io = [ DigitalInOut(pin) for pin in pins ]
pins_flags = [False]*len(pins_io)

for io in pins_io:
    io.pull = Pull.DOWN
#_ = [print(f"{pins[i]} ---> {io.value}") for i,io in enumerate(pins_io)]
for i,io in enumerate(pins_io):
    if io.value is True:
        print(f"{pins[i]} PULL DOWN failed")

for io in pins_io:
    io.pull = Pull.UP
#_ = [print(f"{pins[i]} ---> {io.value}") for i,io in enumerate(pins_io)]
for i,io in enumerate(pins_io):
    if io.value is False:
        print(f"{pins[i]} PULL UP failed")
while True:
    for i,io in enumerate(pins_io):
        if io.value is False and pins_flags[i] is False:
            pins_flags[i] = 'PASS'
            print(f"{pins[i]} PASS!")
