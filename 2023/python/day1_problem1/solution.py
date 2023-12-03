import pathlib

def caliberator(filepath:pathlib.Path):
    caliberation = 0
    with open(filepath)as file:
        lines = file.readlines() 
    for line in lines:
        caliberation += find_caliberation_value(line)
    return caliberation

def find_caliberation_value(line:str):
    digits = []
    for letter in line:
        if letter.isdigit():
            digits.append(int(letter))
    caliberation = (digits[0]*10)+digits[-1]
    return caliberation
    