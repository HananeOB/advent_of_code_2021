import pytest
import time 

INPUT_TEST = '3,4,3,1,2'

'''
LanternFish internal process :
defaultdict(lambda:8)

'''

def task1(input: str) -> int :
    current = [int(x) for x in input.split(',')]
    for _ in range(80) : 
        new_elements = current.count(0)
        for i, el in enumerate(current) : 
            if el == 0 :
                current[i] = 6
            else : 
                current[i] = el-1
        current.extend([8]*new_elements)
    return len(current)


from collections import Counter 

def task2(input: str) -> int : 
    counter1 = Counter([int(x) for x in input.split(',')])
    for _ in range(256) :
        counter2 = Counter({
            k-1 : v for k,v in counter1.items() if k >= 1
        })
        counter2.update({6:counter1[0], 8:counter1[0]})
        counter1 = counter2
    return sum(counter2.values())
@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        pytest.param(INPUT_TEST, 5934, id='the short test example for task 1 '),
    ),
)
def test_task1(input_s: str, expected: int) -> None:
    assert task1(input_s) == expected

@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        pytest.param(INPUT_TEST, 26984457539, id='the short test example for task 2'),
    ),
)
def test_task2(input_s: str, expected: int) -> None:
    assert task2(input_s) == expected


if __name__ == '__main__' : 
    with open('input.txt', 'r') as f:
        input = f.read()
    
    start_time = time.time()
    print(f'answer of part1 is {task1(INPUT_TEST)}') 
    end_time = time.time()
    print(f'Time in seconds {end_time-start_time}') 
    
    start_time = time.time()
    print(f'answer of part2 is {task2(input)}') 
    end_time = time.time()
    print(f'Time in seconds {end_time-start_time}') 
