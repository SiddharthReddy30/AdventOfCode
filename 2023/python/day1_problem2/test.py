import pytest
import pathlib
from solution import caliberator, find_caliberation_value
file_path = pathlib.Path('./input_set_1.txt')
file_path2 = pathlib.Path('./input_set_2.txt')
def test1():
    texts=["two1nine","eightwothree","abcone2threexyz","xtwone3four","4nineeightseven2","zoneight234","7pqrstsixteen","gtlbhbjgkrb5sixfivefivetwosix"]
    caliberations =[29, 83, 13, 24, 42, 14, 76, 56]
    for index,text in enumerate(texts):
        assert find_caliberation_value(text)==caliberations[index]
def test2() :
    assert caliberator(file_path) == 281

def test3() :
    print(caliberator(file_path2))