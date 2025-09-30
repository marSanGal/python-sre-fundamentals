from app.fizzbuzz import fizzbuzz

def test_fizzbuzz_basic():
    result = fizzbuzz(15)
    assert result[2] == "Fizz"
    assert result[4] == "Buzz"
    assert result[14] == "FizzBuzz"
    assert result[0] == 1
    assert len(result) == 15