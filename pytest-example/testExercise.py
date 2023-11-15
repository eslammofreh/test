#import pytest
#import unittest
def fizz_buzz(num):
    if num%3==0 and num%5==0:
        return "FizzBuzz"
    elif num % 3 ==0:
       return "Fizz"
    elif num % 5 == 0:
       return "Buzz";
    elif num < 0: 
        raise Exception("Zero or negative numbers are not accepted");


def test_fizz_buzz():
    assert fizz_buzz(3) == "Fizz" and fizz_buzz(9)== "Fizz";
    assert fizz_buzz(5) == "Buzz" and fizz_buzz(10)=="Buzz";
    assert fizz_buzz(15) == "FizzBuzz" and fizz_buzz(30)=="FizzBuzz";
    #with pytest.raises(Exception, match="Zero or negative numbers are not accepted"):
    #    fizz_buzz(-5);

