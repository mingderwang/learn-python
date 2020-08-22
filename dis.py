print('---------- test dis 看 byte code  --------')
import dis
def myfunc(alist):
    a = 1
    alist.append(a)
    return len(alist)
dis.dis(myfunc)