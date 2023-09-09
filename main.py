import pytest

class MyArray:

  def __init__(self, arr):
    self.array = arr

  def size(self):
    return len(self.array)

  def sum(self):
    return sum(self.array)

@pytest.fixture
def setup_variables():
  return [1, 3, 2], [3, 7, 3, 4], [200, 10, 1]

def test_size(setup_variables):
  arr1, arr2, arr3 = setup_variables
  assert MyArray(arr1).size() == 3
  assert MyArray(arr2).size() == 4
  assert MyArray(arr3).size() == 3

def test_sum(setup_variables):
  arr1, arr2, arr3 = setup_variables
  assert MyArray(arr1).sum() == 6
  assert MyArray(arr2).sum() == 17
  assert MyArray(arr3).sum() == 211
