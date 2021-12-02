input_file = 'input.txt'
with open(input_file, 'r') as file:
    mylist = file.read().splitlines()
    print(mylist[0:4], mylist[-1])
    count = -1
    old_value = 0
    for i in range(len(mylist)-2):
        value = int(mylist[i]) + int(mylist[i+1]) + int(mylist[i+2])
        if value > old_value:
            count += 1
        old_value = value
    print(count)
