from snakes_and_ladders import location,is_ladder,is_finished,is_snake_bite,is_started

def test_location():
    assert location(16)==(1,6)
    assert location(87)==(8,7)
def test_is_ladder():
    assert is_ladder(15)==True
    assert is_ladder(17)==False
    assert is_ladder(3)==True
def test_is_finished():
    assert is_finished(100,51)==True
    assert is_finished(21,41)==False
    assert is_finished(7,100)==True
def test_is_snake_bite():
    assert is_snake_bite(99)==True
    assert is_snake_bite(4)==False
    assert is_snake_bite(81)==True
def is_started():
    assert is_started(6,1,2,5)==True
    assert is_started(2,4,4,1)==True
    assert is_started(1,6,1,6)==True



    


