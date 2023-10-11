#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import deque


# a eviter, car utiliser beaucoup plus de memoire que des boucles
def get_fibonacci_number(index):
	if index == 0:
		return 0
	elif index == 1:
		return 1
	else:
		return get_fibonacci_number(index - 1) + get_fibonacci_number(index - 2)
	## OU:
	# return (
	# 	0 if index == 0 else
	# 	1 if index == 1 else
	# 	get_fibonacci_number(index = 1) + get_fibonacci_number(index - 2)
	# )

def get_fibonacci_sequence(count):
	numbers = [0, 1]
	for i in range(2, count):
		numbers.append(numbers[i - 2] + numbers[i - 1])
	return numbers[:count]

def get_sorted_dict_by_decimals(dictionary):
	# TODO: figure out how this works and compare with correction
	return dict(sorted(dictionary.items(), key=lambda item: item[1] - round(item[1])))

def fibonacci_numbers(length):
	init_values = [0, 1] # transform this into array
	# also take into account length < 2
	for value in init_values[0:length]:
		yield value

	last_elems = deque(init_values) # use deque here
	for _ in range(len(init_values), length): # going from 2 to length makes more sense here
		new_num = last_elems[-1] + last_elems[-2] # also makes more sense here (closer to math notation)
		last_elems.append(new_num) # this is why deque is easier to work with
		last_elems.popleft()
		yield new_num

def build_recursive_sequence_generator(initial_values, function, save_all=False):
	def recursive_func(length):
		for i in range(len(initial_values)): # ou for value in initial_values[0:length]: yield value
			if i >= length:
				return
			yield initial_values[i]

		function_values = deque(initial_values)
		for _ in range(len(function_values), length):
			new_value = function(function_values)
			function_values.append(new_value)
			if not save_all:
				function_values.popleft()
			yield new_value

	return recursive_func


if __name__ == "__main__":
	print([get_fibonacci_number(0), get_fibonacci_number(1), get_fibonacci_number(2)])
	print([get_fibonacci_number(i) for i in range(10)])
	print()

	print(get_fibonacci_sequence(1))
	print(get_fibonacci_sequence(2))
	print(get_fibonacci_sequence(10))
	print()

	spam = {
		2: 2.1,
		3: 3.3,
		1: 1.4,
		4: 4.2
	}
	eggs = {
		"foo": 42.6942,
		"bar": 42.9000,
		"qux": 69.4269,
		"yeet": 420.1337
	}
	print(get_sorted_dict_by_decimals(spam))
	print(get_sorted_dict_by_decimals(eggs))
	print()

	for fibo_num in fibonacci_numbers(10):
		print(fibo_num, end=" ")
	print("\n")

	def fibo_def(last_elems):
		return last_elems[-1] + last_elems[-2]
	fibo = build_recursive_sequence_generator([0, 1], fibo_def)
	for fi in fibo(10):
		print(fi, end=" ")
	print("\n")

	# la consigne disait d'utiliser des fonctions lambda a la place...
	lucas = build_recursive_sequence_generator([2, 1], lambda prev_elems: prev_elems[-1] + prev_elems[-2])
	print(f"Lucas : {[elem for elem in lucas(10)]}")
	perrin = build_recursive_sequence_generator([3, 0, 2], lambda prev_elems: prev_elems[-2] + prev_elems[-3])
	print(f"Perrin : {[elem for elem in perrin(10)]}")
	hofstadter_q = build_recursive_sequence_generator([1, 1], lambda prev_elems: prev_elems[-prev_elems[-1]] + prev_elems[-prev_elems[-2]], True)
	print(f"Hofstadter-Q : {[elem for elem in hofstadter_q(10)]}")
