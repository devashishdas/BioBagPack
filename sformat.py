def formatter(a):
    def index2(string):
        """
        INPUT:  String
        OUTPUT: Formattable version of string
        """
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
        if n==0:
            d = s(len(i))
        else:
            ss = ww(n) + len(i)
            d += s(ss)
    return(d)
            
            


