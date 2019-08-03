import os
import pytest

from pytentiostat.reporter import save_data_to_file


@pytest.mark.parametrize("input,expected",
                         [
                             ([[1, 0, 0]],
                              "Time(s),Voltage(V),Current(mA)\n1,0,0\n1,0,0\n"),
                             ([[1, 0, 0], [2, 0, 0]],
                              "Time(s),Voltage(V),Current(mA)\n1,0,0\n1,0,0\n2,0,0"),
                         ]
                         )
def test_reporter(input, expected, tmpdir):
    file = os.path.join(tmpdir, 'testfile.txt')
    save_data_to_file([[1,0,0]], filename=file)
    with open(file, "r") as f:
        actual = f.read()
    assert expected == actual
