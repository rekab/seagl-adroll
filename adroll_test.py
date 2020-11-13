#!/usr/bin/python3

import adroll
import datetime
import os
import unittest


class TestWhatever(unittest.TestCase):
  def setUp(self):
    self.testdata_dir = os.path.join(
        os.path.dirname(os.path.realpath(__file__)), 'testdata')

  def test_before(self):
    f = adroll.get_file_to_play(
        self.testdata_dir, datetime.datetime(2020, 10, 11, 12))
    self.assertEqual(os.path.join(self.testdata_dir, '11-13-11:30.mp4'), f)

  def test_during(self):
    f = adroll.get_file_to_play(
        self.testdata_dir, datetime.datetime(2020, 11, 13, 11, 31))
    self.assertEqual(os.path.join(self.testdata_dir, '11-13-13:15.mp4'), f)

  def test_after(self):
    f = adroll.get_file_to_play(
        self.testdata_dir, datetime.datetime(2020, 11, 13, 13, 31))
    self.assertEqual(os.path.join(self.testdata_dir, '11-13-14:00.mp4'), f)


if __name__ == '__main__':
    unittest.main()
