from three_sum import ThreeSum

def test_A():
    s = ThreeSum()
    test_array = [9, 11, 16, 17, 20, 35]
    target_sum = 44
    assert  s.run(test_array, target_sum) == [0, 5]

def test_B():
    s = ThreeSum()
    test_array = [9, 11, 16, 17, 20, 35]
    target_sum = 100
    assert  s.run(test_array, target_sum) == [None, None]

def test_C():
    s = ThreeSum()
    test_array = [0, 1]
    target_sum = 1
    assert  s.run(test_array, target_sum) == [0, 1]        

def test_D():
    s = ThreeSum()
    test_array = []
    target_sum = 42
    assert  s.run(test_array, target_sum) == [None, None]            

def test_E():
    s = ThreeSum()
    test_array = [1, 2, 3, 4, 5]
    target_sum = -1
    assert  s.run(test_array, target_sum) == [None, None]
