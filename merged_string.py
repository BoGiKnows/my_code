'''
At a job interview, you are challenged to write an algorithm to check if a given string, s, can be formed from two other strings, part1 and part2.

The restriction is that the characters in part1 and part2 should be in the same order as in s.

The interviewer gives you the following example and tells you to figure out the rest from the given test cases.
'''

data = 'codewars', 'code', 'wars'
wrong_data = 'codewars', 'cod', 'wars'
data1 = "Can we merge it? Yes, we can!", "an wmreY a!", "Ce eg it? es, wecn"


def is_merge(s, part1, part2):
    if len(s) != len(part1) + len(part2):
        return False
    count = 0
    temp = ''
    for i in s:
        try:
            if (part1 and part2) and (part1[len(temp)] == i and part2[len(temp)] == i):
                temp += i
            elif i in part1 or i in part2:
                if part1 and i == part1[len(temp)]:
                    if temp:
                        part1 = part1[len(temp):]
                        temp = ''
                    part1 = part1.replace(i, '', 1)
                    count += 1
                elif part2 and i == part2[len(temp)]:
                    if temp:
                        part2 = part2[len(temp):]
                        temp = ''
                    part2 = part2.replace(i, '', 1)
                    count += 1
        except Exception:
            return False

    print(part1, part2)
    return not any((part1, part2))

print(is_merge('codewars', 'code', 'code'))
