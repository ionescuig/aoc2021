input_file = 'input.txt'
with open(input_file, 'r') as file:
    mylist = file.read().splitlines()

gamma = []
for _idx, number in enumerate(mylist[0]):
    lst = [el[_idx] for el in mylist]
    gamma.append(max(lst, key=lst.count))
epsilon = ['1' if i == '0' else '0' for i in gamma]
gamma = int(''.join(gamma), 2)
epsilon = int(''.join(epsilon), 2)
print(gamma, epsilon, gamma * epsilon)
