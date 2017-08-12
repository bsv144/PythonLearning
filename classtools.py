'''
Различные утилиты и инструменты для работы с классами
'''

t = 1
class AttrDisplay:
    '''
    Реализует наследуемый метод перезагрузки операций вывода, отображающий
    имена классов м все атрибуты в виде пар имя=значение,
    имеющиеся в экземплярах (исключая атрибуты, унаследованные от классов).
    Может добавляться в любые классы и способен работать с любыми экземплярами.
    '''
    attr = t
    def _gatherAttrs(self):
        attrs = []
        for key in sorted(self.__dict__):
            attrs.append('%s = %s' % (key, getattr(self, key)))
        return ', '.join(attrs)
    def __str__(self):
        return '[%s: %s]' % (self.__class__.__name__, self._gatherAttrs())

if __name__ == '__main__':
    class TopTest(AttrDisplay):
        count = 0
        def __init__(self):
            self.attr1 = TopTest.count
            self.attr2 = TopTest.count + 1
            TopTest.count += 2
        def gatherAttrs(self):
            print('spam')

    class SubTest(TopTest):
        pass

    X, Y = TopTest(), SubTest()
    print(X)
    print(Y)