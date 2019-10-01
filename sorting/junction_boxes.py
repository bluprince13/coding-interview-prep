# no link available

import unittest


def orderedJunctionBoxes(numberOfBoxes, boxList):
    old_list, new_list = split_old_new(boxList)
    sorted_old_list = sort_old(old_list)
    return sorted_old_list + new_list

def split_old_new(boxList):
    old_list = []
    new_list = []
    for box in boxList:
        values = box.split(" ")
    
        if str.isdigit(values[1]):
            new_list.append(box)
        else:
            old_list.append(box)
    return old_list, new_list

def sort_old(old_list):
    ids = []
    versions = []
    for box in old_list:
        id, version = box.split(" ", 1)
        ids.append(id)
        versions.append(version)

    versions, ids = zip(*sorted(zip(versions, ids)))
    
    sorted_list = []
    for id, version in zip(ids, versions):
        sorted_list.append(id + " " + version)
        
    return sorted_list


class MyTest(unittest.TestCase):
    def test_1(self):
        numberOfBoxes = 4
        boxList = [
            'mi2 jog mid pet',
            'wz3 34 54 398',
            'a1 alps cow bar',
            'x4 45 21 7'
        ]
        received = orderedJunctionBoxes(numberOfBoxes, boxList)
        expected = [
            'a1 alps cow bar',
            'mi2 jog mid pet',
            'wz3 34 54 398',
            'x4 45 21 7'
        ]
        self.assertEqual(received, expected)

    def test_2(self):
        numberOfBoxes = 6
        boxList = [
            't2 13 121 98',
            'r1 box ape bit',
            'b4 xi me nu',
            'br8 eat nim did',
            'w1 has uni gry',
            'f3 52 54 31'
        ]
        received = orderedJunctionBoxes(numberOfBoxes, boxList)
        expected = [
            'r1 box ape bit',
            'br8 eat nim did',
            'w1 has uni gry',
            'b4 xi me nu',
            't2 13 121 98',       
            'f3 52 54 31'
        ]
        self.assertEqual(received, expected)

if __name__ == '__main__':
    unittest.main()
