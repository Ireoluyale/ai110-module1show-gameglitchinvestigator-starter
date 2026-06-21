from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"


# --- Regression tests for the high/low direction bug ---
# The original bug returned the wrong direction in the hint message:
# a guess that was too high told the player to "Go HIGHER!" and a guess
# that was too low told them to "Go LOWER!" -- both pointing away from
# the secret. These tests pin the message to the correct direction.

def test_too_high_tells_player_to_go_lower():
    # Guess above the secret: the player must aim LOWER.
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message
    assert "HIGHER" not in message


def test_too_low_tells_player_to_go_higher():
    # Guess below the secret: the player must aim HIGHER.
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message
    assert "LOWER" not in message
