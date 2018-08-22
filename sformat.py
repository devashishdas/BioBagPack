# updated from PyCharm
#TODO: change the method to class





class str2(str):
    def isfloat(self):
        if self.count(".") != 1: return False
        return self.replace(".","").isdigit()
    def countfloat(self):
        if self.isfloat():
            return len(self.strip().split(".")[-1])


def formatter(a):
    """
    INPUT:  String
    OUTPUT: Formattable version of string
    """
    def index2(string):
        old = ""
        d = []
        for n, i in enumerate(string):
            if old == " " and i != " ":
                d.append(n)
            old = i
        w = {0:0}
        for n, i in enumerate(string.split()[1:]):
            w[n+1] = d[n]
        return(w)
    a2 = a.split()
    s = lambda w:"{}:>{}{}".format(chr(123),w,chr(125))
    d = ""
    ww = lambda c:len(a[index2(a)[c-1]+len(a2[c-1]):index2(a)[c]])
    for n,i in enumerate(a2):
        i = str2(i)
        if n==0:
            d = s(len(i))
        else:
            ss = ww(n) + len(i)
            ax = ss
            if i.isfloat() and str2(i.countfloat()) > 0:
                ax = str2(ss) + "." + str2(i.countfloat()) + "f"
            d += s(ax)
    return(d)


# a = "ATOM      1  N   ASN A  17     139.035  74.629  68.493  1.00 33.16           N  "
# b = formatter(a)
# print b
# print b.format(*['ATOM', '1', 'N', 'ASN', 'A', '17', 139.035, 74.629, 68.493, 1.00, 33.16, 'N'])
# print a
