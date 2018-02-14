# function must start from "test"

# to run it: "py.test"


import myprogram
import pytest
import shutil  # to copy file
import os


# func version
# def test_doubleit():
#     assert (myprogram.doubleit(10) == 20)
#
# def test_doubleit_type():
#     with pytest.raises(TypeError):  # function rises exception
#         myprogram.doubleit("hello")

# class version

class TestDoubleIt(object):  # starts with Test

    numbers_file_template = "testnums_template.txt"
    numbers_file_testor = "testnums.txt"

    def setup_class(self):
        shutil.copy(TestDoubleIt.numbers_file_template, TestDoubleIt.numbers_file_testor)

    def teardown_class(self):
        os.remove(TestDoubleIt.numbers_file_testor)

    def test_doublelines(self):
        myprogram.doublelines(TestDoubleIt.numbers_file_testor)
        old_vals = [int(line) for line in open(TestDoubleIt.numbers_file_template)]
        new_vals = [int(line) for line in open(TestDoubleIt.numbers_file_testor)]
        for old_val, new_val in zip(old_vals, new_vals):
            assert int(new_val) == 2*int(old_val)

    def test_doubleit(self):
        assert (myprogram.doubleit(10) == 20)

    def test_doubleit_type(self):
        with pytest.raises(TypeError):  # function rises exception
            myprogram.doubleit("hello")
