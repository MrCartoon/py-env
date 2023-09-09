import pytest

class MyArray:

  def __init__(self, arr):
    self.array = arr

  def size(self):
    return len(self.array)

  def sum(self):
    return sum(self.array)


def setup(self):
  self.arr1 = [1, 3, 2]
  self.arr2 = [3, 7, 3, 4]
  self.arr3 = [200, 10, 1]


def test_size(self):
  assert MyArray(self.arr1).size() == 3

def test_sum(self):
  assert MyArray(self.arr1).sum() == 6
