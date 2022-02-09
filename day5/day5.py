from __future__ import annotations 
from typing import NamedTuple
from collections import defaultdict 
import pytest
import time 

INPUT_TEST = '''\
0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2   
'''


class Point(NamedTuple):
    x: int 
    y: int 

    @classmethod
    def parse(cls, point: str) -> Point:
        x = int(point.split(',')[0])
        y = int(point.split(',')[1])
        return cls(x, y)


class Line(NamedTuple):
    point1: Point 
    point2: Point

    def is_horizontal(self) -> bool :
        if self.point1.y == self.point2.y :
            return True
        else :
            return False 
    
    def is_vertical(self) -> bool :
        if self.point1.x == self.point2.x :
            return True
        else :
            return False 

    def points_covered(self, task) -> list[Point] :
        if task == 1 :
            if self.is_horizontal() :
                depart = min(self.point1.x, self.point2.x)
                arrive = max(self.point1.x, self.point2.x) + 1 
                return [Point(i, self.point1.y) for i in range(depart, arrive) ]
            elif self.is_vertical() :
                depart = min(self.point1.y, self.point2.y)
                arrive = max(self.point1.y, self.point2.y) + 1 
                return [Point(self.point1.x, i) for i in range(depart, arrive) ]
            else:
                 return []
        
        if task == 2 :
            x_depart = self.point1.x
            y_depart = self.point1.y 
        
            x_arrive = self.point2.x
            y_arrive = self.point2.y 

            if x_depart > x_arrive:
                x_step = -1
            elif x_depart < x_arrive:
                x_step = 1 
            else : 
                x_step = 0 
            if y_depart > y_arrive:
                y_step = -1
            elif y_depart < y_arrive:
                y_step = 1
            else :
                y_step = 0
            result = []
            while (x_depart, y_depart) != (x_arrive, y_arrive)  : 
                result.append(Point(x_depart, y_depart))
                x_depart = x_depart + x_step
                y_depart = y_depart + y_step 
            result.append(Point(x_depart, y_depart))
            return result 



def task1(input: str) -> int :
    seen_count = defaultdict(int)
    dangerous_points = set()
    result = 0
    
    for line in input.splitlines() :
        point1 = Point.parse(line.split(' -> ')[0])
        point2 = Point.parse(line.split(' -> ')[1])
        line = Line(point1, point2)
        # print(line)
        # print(line.points_covered(task=1))
        for point in line.points_covered(task=1) :
            seen_count[point]+=1 
            if seen_count[point] >=2 and point not in dangerous_points:
                result+=1
                dangerous_points.add(point)
    
    return result 

def task2(input: str) -> int : 
    seen_count = defaultdict(int)
    dangerous_points = set()
    result = 0
    
    for line in input.splitlines() :
        point1 = Point.parse(line.split(' -> ')[0])
        point2 = Point.parse(line.split(' -> ')[1])
        line = Line(point1, point2)
        # print(line)
        # print(line.points_covered(task=2))
        for point in line.points_covered(task=2) :
            seen_count[point]+=1 
            if seen_count[point] >=2 and point not in dangerous_points:
                result+=1
                dangerous_points.add(point)
    
    return result 

@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        pytest.param(INPUT_TEST, 5, id='the short test example for task 1 '),
    ),
)
def test_task1(input_s: str, expected: str) -> None:
    assert task1(input_s) == expected

@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        pytest.param(INPUT_TEST, 12, id='the short test example for task 2 '),
    ),
)
def test_task2(input_s: str, expected: str) -> None:
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
