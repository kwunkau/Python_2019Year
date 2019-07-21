# -*- coding: utf-8 -*-
import math


# 算数平均数
def avg(num_list):
    return sum(num_list)/len(num_list)


# 几何平均数
def avg_geometry(num_list):
    sum = 1
    if num_list and len(num_list) > 0:
        length = len(num_list)
        for num in num_list:
            sum *= num
        return math.pow(sum, 1.0/length)


# 中位数/分位数
def median(num_list, split_num=2):
    num_list.sort()
    length = len(num_list)
    result = []
    if not split_num or split_num == 2:
        if length % 2 == 0:
            return (num_list[int(length/2-1)] + num_list[int(length/2)])/2
        else:
            return num_list[length/2-1]
    else:
        if length % split_num == 0:
            i = split_num
            while i > 1:
                result.append((num_list[int(length / i - 1)] + num_list[int(length / i)]) / 2)
                i -= 1
            return result
        else:
            i = split_num
            while i > 1:
                result.append(num_list[int(length / i - 1)])
                i -= 1
            return result


# 平均差
def average_deviation(num_list):
    avg_num = avg(num_list)
    return sum([abs(num-avg_num) for num in num_list])/len(num_list)


# 方差
def variance(num_list):
    avg_num = avg(num_list)
    return sum([math.pow(num - avg_num, 2) for num in num_list])/len(num_list)


# 标准差
def standard_deviation(num_list):
    return math.pow(variance(num_list), 1.0/2)


# 离散系数 又叫变异系数 标准差/平均数
def coefficient_dispersion(num_list):
    return standard_deviation(num_list)/avg(num_list)


# 众数
def mode(num_list):
    dict = {}
    result = []
    max = 0
    if num_list and len(num_list) > 0:
        for num in num_list:
            if num in dict:
                dict[num] += 1
            else:
                dict[num] = 1
        d1 = sorted(dict.values(), reverse=True)
        max = d1[0]
        for num in dict:
            count = dict.get(num, 0)
            if count == max:
                result.append(num)
    return result


# 异众比率 不是众数在总数占比
def variation_ratio(num_list):
    count = 0
    mode_nums = mode(num_list)
    for num in num_list:
        if num not in mode_nums:
            count += 1
    return count/len(num_list)


if __name__ == '__main__':
    list = [2, 10, 60, 6, 5, 6]
    # 以下 在numpy都有实现
    print(mode(list))
    print(avg(list))
    print(avg_geometry(list))
    print(median(list))
    print(average_deviation(list))
    print(variance(list))
    print(standard_deviation(list))
    print(variation_ratio(list))
    print(coefficient_dispersion(list))
    print(median(list, split_num=3))
