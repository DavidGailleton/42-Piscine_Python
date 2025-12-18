def ft_water_reminder():
    print("Days since last watering:", end=" ")
    x = int(input())
    if x > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")
