#!/usr/bin/env python3
import collections

def from_num_to_rom(number:int) -> str:
	roman_converter_dictionary = collections.OrderedDict([('I'*5, 'V'), ('V'*2,'X'), ('X'*5,'L'), ('L'*2,'C'),('C'*5,'D'),
	('D'*2,'M'),('DCCCC','CM'),('CCCC','CD'),('LXXXX','XC'),('XXXX','XL'),('VIIII','IX'),('IIII','IV')])
	result = 'I'*int(number)
	for key, val in roman_converter_dictionary.items():
		result = result.replace(key,val)
	return result

def from_rom_to_num(result:str) -> str:
	numbers_converter_dictionary = collections.OrderedDict([('CM','900 '),('CD','400 '),('XC','90 '),('XL','40 '),('IX','9 '),('IV','4 '),
	('I', '1 '),('V','5 '),('X','10 '),('L','50 '),('C','100 '),('D','500 '),('M','1000 ')])
	for key, val in numbers_converter_dictionary.items():
		result = result.replace(key, val)

	result = result.strip()
	result = result.split(' ')
	result = list(map(int, result))
	result = sum(result)

	return result

def input_number() -> int:
	return input('Enter your number: ')

def input_roman_number() -> str:
	return input('Enter your rome number: ')


print(from_num_to_rom(input_number()))
print(from_rom_to_num(input_roman_number()))
