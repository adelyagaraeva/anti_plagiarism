def mindiff(str1, str2, str3, str4, first_r, two_r, three_r, num_four_r, diff):
    for i in range(len(str1)):
        two = 0
        three = 0
        num_four = 0
        first = i
        while str2[two] < str1[i] + 1 and two < len(str2):
            if two >= len(str2):
                break
            two = two + 1
        while str3[three] < str1[i] + 1:
            if three >= len(str3):
                break
            three = three + 1
        while str4[num_four] < str1[i] + 1 and num_four < len(str4):
            num_four= num_four+ 1
        two = max(two - 1, 0)
        three = max(three - 1, 0)
        num_four= max(num_four- 1, 0)
        diff0 = - min((str1[first], str2[two], str3[three], str4[num_four])) + max((str1[first], str2[two], str3[three], str4[num_four]))
        if diff0 < diff:
            diff = diff0
            first_r = first
            two_r = two
            three_r = three
            num_four_r = num_four
    return first_r, two_r, three_r, num_four_r, diff
n1 = int(input())
str1 = list(map(int, input().split()))
n2 = int(input())
str2 = list(map(int, input().split()))
n3 = int(input())
str3 = list(map(int, input().split()))
n4 = int(input())
str4 = list(map(int, input().split()))
delta = 10**6
str1.sort()
str3.sort()
str2.sort()
str4.sort()
first_r = 0
three_r = 0
num_four_r = 0
two_r = 0
three_r = 0
num_four_r = 0
first_r, two_r, three_r, num_four_r, delta = mindiff(str1, str2, str3, str4, first_r, two_r, three_r, num_four_r, delta)
two_r, three_r, num_four_r, first_r,delta = mindiff(str2, str3, str4, str1, two_r, three_r, num_four_r, first_r, delta)
three_r, num_four_r, first_r, two_r, delta = mindiff(str3, str4, str1, str2, three_r, num_four_r, first_r, two_r,  delta)
num_four_r, first_r, two_r, three_r, delta = mindiff(str4, str1, str2, str3, num_four_r, first_r, two_r, three_r, delta)
print(str1[first_r], str2[two_r], str3[three_r], str4[num_four_r])