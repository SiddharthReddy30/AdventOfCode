import pytest
import pathlib
from solution import caliberator, find_caliberation_value
file_path = pathlib.Path('./input_set_1.txt')
file_path2 = pathlib.Path('./input_set_2.txt')
def test1():
    texts=["1abc2","pqr3stu8vwx","a1b2c3d4e5f","treb7uchet"]
    caliberations =[12,38,15,77]
    for index,text in enumerate(texts):
        assert find_caliberation_value(text)==caliberations[index]
def test2() :
    assert caliberator(file_path) == 142

def test3() :
    print(caliberator(file_path2))