from is_odd_or_even_module import is_odd_or_even


# Unit тест для проверки работоспособности нашей программы.
def tests_is_odd_or_even():
    assert is_odd_or_even(2) == True , 'error case: 2'
    assert is_odd_or_even(3) == False, 'error case: 3'
    assert is_odd_or_even(21) == True, 'error case: 21'
    assert is_odd_or_even(0) == True, 'error case: 0'
    assert is_odd_or_even(-4) == True, 'error case: -4'


if __name__ == '__main__':
    print('tests_odd_or_even_module запущена сама по себе')
else:
    print('tests_odd_or_even_module импортирована')  
