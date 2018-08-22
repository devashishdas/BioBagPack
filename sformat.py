# updated from PyCharm
#TODO: change the method to class
from __future__ import print_function, division




class str2(str):

    def isfloat(self):
        if self.count(".") != 1: return False
        return self.replace(".","").isdigit()

    def countfloat(self):
        if self.isfloat():
            return len(self.strip().split(".")[-1])


class StrFormat:
    """
    INPUT:  String
    OUTPUT: Formattable version of string
    """
    def __init__(self,string):
        self.string = string

    def index2(self, string):
        old_string = ""
        list_index = []
        for n, i in enumerate(string):
            if old_string == chr(32) and i != chr(32):
                list_index.append(n)
            old_string = i
        dict_index = {0: 0}
        for n, i in enumerate(string.split()[1:]):
            dict_index[n + 1] = list_index[n]
        return dict_index

    def format(self) -> str():
        self.split_string = self.string.split()
        self.string_minor = lambda tmp: "{}:>{}{}".format(chr(123), tmp, chr(125))
        self.string_major = lambda tmp: len(self.string[self.index2(self.string)[tmp - 1] +
                                        len(self.split_string[tmp - 1]):self.index2(self.string)[tmp]])
        self.final_format = str()
        for n, i in enumerate(self.split_string):
            i = str2(i)
            if n == 0:
                # First word is free of formatting.
                self.final_format = self.string_minor(len(i))
            else:
                ss = self.string_major(n) + len(i)
                if i.isfloat() and i.countfloat() > 0:
                    ss = str2(ss) + "." + str2(i.countfloat()) + "f"
                self.final_format += self.string_minor(ss)
        return self.final_format

    def formatAnnot(self):
        """
        This will return a dictionary based on positions and
        """





# a = "ATOM      1  N   ASN A  17     139.035  74.629  68.493  1.00 33.16           N  "
# b = StrFormat(a)
# c = b.format()
# print(c)
# print(c.format(*['ATOM', '1', 'N', 'ASN', 'A', '17', 139.035, 74.629, 68.493, 1.00, 33.16, 'N']))
# print(a)
