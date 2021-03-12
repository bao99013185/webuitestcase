#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time: 2021-03-03 0:45
# @Author: Yi
# @File: test_param
import pytest


class TestParam:
    @pytest.mark.parametrize(["a","b"],[
                            (10,20),
                            (10,5),
                            (3,9)

                              ])
    def test_data1(self,a,b):
        print(a+b)
    # def test_data2(self):
    #     a=11
    #     b=20
    #     print(a+b)