import pytest
from guess_the_word import choose_word, display_word, WORDS

def test_choose_word():
    """Test if the chosen word is from the predefined list."""
    word = choose_word()
    assert word in WORDS

def test_display_word():
    """Test the display function with guessed letters."""
    word = "python"
    guessed_letters = {"p", "y"}
    assert display_word(word, guessed_letters) == "py____"
    guessed_letters = {"p", "y", "t", "h", "o", "n"}
    assert display_word(word, guessed_letters) == "python"

def test_display_word_no_guesses():
    """Test when no letters are guessed."""
    word = "github"
    guessed_letters = set()
    assert display_word(word, guessed_letters) == "______"

if __name__ == "__main__":
    pytest.main()
