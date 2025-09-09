from exercises import *

import pytest
import random
import math
import os

def test_most_repeating():
    lst = ["a", 7, 3, 1, 4, "a", 14, (1, 2), 898, -2, 3, -42, "a"]

    result = most_repeating(lst)

    assert isinstance(result, str)
    assert result == "a"

    for _ in range(5):
        n = random.randint(10, 20)
        n_b = random.randint(0, 5)
        n_e = random.randint(5, 15)
        nums = list(set([random.randint(n_b, n_e) for i in range(n)]))

        m = random.randint(0, len(nums) - 1)
        nums.append(nums[m])
        result = most_repeating(nums)
        assert isinstance(result, int)
        assert result == nums[m]

def test_reverse_number():
    assert isinstance(reverse_number(10), bool)
    assert reverse_number(121)
    assert not reverse_number(123)

    for _ in range(5):
        n = random.randint(10, 1000)
        assert reverse_number(n) == (int(''.join(reversed(str(n)))) == n)

def test_is_vowel():
    assert isinstance(is_vowel('a'), bool)
    for letter in 'aeiouy':
        assert is_vowel(letter)
    for letter in 'qwrtpsdfghjklzxcvbnm':
        assert not is_vowel(letter)

def test_multiple_filter():
    assert isinstance(multiple_filter([], 1), list)
    assert multiple_filter([1, 5, 4, 18, 6, 9, -2, -3], 2) == [1, 5, 9, -3]
    assert multiple_filter([5, 13, 19, 11], 3) == [5, 13, 19, 11]
    assert multiple_filter([2, 4, -6, 8], 2) == []

def test_repeat_count():
    assert isinstance(repeat_count(""), dict)
    sentence = "He main thing was to exchange ideas and contribute to the society,  \
	and therefore not to remain silent and not X hide your personal opinion"
    result = {'and': 3, 'contribute': 1, 'hide': 1, 'silent': 1, 'to': 3, 'not': 2, \
        'exchange': 1, 'ideas': 1, 'thing': 1, 'remain': 1, 'personal': 1, 'therefore': 1, \
        'opinion': 1, 'society': 1, 'x': 1, 'the': 1, 'main': 1, 'was': 1, 'your': 1, 'he': 1}
    assert repeat_count(sentence) == result

def test_descending_sort():
    assert isinstance(descending_sort([]), list)
    lst = [5, 9, 1, -5, 0]
    res = [9, 5, 1, 0, -5]
    assert descending_sort(lst) == res

def test_factorial():
    assert isinstance(factorial(0), int)
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120
    assert factorial(7) == 5040

    for _ in range(5):
        n = random.randint(1, 15)
        assert factorial(n) == math.factorial(n)

def test_english_alphabet():
    res = english_alphabet()
    assert isinstance(res, list)
    assert len(res) == 26
    assert res == ['a', 'b', 'c', 'd', 'e', 'f', 'g', \
        'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', \
        'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def test_average():
    assert isinstance(average([1], 1), float)
    assert average([], 0) == 0
    assert average([1, 2, 3], 0) == 2.
    assert average([1, 2, -5], 3) == -0.667

def test_word_in_file():
    name = 'tmp.txt'
    def check(data, res):
        with open(name, 'w') as f:
            for l in data:
                f.write(l)
        try:
            assert word_in_file(name, 'secret') == res
        except:
            os.remove(name)
            raise

    check([], False)
    check(['a'], False)
    check(['a\n', 'secretdhdy\n', 'asdfadf\n', '1232'], True)
    os.remove(name)
