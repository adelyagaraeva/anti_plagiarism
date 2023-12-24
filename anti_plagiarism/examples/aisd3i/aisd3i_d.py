
n_1 = int(input())
lst_1 = sorted([int(i) for i in input().split()])
n_2 = int(input())
lst_2 = sorted([int(i) for i in input().split()])
n_3 = int(input())
lst_3 = sorted([int(i) for i in input().split()])
n_4 = int(input())
lst_4 = sorted([int(i) for i in input().split()])
m_max = max(max(lst_1[0], lst_2[0]), max(lst_3[0], lst_4[0]))
m_min = min(min(lst_1[0], lst_2[0]), min(lst_3[0], lst_4[0]))
it_1, it_2, it_3, it_4 = 0, 0, 0, 0
res_it = [0, 0, 0, 0]
while(True):
    if (it_1 >= n_1 or it_2 >= n_2 or it_3 >= n_3 or it_4 >= n_4):
        break
    new_max = max(max(lst_1[it_1], lst_2[it_2]), max(lst_3[it_3], lst_4[it_4]))
    new_min = min(min(lst_1[it_1], lst_2[it_2]), min(lst_3[it_3], lst_4[it_4]))
    #print(abs(new_min - new_max), abs(m_min - m_max))
    if (abs(new_min - new_max) < abs(m_min - m_max)):
        res_it = [it_1, it_2, it_3, it_4]
        m_min = new_min
        m_max = new_max
    #print(res_it)
    if (new_min == lst_1[it_1] and it_1 <= n_1 - 1):
        it_1 += 1
    if (new_min == lst_2[it_2] and it_2 <= n_2 - 1):
        it_2 += 1
    if (new_min == lst_3[it_3] and it_3 <= n_3 - 1):
        it_3 += 1
    if (new_min == lst_4[it_4] and it_4 <= n_4 - 1):
        it_4 += 1
print(lst_1[res_it[0]], lst_2[res_it[1]], lst_3[res_it[2]], lst_4[res_it[3]])
