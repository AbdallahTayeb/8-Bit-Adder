class HalfAdder:
    def __init__(self,a,b):
        self.a = a
        self.b = b
        self.c_out = self.a and self.b
        self.adder_sum = self.a ^ self.b

class FullAdder:

        
    def add(self,a,b,c_in):
        self.a = a
        self.b = b
        self.c_in = c_in
        self.ha1 = HalfAdder(a,b)
        self.ha2 = HalfAdder(self.ha1.adder_sum,self.c_in)
        c_out = self.ha1.c_out or self.ha2.c_out
        adder_sum = self.ha2.adder_sum  
        return c_out, adder_sum
    
    @classmethod
    def create(cls,n=8):
        return [cls() for i in range(n)]


class adder_8_bit:
    def __init__(self,first,second):
        self.bins = [tuple(map(int,x)) for x in list(zip(reversed(first),reversed(second)))]
        self.adders = FullAdder.create(8)
        self.pipe = zip(self.bins,self.adders)

    def compute(self,carry=0):
        sum_output = []
        for bin,adder in self.pipe:
            carry, sum_ = adder.add(*bin,carry)
            sum_output.insert(0, sum_)
        binary_output = ''.join(list(map(str,sum_output)))
        return binary_output

my_adder = adder_8_bit('00000001','00000010')
print(int(my_adder.compute(),2))
