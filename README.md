# linux-Caesar-cipher

## About/關於

這是我第一次製作linux工具
突然臨時想嘗試製作看看
如果有code上的建議或其他問題 請DM DC: osga_
因為第一次製作 如果有任何問題請通知我 我會非常感謝你><

## Installation Steps/安裝步驟

```
git clone https://github.com/osga24/linux-Caesar-cipher-command.git

cd linux-Caesar-cipher-command/

chmod +x setup.sh

./setup.sh
```

and D0ne!

## User Guide/使用教學

### Usage Instructions/使用方式

``` caesar "text" shift -[parameters]```

### parameters/參數

- -a | Show all displacements
- -d | Decryption
- -c | Encryption

**ex:**

```
caesar "hello world" 12 -c
```

**Results:**

```
tqxxa iadxp
```

**ex:**

```
caesar "vszzc kcfzr" -a -d
```

**Results:**

```
ROT 1: wtaad ldgas
ROT 2: xubbe mehbt
ROT 3: yvccf nficu
ROT 4: zwddg ogjdv
ROT 5: axeeh phkew
ROT 6: byffi qilfx
ROT 7: czggj rjmgy
ROT 8: dahhk sknhz
ROT 9: ebiil tloia
ROT 10: fcjjm umpjb
ROT 11: gdkkn vnqkc
ROT 12: hello world
ROT 13: ifmmp xpsme
ROT 14: jgnnq yqtnf
ROT 15: khoor zruog
ROT 16: lipps asvph
ROT 17: mjqqt btwqi
ROT 18: nkrru cuxrj
ROT 19: olssv dvysk
ROT 20: pmttw ewztl
ROT 21: qnuux fxaum
ROT 22: rovvy gybvn
ROT 23: spwwz hzcwo
ROT 24: tqxxa iadxp
ROT 25: uryyb jbeyq

```



