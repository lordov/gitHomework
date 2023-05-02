from user_name_constructor_module import user_name_constructor

# Unit тест для проверки работоспособности нашей программы.
def test_user_name_constructor():
    assert user_name_constructor("", "") == "is empty"
    assert user_name_constructor("", " dsad") == "is empty"
    assert user_name_constructor(" ", " ") == "is space"
    assert user_name_constructor(" ", "Doe") == "is space"
    assert user_name_constructor("Joe", "Doe") == "Joe Doe"
    assert user_name_constructor("Joe84512", "Doe") == "is number inside"


if __name__ == '__main__':
    print('test_user_name_constructor запущена сама по себе')
else:
    print('test_user_name_constructor импортирована')    
