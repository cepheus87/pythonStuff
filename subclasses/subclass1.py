class Base:
    pass


def get_subclasses():
    print(Base.__subclasses__())


class Child1(Base):
    pass


if __name__ == "__main__":
    get_subclasses()
