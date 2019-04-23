import numpy as np
import time


# 思路：先创建一行行list，再使用np.array()使之转换为矩阵
# 未处理行数：24743，和到一处有49486，处理过后行数：5093


def DealData(filename):
    Onefiled = []
    Twofiled = []
    # pos = dict()
    out_pos = []
    with open(filename, 'r') as f:
        while True:
            in_pos = dict()
            lines = f.readline()
            if not lines:
                break
                pass
            p_tmp, E_tmp = [str(i) for i in lines.split()]  # 将整形数据分割处理，如果分割符是空格，
            # 括号里就不用传入参数，如果是逗号，则传入‘，’字符
            Onefiled.append(p_tmp)  # 添加新读取的数据
            Twofiled.append(E_tmp)
            in_pos[p_tmp] = E_tmp
            out_pos.append(in_pos)
            pass
        # new_Onefiled = set(Onefiled)
        # new_Twofiled = set(Twofiled)
        # c = list(new_Onefiled | new_Twofiled)
        all_filed = Onefiled + Twofiled
        c = set(all_filed)
        pass
    return c, out_pos, all_filed

'''
def Calculatedegree(data1,data2):
    zero_array = np.zeros(5093,int)
    zero_list = list(zero_array)
    new_dict = dict(zip(data1,zero_list))
    pass
'''

if __name__ == '__main__':
    filename = 'DIP2010.txt'
    data1, data2, data3 = DealData(filename)
    m = np.zeros(shape=(5093, 5093), dtype=np.int)
    data1 = list(data1)
    data1.sort()  # 用于解决每次索引不同的问题

    # 度的矩阵
    for i in data2:
        data2_list1 = list(i)
        data2_list2 = list(i.values())
        p_index = data2_list1[0]
        q_index = data2_list2[0]
        new_p_index = data1.index(p_index)
        new_q_index = data1.index(q_index)
        m[new_p_index][new_q_index] = 1
        m[new_q_index][new_p_index] = 1

    '''
    :param data1 5093
    :param data2 24743
    :param data3 49486
    '''

    # 计算度
    degree = []
    for i, j in zip(data1,data3):
        temp = 0
        if i == j:
            temp += 1
        else:
            pass
        degree.append(temp)
    degree_dict = dict(zip(data1, degree))

    # 计算ECC
    common = np.zeros(shape=(5093, 5093), dtype=np.int)
    for i in range(5093):
        for j in range(5093):
            if i is not j and m[i][j] is 1:
                for k in range(5093):
                    if k is not i and k is not j and m[i][k] * m[j][k] is 1:
                        common[i][j] += 1
                        common[j][i] += 1
                    else:
                        pass
            else:
                pass
    print(common)
    print('ok')

