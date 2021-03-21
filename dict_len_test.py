import dictionary

def test_large_value_list():
    keys=['a','b','c']
    values=[1,2,3,4,5]
    val = len(dictionary.list_to_dict(keys,values))
    assert val == 3

def test_large_key_list():
    keys=['a','b','c']
    values=[1,2]
    val = len(dictionary.list_to_dict(keys,values))
    assert val == 3

