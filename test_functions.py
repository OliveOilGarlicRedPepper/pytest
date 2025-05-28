from functions import *

###########################################################
# Examples 
###########################################################
def test_add():
    assert add(2, 3) == 5
    assert add(1, 1) == 2
    assert add(1.2, 1.2) == 2.4

def test_divide():
    assert divide(4, 2) == 2
    assert divide(9, 1) == 9

def test_multiply():
    assert multiply(1, 1) == 1
    assert multiply(3, 2) == 6

def test_square():
    assert square(2) == 4

def test_is_gmail():
    assert is_gmail('abc@gmail.com') == True
    assert is_gmail('abc@yahoo.com') == False 


###########################################################
# Practice 
###########################################################
def test_remove_negatives():
    df = pd.DataFrame({'A': [1, -2, 3], 'B': [4, 5, 6]})
    cleaned_df = remove_negatives(df)
    assert (cleaned_df['A'] < 0).sum() == 0  # No negative values

def test_scale_data():
    df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
    scaled_df = scale_data(df)
    expected_df = pd.DataFrame({'A': [2, 4], 'B': [6, 8]})
    pd.testing.assert_frame_equal(scaled_df, expected_df)

def test_normalize_text():
    assert normalize_text("  HeLLo ") == "hello"
    assert normalize_text("WORLD  ") == "world"
    assert normalize_text("  spaced out ") == "spaced out"

def test_reverse_list():
    assert reverse_list([1, 2, 3]) == [3, 2, 1]
    assert reverse_list(['a', 'b', 'c']) == ['c', 'b', 'a']
    assert reverse_list([]) == []

def test_gcd():
    assert gcd(10, 5) == 5
    assert gcd(14, 21) == 7
    assert gcd(17, 13) == 1  
    assert gcd(0, 5) == 5
    assert gcd(0, 0) == 0 

def test_is_prime():
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(4) == False
    assert is_prime(11) == True
    assert is_prime(1) == False
    assert is_prime(0) == False

def test_remove_duplicates():
    assert remove_duplicates([1, 2, 2, 3, 1]) == [1, 2, 3]
    assert remove_duplicates(["a", "b", "a"]) == ["a", "b"]
    assert remove_duplicates([]) == []
