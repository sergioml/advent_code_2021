def get_increases_depth():
    PATH_DATA = "data/depths.txt"
    max_number_increases = 0
    previous_number = 0

    with open(PATH_DATA) as depths:
        for i, depth in enumerate(depths):
            if i != 0:
                if (int(depth) - previous_number) > 0:
                    max_number_increases += 1
            previous_number = int(depth.rstrip())
    print(max_number_increases)

def get_increses_windows():
    PATH_DATA = "data/depths.txt"
    max_number_increases = 0
    file = open(PATH_DATA, 'r')
    depths = [ int(d) for d in file ]
    previous_sum = 0
    current_sum = 0

    for i in range(2, len(depths)):
        if i == 2:
            previous_sum = sum(depths[:i+1])
            continue
        else:
            current_sum = sum(depths[i-2:i+1])
        
        if current_sum > previous_sum:
            max_number_increases += 1
        
        previous_sum = current_sum

    print(max_number_increases)


if __name__ == "__main__":
    # get_increases_depth() # Part one
    get_increses_windows()
