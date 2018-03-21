from functools import wraps
import os
import pdb

def log(*args):
    print(*args)

class TraceDecorator(object):

    def __init__(self, f):
        self.func = f

    def __call__(self, *args, **kwargs):
        log(">>> calling ", self.func, args, kwargs)
        try:
            return self.func(*args, **kwargs)
        except:
            log("GOT AN EXCEPTION IN TRACE")
            pdb.set_trace()


def trace(f):
    return TraceDecorator(f)


class CondDecorator(object):
    def __init__(self, f, condition, style='pre'):
        self.func = f
        self.condition = condition
        self.style = style

    def test(self, args, kwargs):
        # todo add the args to locals so we can check them
        loc = locals()
        loc.update(kwargs)
        return eval(self.condition, globals(), loc) == True

    def __call__(self, *args, **kwargs):
        if self.style == 'pre' or self.style == 'invariant':
            if self.test(args, kwargs) == False:
                log(f"{self.style} fail before call", self.condition)

        self.func(*args, **kwargs)

        if self.style == 'post' or self.style == 'invariant':
            if self.test(args, kwargs) == False:
                log(f"{self.style} fail after call", self.condition)

def pre(test):
    def actual_decorator(f):
        return CondDecorator(f, test)
    return actual_decorator

def post(test):
    def actual_decorator(f):
        return CondDecorator(f, test, style='post')
    return actual_decorator

def invariant(test):
    def actual_decorator(f):
        return CondDecorator(f, test, style='invariant')
    return actual_decorator

def check(test, message):
    if 'ASSERT' in os.environ:
        assert test, message
    else:
        if not test:
            log("Assert failure", test, message)

run = True

@invariant('ping == True and args == True')
def test_me(thing, ping=False):
    global ran
    log("You got this!")
    ran = False

test_me(True, ping=True)
test_me(True, ping=False)

@trace
def boom():
    assert False, "WHAAAATTT"

boom()

check(1 + 1 == 3, "I can't do math.")

