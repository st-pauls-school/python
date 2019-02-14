import sys

def test(did_pass):
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = "Test at line {0} successful.".format(linenum)
    else:
        msg = "Test at line {0} failed.".format(linenum)
    print(msg)
