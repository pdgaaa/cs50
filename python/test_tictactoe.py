from tictactoe import winner

def test_nowinner_diag_backslash():
    board=[
        ["O","*","X"],
        ["*","O","*"],
        ["O","*","X"]
    ]
    assert winner(board) == ""

def test_nowinner_diag_slash():
    board=[
        ["*","*","X"],
        ["*","O","*"],
        ["O","*","*"]
    ]
    assert winner(board) == ""

def test_nowinner_column():
    board=[
        ["X","*","*"],
        ["X","*","*"],
        ["O","*","*"]
    ]
    assert winner(board) == ""

def test_nowinner_line():
    board=[
        ["X","O","X"],
        ["*","*","*"],
        ["*","*","*"]
    ]
    assert winner(board) == ""

def test_winner_line_top():
    board=[
        ["X","X","X"],
        ["*","*","*"],
        ["*","*","*"]
    ]
    assert winner(board) == "X"

def test_winner_middle_line():
    board=[
        ["*","*","*"],
        ["O","O","O"],
        ["*","*","*"]
    ]
    assert winner(board) == "O"

def test_winner_bottom_line():
    board=[
        ["*","*","*"],
        ["*","*","*"],
        ["X","X","X"]
    ]
    assert winner(board) == "X"

def test_winner_diagonal_slash():
    board=[
        ["X","*","O"],
        ["*","O","*"],
        ["O","*","X"]
    ]
    assert winner(board) == "O"

def test_winner_middle_column():
    board=[
        ["O","X","*"],
        ["O","X","*"],
        ["*","X","O"]
    ]
    assert winner(board) == "X"

def test_winner_diagonal_backslash():
    board=[
        ["X","*","*"],
        ["*","X","*"],
        ["*","*","X"]
    ]
    assert winner(board) == "X"
