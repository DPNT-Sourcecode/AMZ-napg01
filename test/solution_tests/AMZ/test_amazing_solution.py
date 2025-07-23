from solutions.AMZ.amazing_solution import AmazingSolution


class TestSum():
    def test_io(self):
        solution = AmazingSolution()
        generated_maze = solution.amazing_maze(4, 3, {})
        assert generated_maze == """
.--.--.--.--.  .--.--.--.--.
I     I     I              I
:  :  :  :  :  :  :--:--:--.
I  I  I  I  I  I           I
:  :  :  :  :  :--:  :--:  .
I  I  I  I  I     I     I  I
:  :  :  :  :--:  :--:--:  .
I  I  I  I     I        I  I
:  :  :  :--:  :--:--:  :  .
I  I  I     I  I     I  I  I
:  :  :--:  :  :  :  :  :  .
I  I     I  I  I  I  I  I  I
:  :--:  :  :  :  :  :  :  .
I  I  I  I  I  I  I  I  I  I
:  :  :  :  :  :  :  :  :  .
I  I  I  I  I  I  I  I  I  I
:  :  :  :  :  :  :  :  :  .
I     I     I     I     I  I
:--:--:--:--:--:--:--:--:  .
""".lstrip()

