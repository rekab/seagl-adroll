#!/usr/bin/python3
"""
given the filenames '11-13-11:30.mp4', '11-13-13:15.mp4', and 11-13-14:00.mp4',
can the first file be played before 11:30, the second file played between 11:30
and 13:15, and the third file played between 13:15 and 14:00?

USAGE:
  adroll.py <dir with files>
"""

import datetime
import os
import re
import sys

FILENAME_PATTERN = re.compile('\d\d-\d\d-\d\d:\d\d.mp4$')


class TimestampedFile(object):
    def __init__(self, filename, time):
        self.filename = filename
        self.time = time


def get_files(path):
  """Get filenames and the time they represent from a path.

  Returns filenames sorted by time, ascending. Does not handle year boundaries!
  """
  if path is None:
    path = '.'
  basename = os.path.abspath(path)

  files = []
  for f in os.listdir(path=path):
    if FILENAME_PATTERN.match(f):
      # Parse the time from the filename. Replace the year with this year.
      t = datetime.datetime.strptime(f, '%m-%d-%H:%M.mp4').replace(
          year=datetime.datetime.now().year)
      fullpath = os.path.join(basename, f)
      files.append(TimestampedFile(fullpath, t))

  # Sort files by their times, ascending.
  return sorted(files, key=lambda f: f.time)


def get_file_to_play(path, now):
  files = get_files(path)
  if not files:
    raise RuntimeError('no files')

  # Find the next applicable
  for f in files:
    if now < f.time:
      return f.filename
  else:
    # return the last one, i guess?
    return files[-1]


if __name__ == '__main__':
  if len(sys.argv) > 2:
    raise RuntimeError('too many args')
  path = '.'
  if len(sys.argv) == 2:
    path = sys.argv[1]
  print(get_file_to_play(path, datetime.datetime.now()))
