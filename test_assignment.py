import os
from pathlib import Path

def check_if_data_exits():
    print(os.path.isdir('data'))
    assert os.path.isdir('data') == True

def check_if_model_exits():
    print(os.path.isfile('model.h5'))
    assert os.path.isfile('model.h5') == True

check_if_data_exits()
check_if_model_exits()