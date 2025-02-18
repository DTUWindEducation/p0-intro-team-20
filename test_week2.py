"""Test your functions from Week 2 assignment.
"""
import pytest
import preclass_assignment.functions as fxn


def test_greet(capsys):
    """Check that the greet function prints as expected"""
    # Given
    name = 'world'  # who should we greet?

    # When
    fxn.greet(name)  # greet them
    captured = capsys.readouterr()  # capture what would have been printed to screen

    # Then
    assert captured.out == 'Hello, world!\n'  # check that the greeting was what we expect


# # @pytest.mark.parametrize("bed_length, expected_output", [
# #     (135, "The bed is too small.\n"),
# #     (145, "Goldilocks is happy with the bed.\n"),
# #     (160, "The bed is too large.\n"),
# # ])
# def test_goldilocks(capsys, bed_length, expected_output):
#     """Check goldilocks returns expected output"""
#     # When
#     fxn.goldilocks(bed_length)
#     captured = capsys.readouterr()  # Capture printed output

#     # Then
#     assert captured.out == expected_output, f"Expected {expected_output}, but got {captured.out}"


# import pytest

# @pytest.mark.parametrize("bed_length, expected_output", [
#     (135, "The bed is too small.\n"),
#     (145, "Goldilocks is happy with the bed.\n"),
#     (160, "The bed is too large.\n"),
# ])
def test_goldilocks(capsys, bed_length, expected_output):
    """Check goldilocks() prints expected messages based on bed length."""
    # When
    fxn.goldilocks(bed_length)  # Call the function
    captured = capsys.readouterr()  # Capture printed output

    # Then
    assert captured.out == expected_output, f"Expected {expected_output}, but got {captured.out}"


def test_square_list():
    """Check square_list returns expected output"""
    # Given
    inp = [1, 2, 3]  # test input to function
    exp_out = [1, 4, 9]  # expected output

    # When
    out = fxn.square_list_from_user(inp)  # actual output

    # Then
    assert exp_out == out  # throw error if actual and expected output don't match


def test_fibonacci_stop():
    """Check fibonacci_stop works as expected."""
    # Given
    max_value = 10
    expected_output = [1, 1, 2, 3, 5, 8]

    # When
    result = fxn.fibonacci_stop(max_value)

    # Then
    assert result == expected_output, f"Expected {expected_output}, but got {result}"


def test_clean_pitch():
    """Check clean_pitch works as expected."""
    # Given
    pitch_angles = [-1, 2, 6, 95, 76]  # "raw" pitch angles
    status_signals = [1, 0, 0, 0, 0]  # status signals
    expected_output = [-999, 2, 6, 95, 76]  # expected cleaned pitch

    # When
    result = fxn.clean_pitch(pitch_angles, status_signals)

    # Then
    assert result == expected_output, f"Expected {expected_output}, but got {result}"
