# Hello World in Multiple Languages

여러 프로그래밍 언어로 작성한 간단한 **Hello, World!** 예제 모음입니다.

## 파일 목록

| 번호 | 언어 | 파일 |
|---:|---|---|
| 01 | Python | [`01 Hello.py`](./01%20Hello.py) |
| 02 | C | [`02 Hello.c`](./02%20Hello.c) |
| 03 | C++ | [`03 Hello.cpp`](./03%20Hello.cpp) |
| 04 | JavaScript | [`04 Hello.js`](./04%20Hello.js) |
| 05 | TypeScript | [`05 Hello.ts`](./05%20Hello.ts) |
| 06 | Verilog | [`06 Hello.v`](./06%20Hello.v) |
| 07 | Java | [`07 Hello.java`](./07%20Hello.java) |
| 08 | Kotlin | [`08 Hello.kt`](./08%20Hello.kt) |
| 09 | Dart | [`09 Hello.dart`](./09%20Hello.dart) |
| 10 | Brainfuck | [`10 Hello.bf`](./10%20Hello.bf) |

## 실행 예시

### Python

```bash
python "01 Hello.py"
```

### C

```bash
gcc "02 Hello.c" -o hello
./hello
```

### C++

```bash
g++ "03 Hello.cpp" -o hello
./hello
```

### JavaScript

```bash
node "04 Hello.js"
```

### TypeScript

```bash
npx ts-node "05 Hello.ts"
```

### Verilog

```bash
iverilog -o hello "06 Hello.v"
vvp hello
```

### Java

```bash
javac "07 Hello.java"
java MyClass
```

### Kotlin

```bash
kotlinc "08 Hello.kt" -include-runtime -d hello.jar
java -jar hello.jar
```

### Dart

```bash
dart run "09 Hello.dart"
```

### Brainfuck

[Brainfuck 인터프리터](https://sange.fi/esoteric/brainfuck/impl/interp/i.html)를 사용해 실행합니다.

```bash
bf "10 Hello.bf"
```
