#!/usr/bin/env python
# -*- coding:utf-8 -*-
#__author__ = "Ligq"

import pandas as pd
import numpy as np
#显示所有列
pd.set_option('display.max_columns', None)
#显示所有行
pd.set_option('display.max_rows', None)


if __name__=='__main__':
    file_path='F:/2WORK/123/one.csv'
    v1=pd.read_csv(file_path,encoding='gbk',low_memory=False,header=0)

    vv = v1[(v1['工号'] ==20288913.0]
    vv2 = vv['值'].sum()
    print(vv[['综合类型','薪资项目','来源','值','工号','姓名']])
    print(vv2)

    # data1 = v1[(v1['综合类型']=='固薪') & (v1['发薪单位编码']==282235031748)]
    # data11 = v1[['发薪单位编码','发薪单位名称','预算组织编码']]
    # data12 = data11.drop_duplicates(['发薪单位编码','发薪单位名称','预算组织编码'])
    # data12.to_csv('F:/123/发薪单位名称.csv', index=False, header=True, sep=',', encoding='gbk')

    # data2 = data1.pivot_table(index=['工号','姓名'],values='值',aggfunc=np.sum,fill_value=0)
    # print(data2.sort_values(by='值',ascending=False))

