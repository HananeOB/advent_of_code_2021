import pytest 
import time 


INPUT_TEST = '16,1,2,0,4,2,7,1,2,14'


def task1(input: str) -> int : 
    positions = sorted([int(i) for i in input.split(',')])
    n = len(positions)

    if n%2 == 0 :
        median = positions[n//2]
    else : 
        median =  (positions[(n-1)//2] + positions[(n+1)//2])/2
    
    return sum([abs(i-median) for i  in positions])

def task2(input: str) -> int : 
    positions = [int(i) for i in input.split(',')]
    res = []
    for position1 in range(max(positions)) :
        
        sum_p = 0
        for position2 in positions :
            diff = abs(position2-position1) 
            sum_p = sum_p + diff*(diff+1)//2 
        res.append(sum_p)
    return min(res)


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        pytest.param(INPUT_TEST, 37, id='the short test example for task 1 '),
    ),
)
def test_task1(input_s: str, expected: int) -> None:
    assert task1(input_s) == expected

@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        pytest.param(INPUT_TEST, 168, id='the short test example for task 2'),
    ),
)
def test_task2(input_s: str, expected: int) -> None:
    assert task2(input_s) == expected


if __name__ == '__main__' : 
    with open('input.txt', 'r') as f:
        input = f.read()
    
    start_time = time.time()
    print(f'answer of part1 is {task1(input)}') 
    end_time = time.time()
    print(f'Time in seconds {end_time-start_time}') 
    
    start_time = time.time()
    print(f'answer of part2 is {task2(input)}') 
    end_time = time.time()
    print(f'Time in seconds {end_time-start_time}') 
