def mindiff(str1, str2, str3, str4, first_r, two_r, three_r, num_four_r, diff):
    two = 0
    three = 0
    num_four= 0
    for i in range(len(str1)):
        first = i
        while two < len(str2) and str2[two] <= str1[i]:
            two += 1
        while three < len(str3) and str3[three] <= str1[i]:
            three += 1
        while num_four< len(str4) and str4[num_four] <= str1[i]:
            num_four+= 1
        two = max(two - 1, 0)
        three = max(three - 1, 0)
        num_four= max(num_four- 1, 0)
        diff0 = max((str1[first], str2[two], str3[three], str4[num_four])) - min((str1[first], str2[two], str3[three], str4[num_four]))
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
str1.sort()
str2.sort()
str3.sort()
str4.sort()
first_r = 0
two_r = 0
three_r = 0
num_four_r = 0
diff = 10**6
first_r, two_r, three_r, num_four_r, diff = mindiff(str1, str2, str3, str4, first_r, two_r, three_r, num_four_r, diff)
two_r, three_r, num_four_r, first_r, diff = mindiff(str2, str3, str4, str1, two_r, three_r, num_four_r, first_r, diff)
three_r, num_four_r, first_r, two_r, diff = mindiff(str3, str4, str1, str2, three_r, num_four_r, first_r, two_r,  diff)
num_four_r, first_r, two_r, three_r, diff = mindiff(str4, str1, str2, str3, num_four_r, first_r, two_r, three_r, diff)
print(str1[first_r], str2[two_r], str3[three_r], str4[num_four_r])