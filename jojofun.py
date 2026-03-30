import time


def loading_animation(progress, percent_range, speed1, speed2, message):
    print("Loading", end="", flush=True)

    for i in range(5):
         print(".", end="", flush=True)
    time.sleep(speed1)

    for i in range(progress):
        bar = "#" * i
        spaces = " " * (20 - i)
        percent = i * percent_range

        print(f"\rLoading [{bar}{spaces}] {percent}%", end="", flush=True)
        time.sleep(speed2)
    print(f"\n{message}\n")




def loading_dots(count, speed):
    for i in range(count):
        print(".", end="", flush=True)
        time.sleep(speed)




def rev_loading_animation(progress, percent_range, speed1, speed2, message):
    print("Loading", end="", flush=True)

    for i in range(5):
         print(".", end="", flush=True)
    time.sleep(speed1)

    for i in range(progress):
        bar = "#" * (progress - i-1)
        spaces = " " * i
        percent = int((progress - i - 1) / (progress - 1) * 100)
        percent_str = f"{percent:3d}%"

        print(f"\rLoading [{bar}{spaces}] {percent_str}", end="", flush=True)
        time.sleep(speed2)
    print(f"\n{message}\n")
