#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time: 2021-03-02 0:27
# @Author: Yi
# @File: JJ
import pytest


def func(x):
    return x + 1
@pytest.mark.parametrize('a,b',[
    (1,2),
    (10,20),
    ('a','a1'),
    (3,4),
    (5,6)])

def test_answer(a,b):
    assert func(a) == b

def test_answer1():
    assert func(1) == 2

def test_answer2():
    assert func(3) == 4

@pytest.fixture()
def login():
    username='Jerry'
    return username

class TestDemo:
    def test_a(self,login):
        print(f"a   username={login}")
    def test_b(self):
        print('b')
    def test_c(self,login):
        print(f"c   username={login}")

if __name__=='__main__':
    pytest.main(['test_pytest1.py::TestDemo','-v'])