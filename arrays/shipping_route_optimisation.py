# no link available

# Amazon online assessment

import unittest


def optimalUtilization(maxTravelDist, forwardRouteList, returnRouteList):
    highest = 0
    result = []
    for forwardRoute in forwardRouteList:
        for returnRoute in returnRouteList:
            fwd_id = forwardRoute[0]
            fwd_dist = forwardRoute[1]

            ret_id = returnRoute[0]
            ret_dist = returnRoute[1]

            pair_id = [fwd_id, ret_id]
            total_dist = fwd_dist + ret_dist

            if total_dist < highest:
                pass
            elif total_dist > highest and total_dist <= maxTravelDist:
                highest = total_dist
                result = [pair_id]
            elif total_dist == highest:
                result.append(pair_id)

    return result


class MyTest(unittest.TestCase):
    def test_1(self):
        maxTravelDist = 20
        forwardRouteList = [
            [1, 8],
            [2, 7],
            [3, 14]
        ]
        returnRouteList = [
            [1, 5],
            [2, 10],
            [3, 14]
        ]
        received = optimalUtilization(
            maxTravelDist, 
            forwardRouteList, 
            returnRouteList)
        expected = [[3, 1]]
        self.assertEqual(received, expected)

    def test_2(self):
        maxTravelDist = 20
        forwardRouteList = [
            [1, 8],
            [2, 15],
            [3, 9]
        ]
        returnRouteList = [
            [1, 8],
            [2, 11],
            [3, 12]
        ]
        received = optimalUtilization(
            maxTravelDist, 
            forwardRouteList, 
            returnRouteList)
        expected = [[1, 3], [3, 2]]
        self.assertEqual(received, expected)


if __name__ == '__main__':
    unittest.main()
