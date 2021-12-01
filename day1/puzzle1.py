input_file = 'input.txt'
with open(input_file, 'r') as file:
    count = -1
    old_line = 0
    for line in file:
        if int(line) > old_line:
            count += 1
        old_line = int(line)
    print(count)
