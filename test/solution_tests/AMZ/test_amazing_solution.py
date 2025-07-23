from solutions.AMZ.amazing_solution import AmazingSolution


class TestSum():
    def test_io(self):
        solution = AmazingSolution()
        generated_maze = solution.amazing_maze(5, 7, {})
        assert generated_maze == """
.--.--.--.  .--.--.--.
I        I           I
:  :  :  :  :  :--:--.
I  I  I  I  I        I
:  :  :  :  :--:  :  .
I  I  I  I     I  I  I
:  :  :  :--:  :--:  .
I  I  I     I     I  I
:  :  :--:  :--:  :  .
I  I     I        I  I
:--:--:--:--:--:--:  .
""".lstrip()

    def test_entry_column(self):
        solution = AmazingSolution()
        generated_maze = solution.amazing_maze(6, 9, { "ENTRY_COLUMN": "1" })
        assert generated_maze.split("\n")[0] == ".  .--.--.--.--.--.--.--.--."

    def test_random_number_generation(self):
        solution = AmazingSolution()
        generated_maze = solution.amazing_maze(13, 14, { "LEGACY_RANDOM_MAGIC_NUMBER": "0.0" })
        assert generated_maze == """
.  .--.--.--.--.--.--.--.--.--.--.--.--.--.
I                                         I
:--:--:--:--:--:--:--:--:--:--:--:--:--:  .
I                                         I
:  :--:--:--:--:--:--:--:--:--:--:--:--:--.
I                                         I
:--:--:--:--:--:--:--:--:--:--:--:--:--:  .
I                                         I
:  :--:--:--:--:--:--:--:--:--:--:--:--:--.
I                                         I
:--:--:--:--:--:--:--:--:--:--:--:--:--:  .
I                                         I
:  :--:--:--:--:--:--:--:--:--:--:--:--:--.
I                                         I
:--:--:--:--:--:--:--:--:--:--:--:--:--:  .
I                                         I
:  :--:--:--:--:--:--:--:--:--:--:--:--:--.
I                                         I
:--:--:--:--:--:--:--:--:--:--:--:--:--:  .
I                                         I
:  :--:--:--:--:--:--:--:--:--:--:--:--:--.
I                                         I
:--:--:--:--:--:--:--:--:--:--:--:--:--:  .
I                                         I
:  :--:--:--:--:--:--:--:--:--:--:--:--:--.
I                                         I
:  :--:--:--:--:--:--:--:--:--:--:--:--:--.
""".lstrip()

    def test_chest_at_dead_end(self):
        solution = AmazingSolution()
        generated_maze = solution.amazing_maze(3, 4, { "ENTRY_COLUMN": "1", "DEAD_END_ON_LAST_ROW_BEHAVIOUR": "CREATE_TREASURE" })
        assert generated_maze == """
.  .--.--.--.
I     I     I
:  :  :  :  .
I  I  I  I  I
:  :  :--:  .
I<>I        I
:--:--:  :--.
""".lstrip()

