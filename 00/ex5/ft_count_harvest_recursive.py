def ft_count_harvest_recursive(x: int = -1):
    if x < 0:
        print("Days until harvest:", end=" ")
        x = int(input())
        ft_count_harvest_recursive(x)
        print("Harvest time!")
    elif x > 0:
        ft_count_harvest_recursive(x - 1)
        print("Day", x)
