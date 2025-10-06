from src.main import tally_game
import pytest

def test_a_wins_easy():
    # input sequence: B scores 9 before A finishes at 21
    rallies = ("AB" * 9) + ("A" * 12)
    result = tally_game(rallies)
    assert result == (21, 9, "A")

def test_b_wins_easy():
    # input sequence: A scores 9 before B finishes at 21
    rallies = ("BA" * 9) + ("B" * 12)
    result = tally_game(rallies)
    assert result == (9, 21, "B")

def test_a_wins_deuce():
    # input sequence reaches 20-20, then A takes two consecutive points
    rallies = ("AB" * 20) + ("A" * 2)
    result = tally_game(rallies)
    assert result == (22, 20, "A")
    
def test_a_wins_cap():
    # input sequence reaches 29-29, then A wins by reaching the cap
    rallies = ("AB" * 29) + "A"
    result = tally_game(rallies)
    assert result == (30, 29, "A")

def test_b_wins_cap():
    # input sequence reaches 29-29, then B wins by reaching the cap
    rallies = ("BA" * 29) + "B"
    result = tally_game(rallies)
    assert result == (29, 30, "B")

def test_no_winner_yet():
    # sequence ends 22-23 with no decisive lead after reaching target
    rallies = ("AB" * 20) + "BABAB"
    result = tally_game(rallies)
    assert result == (22, 23, None)

def test_game_not_over():
    #input A gets 12 points, B gets 20 points
    result = tally_game("A"*12 + "B"*20)
    assert result == (12, 20, None)

def test_invalid_input_raises_error():
    # input contains invalid character mid-sequence
    with pytest.raises(ValueError):
        tally_game("A" * 5 + "X" + "B" * 3)

def test_post_win_rallies_ignored():
    # A wins 21-0; extra rallies now treated as invalid
    with pytest.raises(ValueError):
        tally_game("A"*21 + "B"*5)

def test_cap_reached_stops_game():
    # B reaches cap 30-29; extra rallies now treated as invalid
    with pytest.raises(ValueError):
        tally_game("A"*29 + "B"*30 + "A"*3)