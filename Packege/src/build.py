def Algo2Array(separator: str,mode: str):
    count = int(input())
    data_in = []
    for d in range(count):
        data_in.append(input())
    if mode == 'array':
        temp = []
        for i in data_in:
            _ = []
            for g in i.split(separator):
                _.append(g)
            temp.append(_)
        return temp
    elif mode == 'list':
        temp = []
        for i in data_in:
            for g in i.split(separator):
                temp.append(g)
        return temp
    else:
        temp = []
        for i in data_in:
            _ = []
            for g in i.split(separator):
                _.append(g)
            temp.append(_)
        return temp





