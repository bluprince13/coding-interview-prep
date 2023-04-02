# https://leetcode.com/problems/the-skyline-problem/

from typing import List
from dataclasses import dataclass
import pytest
import heapq

class Building:
    def __init__(self, left, right, height):
        self.left = left
        self.right = right
        self.height = height

class Point:
    def __init__(self, x, height, is_start=False):
        self.x = x
        self.height = height
        self.is_start = is_start

def parse(buildings):
    return [Building(left, right, height) for left, right, height in buildings]


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        return getSkyline(buildings)

def get_sorted_points(buildings):
    points = []
    for building in buildings:
        points.append(Point(building.left, building.height, True))
        points.append(Point(building.right, building.height, False))
    # Points are sorted by x
    # If there is a clash, then we need to pick a start point over an exit point
    # If there is a clash b/w two start points, pick the higher one first, as
    # the higher point needs to go on the skyline
    # If there is a clash b/w two exit points, pick the lower one first, so that
    # removing it doesn't impact the skyline
    return sorted(points, key=lambda x: (x.x, not x.is_start, -x.height) if x.is_start else (x.x, not x.is_start, x.height))

# O(n*logn)
def getSkyline(buildings: List[List[int]]):
    buildings = parse(buildings)
    points = get_sorted_points(buildings)
    priority_queue = []
    priority_queue.append(0)
    skyline = []
    removed_from_priority_queue = []
    for point in points:
        # Add start points to priority queue
        # Remove end points from priority queue
        # Keep track of the priority queue max before and after the change
        previous_max = -priority_queue[0]
        if point.is_start:
            heapq.heappush(priority_queue, -point.height)
        else:
            removed_from_priority_queue.append(-point.height)
            while priority_queue[0] in removed_from_priority_queue:
                removed_from_priority_queue.remove(heapq.heappop(priority_queue))
        new_max = -priority_queue[0]

        # Detect change in max within the priority queue
        # This means the skyline needs to be updated
        if new_max != previous_max:
            skyline.append([point.x, new_max])
    return skyline

# O(n*m) where n is number of buildings and m is width of building
def getSkylineBruteforce(buildings: List[List[int]]):
    buildings = parse(buildings)
    # Find maximum height from 0 to the rightmost point
    # e.g. [0, 0, 0, 0 .. 0]
    max_heights = [0] * (max(building.right for building in buildings) + 1)
    for building in buildings:
        for i in range(building.left, building.right):
            max_heights[i] = max(max_heights[i], building.height)

    # Compute skyline based on height changes
    skyline = []
    for x, height in enumerate(max_heights):
        if not skyline and height == 0:
            continue
        if not skyline or skyline[-1][1] != height:
            skyline.append([x, height])
    return skyline

# ------------------------------------------------------------------------------
# TESTS
# ------------------------------------------------------------------------------

@dataclass
class TestData:
    id: str
    input: tuple
    expected: any
    __test__ = False


class TestClass:
    testdata = [
        TestData(id="1", input=([[0,2,3],[2,5,3]],), expected=[[0,3],[5,0]]),
        TestData(id="2", input=([[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]],), expected=[[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]),
        TestData(id="3", input=([[1,2,1],[1,2,2],[1,2,3]],), expected=[[1,3],[2,0]]),
    ]

    @pytest.mark.parametrize(
        "input,expected",
        map(lambda x: (x.input, x.expected), testdata),
        ids=map(lambda x: x.id, testdata),
    )
    def test(self, input, expected):
        actual = getSkyline(*input)
        assert actual == expected


    @pytest.mark.parametrize(
        "input,expected",
        map(lambda x: (x.input, x.expected), testdata),
        ids=map(lambda x: x.id, testdata),
    )
    def testBruteforce(self, input, expected):
        actual = getSkylineBruteforce(*input)
        assert actual == expected

if __name__ == "__main__":
    pytest.main()