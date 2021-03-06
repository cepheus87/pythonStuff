from multiprocessing import Pool


class ParallelObject:
    _a = 2
    _b = 3
    

    def __init__(self, b):
        self._b = b
        self._c = 4    

    def run(self, c):
        self._c = c
        print(self._a, self._b,  self._c)
        print(self._a * self._b * self._c)

    def run2(self, c):
        print(c)
        return c["deviceId"]


if __name__ == "__main__":

    num_processes = 4
    obj = ParallelObject(4)

    todo_config = [
        {
            "deviceId": "123",
            "refDeviceId": "456",
        },
        {
            "deviceId": "123",
            "refDeviceId": "456",
        },
        ]

    conf = [(e,) for e in todo_config]

    print(conf)

    try:
        with Pool(num_processes) as p:
            p.starmap(obj.run, [(5,), (6,)])
            out = p.starmap(obj.run2, conf)
    except Exception as e:
        print(e)


    print(out)



