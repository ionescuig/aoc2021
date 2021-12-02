input_file = 'input.txt'
with open(input_file, 'r') as file:
    my_list = file.read().splitlines()
    new_list = [item.split() for item in my_list]
    horizontal = 0
    depth = 0
    aim = 0
    for action, size in new_list:
        if action == 'forward':
            horizontal += int(size)
            depth += aim * int(size)
        elif action == 'up':
            aim -= int(size)
        elif action == 'down':
            aim += int(size)
    print(horizontal, depth, horizontal * depth)
