import re
import pytest
import time 

TEST_INPUT = '''\
7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
'''








def task1(input) :
    first, *rest = input.split('\n\n')
    r_numbers = [int(number) for number in first.split(',')]
    
    min_x =  len(r_numbers)
    result = 0
    
    for grid in rest :

        grid = [int(number) for number in grid.split()]
        s_lines = [0]*5
        s_columns = [0]*5
        marked_sum = 0 

        for pos,x in enumerate(r_numbers) :

            try :
                index = grid.index(x)
                i = index//5 
                j = index %5 
                s_lines[i] += 1
                s_columns[j] += 1 
                marked_sum += x 
            except ValueError :
                continue
            
            if s_columns[j] == 5 or s_lines[i] == 5 : 
                if pos <= min_x:  
                    min_x = pos 
                    result = x * (sum(grid)-marked_sum)
                break
    
    return(result)


def task2(input) :
    
    first, *rest = input.split('\n\n')
    r_numbers = [int(number) for number in first.split(',')]
    
    max_x =  0
    result = 0

    for grid in rest :
        grid = [int(number) for number in grid.split()]
        
        s_lines = [0]*5
        s_columns = [0]*5
        marked_sum = 0 

        for pos,x in enumerate(r_numbers) :
            try :
                index = grid.index(x)
                i = index//5 
                j = index %5 
                s_lines[i] += 1
                s_columns[j] += 1 
                marked_sum += x 
            
            except ValueError :
                continue
            
            if s_columns[j] == 5 or s_lines[i] == 5 : 
                if pos >= max_x:  
                    max_x = pos 
                    result = x * (sum(grid)-marked_sum)
                break
    
    return(result)

@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        pytest.param(TEST_INPUT, 4512, id='the short test example for task 1 '),
    ),
)
def test_task1(input_s: str, expected: int) -> None:
    assert task1(input_s) == expected

@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        pytest.param(TEST_INPUT, 1924, id='the short test example for task 2 '),
    ),
)
def test_task2(input_s: str, expected: int) -> None:
    assert task2(input_s) == expected


def main() : 
    with open('input.txt', 'r') as f :
        input_s = f.read()
    
    start_time = time.time()
    print(f'answer of part1 is {task1(input_s)}') 
    end_time = time.time()
    print(f'Time in seconds {end_time-start_time}') 

    start_time = time.time()
    print(f'answer of part2 is {task2(input_s)}') 
    end_time = time.time()
    print(f'Time in seconds {end_time-start_time}') 
    
if __name__ == '__main__':
    raise SystemExit(main())