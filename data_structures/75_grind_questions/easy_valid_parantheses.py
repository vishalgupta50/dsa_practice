def valid_parantheses(istr):
    hash_dict = {'{': 0, '[': 0, '(': 0}
    counter = 0

    n = len(istr)

    for i in range(n):
        if istr[i] in ['{', '[', '(']:
            hash_dict[istr[i]] += 1
        elif istr[i] == '}':
            hash_dict['{'] -= 1
            counter += 1
        elif istr[i] == ']':
            hash_dict['['] -= 1
            counter += 1
        elif istr[i] == ')':
            hash_dict['('] -= 1
            counter += 1

        if i == 0 and counter == 1:
            return False

    for elem in hash_dict.values():
        if elem > 0 or elem < 0:
            return False

    return True

input_str = [
    '[{}{}(]',
    '{[]{()}}',
    '((()',
    '[()]{}{[()(v))]()}a{}a{}',
    '{[]{()}}',
    '({{}}){}[]',
    '}{}{'
]

print(valid_parantheses(input_str[1]))
