# https://www.hackerrank.com/challenges/ctci-ransom-note/problem

def checkMagazine(magazine, note):
    # brute force approach:
    # for each word in note, check if it exists in magazine
    # but that'd be O(n * m) which is awful
    # optimize by storing magazine words in hash table
    # this will then be O(n + m)
    result = 'Yes'
    magazine_words = {}
    for word in magazine:
        if word in magazine_words:
            magazine_words[word] += 1
        else:
            magazine_words[word] = 1

    note_words = {}
    for word in note:
        if word not in magazine_words:
            result = 'No'
            break
        elif word in magazine_words and word in note_words:
            if note_words[word] == magazine_words[word]:
                result = 'No'
                break
            else:
                note_words[word] += 1
        else:
            note_words[word] = 1
        
    print(result)
    return result
            
import unittest

class MyTest(unittest.TestCase):
    def test_1(self):
        magazine = "two times three is not four".split()
        note = "two times two is four".split()
        received = checkMagazine(magazine, note)
        expected = "No"
        self.assertEqual(received, expected)

    def test_2(self):
        magazine = "give me one grand today night".split()
        note = "give one grand today".split()
        received = checkMagazine(magazine, note)
        expected = "Yes"
        self.assertEqual(received, expected)

if __name__ == '__main__':
    unittest.main()