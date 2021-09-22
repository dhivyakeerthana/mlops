import os

def test_capitalize_string():
    abc = 'Test'
    assert abc == 'Test'

def check_if_data_exits():
    print(os.path.isdir('data'))
    assert os.path.isdir('data') == True

def check_if_model_exits():
    print(os.path.isfile('model.h5'))
    assert os.path.isfile('model.h5') == True
