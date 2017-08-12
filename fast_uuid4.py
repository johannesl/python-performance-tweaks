#
#  Faster and less random uuid4() function.
#  Returns a string directly instead of an UUID object.
#
#  Written by Johannes Ridderstedt <johannesl@46elks.com>
#  Released as public domain. Use freely.
#

import random

def fast_uuid4():
  return '%032x' % random.getrandbits(128)

# Import this as your uuid4() if you require the same UUID4 string layout.
# Roughly twice as slow as fast_uuid4() but still 10x faster than uuid.uuid4().
def uuid4():
  s = '%032x' % random.getrandbits(128)
  return s[0:8]+'-'+s[8:12]+'-4'+s[13:16]+'-'+s[16:20]+'-'+s[20:32]
