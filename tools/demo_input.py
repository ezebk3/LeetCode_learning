import sys


def sort_dict():
    t_dict = {"A": 3, "B": 1, "C": 2}

    S_dict = sorted(t_dict.items(), key=lambda i: i[1])
    print(S_dict)


if __name__ == '__main__':

    sort_dict()
    # input_list = []
    # while True:
    #     m = sys.stdin.readline().strip()
    #     if m == '':
    #         break
    #     input_list.append(m)
    #
    # print(input_list)
