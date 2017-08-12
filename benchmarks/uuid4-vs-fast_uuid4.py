#!/usr/bin/env python
#
#  Benchmarks here. Add fast_uuid4.py to your code base if you want to use it.
#
#  Written by Johannes Ridderstedt <johannesl@46elks.com>
#

from time import time
from uuid import uuid4
import random
import uuid
import sys

# This is the usual way people use uuid4()
def run_uuid4( interations ):
  for i in range(0,iterations):
    s = str(uuid4())

# Alternative way 5x faster and less random.
def run_alternative_uuid4( iterations ):
  for i in range(0,iterations):
    s = str(uuid.UUID(int=random.getrandbits(128), version=4))

# Roughly 20x faster than uuid4 and same collision rate as alternative_uuid4.
def run_fast_uuid4( iterations ):
  for i in range(0,iterations):
    s = fast_uuid4()

# Barely no difference and range allows better readability.
def run_fast_uuid4b( iterations ):
  i = 0
  while i < iterations:
    s = fast_uuid4()
    i = i + 1

# Loop-unrolling gives is slightly faster but rarely possible in real code.
def run_fast_uuid4c( iterations ):
  i = 0
  while i < iterations:
    s = fast_uuid4()
    s = fast_uuid4()
    s = fast_uuid4()
    s = fast_uuid4()
    s = fast_uuid4()
    s = fast_uuid4()
    s = fast_uuid4()
    s = fast_uuid4()
    s = fast_uuid4()
    s = fast_uuid4()
    i = i + 10

# Inline code is faster than loop-unrolling.
def run_fast_uuid4d( iterations ):
  getrandbits = random.getrandbits
  for i in range(0,iterations):
    s = '%032x' % getrandbits(128)

# Add loop-unrolling to shave of another ~20ms from 1 million iterations.
def run_fast_uuid4e( iterations ):
  getrandbits = random.getrandbits
  i = 0
  while i < iterations:
    s = '%032x' % getrandbits(128)
    s = '%032x' % getrandbits(128)
    s = '%032x' % getrandbits(128)
    s = '%032x' % getrandbits(128)
    s = '%032x' % getrandbits(128)
    s = '%032x' % getrandbits(128)
    s = '%032x' % getrandbits(128)
    s = '%032x' % getrandbits(128)
    s = '%032x' % getrandbits(128)
    s = '%032x' % getrandbits(128)
    i = i + 10

# Here is my tiny fast implementation. Use fast_uuid4.py in a real code base.
def fast_uuid4():
  return '%032x' % random.getrandbits(128)

benchmarks = [
  ('run_uuid4', 10000),
  ('run_alternative_uuid4', 10000),
  ('run_fast_uuid4', 10000),
  ('run_uuid4', 100000),
  ('run_alternative_uuid4', 100000),
  ('run_fast_uuid4', 100000),
  ('run_uuid4', 1000000),
  ('run_alternative_uuid4', 1000000),
  ('run_fast_uuid4',  1000000),
  ('run_fast_uuid4b', 1000000),
  ('run_fast_uuid4c', 1000000),
  ('run_fast_uuid4d', 1000000),
  ('run_fast_uuid4e', 1000000),
]

for f, iterations in benchmarks:
  self = sys.modules[__name__]
  start = time()
  getattr(self,f)(iterations)
  stop = time()
  print '%28s(%d): %.02fs' % (f, iterations, stop - start)
