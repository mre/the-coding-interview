import time

current_milli_time = lambda: int(round(time.time() * 1000))
call_time = None

def debounce(f, timeout = 1000):
    global call_time
    call_time = current_milli_time()
    def g():
        global call_time
        curr_time = current_milli_time()
        delta = curr_time - call_time
        if (delta > timeout):
            call_time = current_milli_time()
            f()
        else:
            # Too soon!
            pass
    return g


def f():
    print "hello"

g = debounce(f)
while True:
    g()
