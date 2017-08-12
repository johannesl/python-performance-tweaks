# Commonly used python functions made faster

Tweaking code that runs lots of times can give great performance benefits. The focus of this repo is to gather suggestions on how commonly used functions can be tweaked to run faster. Either by passing optimal arguments or by replacing the implementation with another one written in pure Python (with none or minimum dependancies).

Made by Johannes Ridderstedt, johannesl@46elks.com

## uuid4()

When generating unique IDs it's common to use the `uuid.uiid4` function. However, out in the real world there is a trade off between potential collisions and execution time. Using a PRNG seeded with real random bits is usually random enough for most systems and way faster. This is what my new `fast_uuid` function does.

    $ python uuid4-vs-fast_uuid4.py
                  run_uuid4(10000): 0.14s
      run_alternative_uuid4(10000): 0.03s
             run_fast_uuid4(10000): 0.01s
                  run_uuid4(100000): 1.42s
      run_alternative_uuid4(100000): 0.31s
             run_fast_uuid4(100000): 0.07s
                  run_uuid4(1000000): 14.14s
      run_alternative_uuid4(1000000): 3.24s
             run_fast_uuid4(1000000): 0.79s
            run_fast_uuid4b(1000000): 0.79s
            run_fast_uuid4c(1000000): 0.73s
            run_fast_uuid4d(1000000): 0.65s
            run_fast_uuid4e(1000000): 0.62s

*My functions fast_uuid4 and uuid4 are released as public domain. Use freely.*
