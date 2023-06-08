class MealyError(Exception):
    pass


class Automat:
    state = 'A'

    def reset(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        if self.state == 'B':
            self.state = 'C'
            return 2
        if self.state == 'D':
            self.state = 'B'
            return 6
        if self.state == 'F':
            self.state = 'D'
            return 8
        else:
            raise(MealyError('reset'))

    def tread(self):
        if self.state == 'B':
            return 3
        if self.state == 'A':
            self.state = 'D'
            return 1
        if self.state == 'C':
            self.state = 'D'
            return 4
        if self.state == 'D':
            self.state = 'E'
            return 5
        else:
            raise(MealyError('tread'))

    def roam(self):
        if self.state == 'E':
            self.state = 'F'
            return 7
        else:
            raise (MealyError('roam'))


def main():
    return Automat()


def raises(func, error):
    output = None
    try:
        output = func()
    except Exception as e:
        assert type(e) == error
    assert output is None


def test():
    a = main()
    a.state = 'A'
    assert a.reset() == 0
    assert a.state == 'B'
    a.state = 'A'
    raises(lambda: a.roam(), MealyError)
    assert a.tread() == 1
    assert a.state == 'D'
    raises(lambda: a.roam(), MealyError)
    a.state = 'B'
    assert a.tread() == 3
    assert a.state == 'B'
    raises(lambda: a.roam(), MealyError)
    assert a.reset() == 2
    assert a.state == 'C'
    raises(lambda: a.roam(), MealyError)
    raises(lambda: a.reset(), MealyError)
    assert a.tread() == 4
    assert a.state == 'D'
    assert a.reset() == 6
    assert a.state == 'B'
    a.state = 'D'
    assert a.tread() == 5
    assert a.state == 'E'
    raises(lambda: a.reset(), MealyError)
    raises(lambda: a.tread(), MealyError)
    assert a.roam() == 7
    assert a.state == 'F'
    raises(lambda: a.roam(), MealyError)
    raises(lambda: a.tread(), MealyError)
    assert a.reset() == 8
    assert a.state == 'D'

test()

o = main()
print(o.tread())
print(o.reset())
print(o.tread())
print(o.tread())
#print(o.roam())
print(o.reset())
print(o.tread())
print(o.tread())
print(o.roam())
print(o.reset())