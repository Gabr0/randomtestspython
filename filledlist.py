import copy


class Filledlist(list):
    def __init__(self,count,value,*args,**kwargs):
        super().__init__()
        for _ in range(count):
            slef.append(copy.copy(value))
