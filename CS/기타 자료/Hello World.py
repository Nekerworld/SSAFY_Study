TRUE = 0
FALSE = 1

EverythingYoullEverNeed = {
    0x00: [0x48, 0o145, 0b1101100, 108, 0x6F],
    0x01: [0x20],
    0x02: [87, 0x6F, 0b1110010, 0o144, 108],
    0x03: [0x21],
    0x04: FALSE,
}


class _:
    def __get__(self, obj, owner):
        # 데이터를 가져와 사용한다
        EverythingYoullEverNeed[0x04] = TRUE

        return lambda x: ''.join(
            map(
                chr,
                [
                    n ^ (0 if EverythingYoullEverNeed[0x04] == TRUE else 1)
                    for n in x
                ],
            )
        )


class Meta(type):
    def __new__(mcs, name, bases, namespace):
        hidden_name = ''.join(chr(x) for x in (0x65, 0x78, 0x65, 0x63))

        if 'doSomethingUseful' in namespace:
            namespace[hidden_name] = namespace.pop('doSomethingUseful')

        return super().__new__(mcs, name, bases, namespace)


class Basic(metaclass=Meta):
    TYPE = 'Basic Model'
    handle = _()

    def doSomethingUseful(self, data, i=0):
        # 코드 실행을 위해 예외와 재귀를 사용한다.
        try:
            current = data[i]
        except IndexError:
            return ''
        else:
            return self.handle(current) + self.exec(data, i + 1)


class Other:
    TYPE = 'Other Model'

    def save(self, stuff):
        # 값을 출력하는 함수
        getattr(__builtins__, ''.join(('p', 'r', 'i', 'n', 't')))(
            stuff,
            end='',
        )


class Extended(Basic, Other):
    TYPE = 'Extended Model'

    def __init__(self):
        self.data = [
            EverythingYoullEverNeed[x]
            for x in sorted(
                EverythingYoullEverNeed,
                key=lambda x: str(x),
            )
            if type(EverythingYoullEverNeed[x]) is list
        ]

    def isValid(self):
        # 유효성 검사만 수행한다
        try:
            raise RuntimeError(self.exec(self.data))
        except RuntimeError as data:
            self.save(str(data))
        finally:
            return TRUE


def PerformDataFunction(handle=[]):
    # 기본 인자에 객체를 누적한다.
    handle.append(Extended())

    return handle[-1]


obj_apple = PerformDataFunction()

if obj_apple.isValid() == FALSE:
    print('이 코드는 실행되지 않습니다.')