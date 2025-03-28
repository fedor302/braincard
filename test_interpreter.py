from .code import run_braincard

def test_output_on_start():
    result = run_braincard("♥ ♠ ")
    assert result == chr(0)

def test_increment_on_start():
    result = run_braincard("♠ ♠ ♥ ♠ ")
    assert result == chr(1)

def test_decrement_and_increment_on_start():
    result = run_braincard("♥ ♥ ♠ ♠ ♠ ♠ ♥ ♠ ")
    assert result == chr(1)

def test_decrement_on_start():
    result = run_braincard("♥ ♥ ♥ ♠ ")
    assert result == chr(255)

def test_double_output_on_start():
    result = run_braincard("♥ ♠ ♥ ♠ ")
    assert result == chr(0) + chr(0)

def test_right_output_on_start():
    result = run_braincard("♠ ♠ ♠ ♦ ♥ ♠ ")
    assert result == chr(0)

def test_left_movement():
    result = run_braincard("♠ ♠ ♠ ♦ ♠ ♠ ♦ ♠ ♥ ♠ ")
    assert result == chr(1)

def test_input_processing():
    result = run_braincard("♠ ♥ ♥ ♠ ♠ ♥ ♥ ♠ ", "AB")
    assert result == "AB"

def test_simple_loop():
    result = run_braincard("♠ ♠ ♠ ♠ ♠ ♠ ♥ ♦ ♥ ♥ ♠ ♦ ♠ ♠ ♦ ♠ ♦ ♥ ♠ ♦ ♥ ♠ ")
    assert result == chr(3)
