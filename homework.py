from itertools import combinations as cm

data = "444996, 699990, 666690, 096904, 600644, 640646, 606469, 409694, 666094, 606490"
# data = "6900690040, 4690606946, 9990494604"
def pos_average(s):
    s = list(map(lambda x: x.strip(), data.split(',')))
    count = 0
    len_of_comb = len(list(cm(s, 2)))
    for number1, number2 in list(cm(s, 2)):
        for i in range(len(number1)):
            if number1[i] == number2[i]:
                count += 1
    return count / (len_of_comb * len(s[0])) * 100

chislo = pos_average(data)
print(chislo)