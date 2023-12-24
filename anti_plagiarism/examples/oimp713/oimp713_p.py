with open('input.txt', 'r', encoding='utf-8') as file:
    n_cl = []
    t_cl = []
    el_cl = []
    for line in file:
        first_name, two_name, class_value, result = input().split()
        if class_value == '10':
            t_cl.append(int(result))
        elif class_value == '9':
            n_cl.append(int(result))
        else:
            t_cl.append(int(result))
    print(sum(n_cl) / len(n_cl))
    print(sum(t_cl) / len(t_cl))
    print(sum(el_cl) / len(el_cl))