class Sorted:

    def __init__(self, obj):
        self.obj = obj
        self.obj = self.__iter__()

    def __iter__(self):
        return iter(sorted(self.obj))

class SortedSet(Sorted, set):

    def __init__(self, obj):
        Sorted.__init__(self,obj)

    def __str__(self):
        return set(self.obj).__str__()

if __name__ == '__main__':
    s = SortedSet([4, 2, 1, 1, 5, 6, 11, 2, 12, 12, 8])
    print(s)