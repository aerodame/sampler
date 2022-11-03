from three_sum import ThreeSum

def test_A():
    s = ThreeSum()
    test_array = [-1,0,1,2,-1,-4]
    target_sum = 0
    assert  s.run(test_array, target_sum) == [[-1,-1,2],[-1,0,1]]
    ## My incorrect output > [[-1,0,1],[-1,2,-1],[0,1,-1]]  

def test_B():
    s = ThreeSum()
    test_array = []
    target_sum = 0
    assert  s.run(test_array, target_sum) == []            

def test_C():
    s = ThreeSum()
    test_array = [-47, -46, -38, -37, -33, -16, -13, -11, -4, -2, 2, 7, 17, 26, 33, 35, 39, 43, 46, 47]
    target_sum = 0
    assert  s.run(test_array, target_sum) == [[-46, 7, 39], [-37, -2, 39], [-37, 2, 35], [-33, -13, 46], [-33, -2, 35], [-33, 7, 26], [-13, -4, 17]]    
