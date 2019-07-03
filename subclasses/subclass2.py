import subclass3

from subclass1 import Base, get_subclasses


class Child2(Base):
    pass


if __name__ == "__main__":
    get_subclasses()
