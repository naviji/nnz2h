
class Node:
    def __init__(self, _data, _children=[], _op=''):
        self._data = _data
        self._children = set(_children)
        self._op = _op
        
    def value(self):
        return self._data

    def __add__(self, _other):
        other = _other if isinstance(_other, Node) else Node(_other)
        return Node(self.value()+other.value(), [self, other], 'add')


    def __radd__(self, other): # other + self
        self.__add__(self, other)
        pass

    def backward(self):
        pass

    def forward(self):
        pass

    def __mul__(self, other):
        pass

    def __pow__(self, other):
        pass

    def relu(self):
        pass

    def tanh(self):
        pass

    def backward(self):
        pass

    def __neg__(self): # -self
        pass

    def __sub__(self, other): # self - other
        pass

    def __rsub__(self, other): # other - self
        pass

    def __rmul__(self, other): # other * self
        pass

    def __truediv__(self, other): # self / other
        pass

    def __rtruediv__(self, other): # other / self
        pass

    def __repr__(self):
        pass
