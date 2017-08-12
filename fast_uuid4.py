#
#  Faster and less random uuid4() function.
#  Returns a string directly instead of an UUID object.
#
#  Written by Johannes Ridderstedt <johannesl@46elks.com>
#  Release as public domain. Use freely.
#

import random

def fast_uuid4():
  return '%032x' % random.getrandbits(128)
