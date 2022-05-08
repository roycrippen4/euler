# P022

def main():
    alpha_num_dict = {chr(x + 96): x for x in range(1, 27)}
    names = get_list_names()
    answer = 0
    for name in names:
        answer += (names.index(name) + 1) * get_name_value(name, alpha_num_dict)
    print(answer)  # 871198282


def get_name_value(name: str, d: dict):
    value = 0
    name = name.lower()
    for letter in name:
        value += d[letter]
    return value


def get_list_names():
    with open('/supplementary_files/p022_names.txt') as file:
        names = file.read()
        split_names = names.split(',')
        strip_names = []
        for name in split_names:
            lowercase_name = name.lower()
            strip_names.append(lowercase_name.strip('"'))
            strip_names.sort()
        return strip_names


if __name__ == "__main__":
    main()
