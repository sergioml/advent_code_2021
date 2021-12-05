def diving():
    PATH_DATA = './data/dive.txt'
    initial_position = [0, 0]

    with open(PATH_DATA, 'r') as data:
        for instruction in data:
            temp_instruction = instruction.split(' ')
            if len(temp_instruction) > 1:
                if temp_instruction[0] == 'forward':
                    initial_position[0] += int(temp_instruction[1])
                elif temp_instruction[0] == 'down':
                    initial_position[1] -= int(temp_instruction[1])
                elif temp_instruction[0] == 'up':
                    initial_position[1] += int(temp_instruction[1])

    print(initial_position[0] * initial_position[1])

def diving_part_two():
    PATH_DATA = './data/dive.txt'
    initial_position = [0, 0, 0]

    with open(PATH_DATA, 'r') as data:
        for instruction in data:
            temp_instruction = instruction.split(' ')
            if len(temp_instruction) > 1:
                if temp_instruction[0] == 'forward':
                    initial_position[0] += int(temp_instruction[1])
                    initial_position[1] += int(temp_instruction[1]) * initial_position[2]    
                elif temp_instruction[0] == 'down':
                    initial_position[2] += int(temp_instruction[1])
                elif temp_instruction[0] == 'up':
                    initial_position[2] -= int(temp_instruction[1])
                    

    print(initial_position[0] * initial_position[1])

if __name__ == '__main__':
    # diving()
    diving_part_two()