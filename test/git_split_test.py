from . import repo
import unittest

GIT = repo.GIT
GIT_SILENT = repo.GIT_SILENT


def psp():
    print(*GIT.status('--porcelain'), sep - '\n')


class GitSplitTest(unittest.TestCase):
    @repo.method
    def test_multiple(self):
        self.assertEqual(repo.make_commit('0'), 'c0d1dbb')
        repo.make_commit('1', '2')

        repo.make_commit('3', '4')
        repo.make_commit('5')
        GIT.mv('0', '6')
        GIT.commit('-am', '6')
        with self.assertRaises(Exception):
            GIT.split('HEAD~~~~')
        GIT.split('HEAD~~~')
        actual = GIT.log('--oneline')
        expected = [
            '78923d2 [split] Renamed 0 -> 6',
            'ed73fa3 [split] Added 5',
            '2605324 [split] Added 4',
            '96e0ea3 [split] Added 3',
            '3c32b33 [split] Added 2',
            '5bb18ae [split] Added 1',
            'c0d1dbb 0',
        ]
        self.assertEqual(actual, expected)

    @repo.method
    def test_single(self):
        repo.make_commit('0', '1', '2')
        repo.make_commit('3', '4', '5')
        GIT.split()
        actual = GIT.log('--oneline', '-10')
        expected = [
            '7b3370b [split] Added 5',
            'b5b9547 [split] Added 4',
            'c490a2c [split] Added 3',
            '19deae6 0_1_2',
        ]
        self.assertEqual(actual, expected)

    @repo.method
    def test_staging_area(self):
        repo.make_commit('0')
        repo.make_commit('1')
        repo.make_commit('2')
        repo.write_files('3', '4')
        repo.add_files('3')
        GIT.mv('1', '5')
        GIT.rm('0')
        GIT.split()
        actual = GIT.log('--oneline', '-10')
        expected = [
            'cea714a [split] Added 4',
            '05ecff4 [split] Renamed 1 -> 5',
            'e6b7f89 [split] Added 3',
            '21f80f5 [split] Deleted 0',
            '043df1f 2',
            'a03c0f8 1',
            'c0d1dbb 0'
            ]
        self.assertEqual(actual, expected)
