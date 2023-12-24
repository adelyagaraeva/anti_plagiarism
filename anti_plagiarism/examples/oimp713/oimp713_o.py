with open('input.txt', 'r', encoding='utf-8') as file:
    nineth_class = []
    tenth_class = []
    eleventh_class = []
    for line in file:
        surname, name, class_v, score = input().split()
        if class_v == '9':
            nineth_class.append(int(score))
        elif class_v == '10':
            tenth_class.append(int(score))
        else:
            eleventh_class.append(int(score))
    print(sum(nineth_class) / len(nineth_class), sum(tenth_class) / len(tenth_class), sum(eleventh_class) / len(eleventh_class))