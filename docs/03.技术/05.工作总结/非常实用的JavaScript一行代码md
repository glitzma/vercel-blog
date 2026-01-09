---
title: 非常实用的JavaScript一行代码
date: 2016-11-02 09:51:37
permalink: /pages/a61298/
categories:
  - 前端
  - JavaScript文章
tags:
  - JavaScript
author: CUGGZ
---

## 一、日期处理

### 1. 检察日期是否有效

该方法用于检测给出的日期是否有效：

```javascript
const isDateValid = (...val) => !Number.isNaN(new Date(...val).valueOf());

isDateValid("December 17, 1995 03:24:00");  // true
复制代码
```

### 2. 计算两个日期之间的间隔

该方法用于计算两个日期之间的间隔时间：

```javascript
const dayDif = (date1, date2) => Math.ceil(Math.abs(date1.getTime() - date2.getTime()) / 86400000)

dayDif(new Date("2021-11-3"), new Date("2022-2-1"))  // 90
复制代码
```

距离过年还有90天~

### 3. 查找日期位于一年中的第几天

该方法用于检测给出的日期位于今年的第几天：

```javascript
const dayOfYear = (date) => Math.floor((date - new Date(date.getFullYear(), 0, 0)) / 1000 / 60 / 60 / 24);

dayOfYear(new Date());   // 307
复制代码
```

2021年已经过去300多天了~

### 4. 时间格式化

该方法可以用于将时间转化为hour:minutes:seconds的格式：

```javascript
const timeFromDate = date => date.toTimeString().slice(0, 8);

timeFromDate(new Date(2021, 11, 2, 12, 30, 0));  // 12:30:00
timeFromDate(new Date());  // 返回当前时间 09:00:00
复制代码
```

## 二、字符串处理

### 1. 字符串首字母大写

该方法用于将英文字符串的首字母大写处理：

```javascript
const capitalize = str => str.charAt(0).toUpperCase() + str.slice(1)

capitalize("hello world")  // Hello world
复制代码
```

### 2. 翻转字符串

该方法用于将一个字符串进行翻转操作，返回翻转后的字符串：

```javascript
const reverse = str => str.split('').reverse().join('');

reverse('hello world');   // 'dlrow olleh'
复制代码
```

### 3. 随机字符串

该方法用于生成一个随机的字符串：

```javascript
const randomString = () => Math.random().toString(36).slice(2);

randomString();
复制代码
```

### 4. 截断字符串

该方法可以从指定长度处截断字符串:

```javascript
const truncateString = (string, length) => string.length < length ? string : `${string.slice(0, length - 3)}...`;

truncateString('Hi, I should be truncated because I am too loooong!', 36)   // 'Hi, I should be truncated because...'
复制代码
```

### 5. 去除字符串中的HTML

该方法用于去除字符串中的HTML元素：

```javascript
const stripHtml = html => (new DOMParser().parseFromString(html, 'text/html')).body.textContent || '';
复制代码
```

## 三、数组处理

### 1. 从数组中移除重复项

该方法用于移除数组中的重复项：

```javascript
const removeDuplicates = (arr) => [...new Set(arr)];

console.log(removeDuplicates([1, 2, 2, 3, 3, 4, 4, 5, 5, 6]));
复制代码
```

### 2. 判断数组是否为空

该方法用于判断一个数组是否为空数组，它将返回一个布尔值：

```javascript
const isNotEmpty = arr => Array.isArray(arr) && arr.length > 0;

isNotEmpty([1, 2, 3]);  // true
复制代码
```

### 3. 合并两个数组

可以使用下面两个方法来合并两个数组：

```javascript
const merge = (a, b) => a.concat(b);

const merge = (a, b) => [...a, ...b];
复制代码
```

## 四、数字操作

### 1. 判断一个数是奇数还是偶数

该方法用于判断一个数字是奇数还是偶数：

```javascript
const isEven = num => num % 2 === 0;

isEven(996);
复制代码
```

### 2. 获得一组数的平均值

```javascript
const average = (...args) => args.reduce((a, b) => a + b) / args.length;

average(1, 2, 3, 4, 5);   // 3
复制代码
```

### 3. 获取两个整数之间的随机整数

该方法用于获取两个整数之间的随机整数

```javascript
const random = (min, max) => Math.floor(Math.random() * (max - min + 1) + min);

random(1, 50);
复制代码
```

### 4. 指定位数四舍五入

该方法用于将一个数字按照指定位进行四舍五入：

```javascript
const round = (n, d) => Number(Math.round(n + "e" + d) + "e-" + d)

round(1.005, 2) //1.01
round(1.555, 2) //1.56
复制代码
```

## 五、颜色操作

### 1. 将RGB转化为十六机制

该方法可以将一个RGB的颜色值转化为16进制值：

```javascript
const rgbToHex = (r, g, b) => "#" + ((1 << 24) + (r << 16) + (g << 8) + b).toString(16).slice(1);

rgbToHex(255, 255, 255);  // '#ffffff'
复制代码
```

### 2. 获取随机十六进制颜色

该方法用于获取一个随机的十六进制颜色值：

```javascript
const randomHex = () => `#${Math.floor(Math.random() * 0xffffff).toString(16).padEnd(6, "0")}`;

randomHex();
复制代码
```

## 六、浏览器操作

### 1. 复制内容到剪切板

该方法使用 navigator.clipboard.writeText 来实现将文本复制到剪贴板：

```javascript
const copyToClipboard = (text) => navigator.clipboard.writeText(text);

copyToClipboard("Hello World");
复制代码
```

### 2. 清除所有cookie

该方法可以通过使用 document.cookie 来访问 cookie 并清除存储在网页中的所有 cookie：

```javascript
const clearCookies = document.cookie.split(';').forEach(cookie => document.cookie = cookie.replace(/^ +/, '').replace(/=.*/, `=;expires=${new Date(0).toUTCString()};path=/`));
复制代码
```

### 3. 获取选中的文本

该方法通过内置的 getSelection 属性获取用户选择的文本：

```javascript
const getSelectedText = () => window.getSelection().toString();

getSelectedText();
复制代码
```

### 4. 检测是否是黑暗模式

该方法用于检测当前的环境是否是黑暗模式，它是一个布尔值：

```javascript
const isDarkMode = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches

console.log(isDarkMode)
复制代码
```

### 5. 滚动到页面顶部

该方法用于在页面中返回顶部：

```javascript
const goToTop = () => window.scrollTo(0, 0);

goToTop();
复制代码
```

### 6. 判断当前标签页是否激活

该方法用于检测当前标签页是否已经激活：

```javascript
const isTabInView = () => !document.hidden;
复制代码
```

### 7. 判断当前是否是苹果设备

该方法用于检测当前的设备是否是苹果的设备：

```javascript
const isAppleDevice = () => /Mac|iPod|iPhone|iPad/.test(navigator.platform);

isAppleDevice();
复制代码
```

### 8. 是否滚动到页面底部

该方法用于判断页面是否已经底部：

```javascript
const scrolledToBottom = () => document.documentElement.clientHeight + window.scrollY >= document.documentElement.scrollHeight;
复制代码
```

### 9. 重定向到一个URL

该方法用于重定向到一个新的URL：

```javascript
const redirect = url => location.href = url

redirect("https://www.google.com/")
复制代码
```

### 10. 打开浏览器打印框

该方法用于打开浏览器的打印框：

```javascript
const showPrintDialog = () => window.print()
复制代码
```

## 七、其他操作

### 1. 随机布尔值

该方法可以返回一个随机的布尔值，使用Math.random()可以获得0-1的随机数，与0.5进行比较，就有一半的概率获得真值或者假值。

```javascript
const randomBoolean = () => Math.random() >= 0.5;

randomBoolean();
复制代码
```

### 2. 变量交换

可以使用以下形式在不适用第三个变量的情况下，交换两个变量的值：

```javascript
[foo, bar] = [bar, foo];
复制代码
```

### 3. 获取变量的类型

该方法用于获取一个变量的类型：

```javascript
const trueTypeOf = (obj) => Object.prototype.toString.call(obj).slice(8, -1).toLowerCase();

trueTypeOf('');     // string
trueTypeOf(0);      // number
trueTypeOf();       // undefined
trueTypeOf(null);   // null
trueTypeOf({});     // object
trueTypeOf([]);     // array
trueTypeOf(0);      // number
trueTypeOf(() => {});  // function
复制代码
```

### 4. 华氏度和摄氏度之间的转化

该方法用于摄氏度和华氏度之间的转化：

```javascript
const celsiusToFahrenheit = (celsius) => celsius * 9/5 + 32;
const fahrenheitToCelsius = (fahrenheit) => (fahrenheit - 32) * 5/9;

celsiusToFahrenheit(15);    // 59
celsiusToFahrenheit(0);     // 32
celsiusToFahrenheit(-20);   // -4
fahrenheitToCelsius(59);    // 15
fahrenheitToCelsius(32);    // 0
复制代码
```

### 5. 检测对象是否为空

该方法用于检测一个JavaScript对象是否为空：

```javascript
const isEmpty = obj => Reflect.ownKeys(obj).length === 0 && obj.constructor === Object;
复制代码
```

## 正则基本语法

```
^ 匹配一个输入或一行的开头，/^a/匹配"an A"，而不匹配"An a" 
$ 匹配一个输入或一行的结尾，/a$/匹配"An a"，而不匹配"an A" 
* 匹配前面元字符0次或多次，/ba*/将匹配b,ba,baa,baaa 
+ 匹配前面元字符1次或多次，/ba*/将匹配ba,baa,baaa 
? 匹配前面元字符0次或1次，/ba*/将匹配b,ba  当该字符紧跟在任何一个其他限制符（*,+,?，{n}，{n,}，{n,m}）后面时，匹配模式是非贪婪的。非贪婪模式尽可能少的匹配所搜索的字符串，而默认的贪婪模式则尽可能多的匹配所搜索的字符串。例如，对于字符串“oooo”，“o+?”将匹配单个“o”，而“o+”将匹配所有“o”。
(x) 匹配x保存x在名为$1...$9的变量中 要匹配圆括号字符，请使用\n来引用，n表示第几个匹配的分组
x|y 匹配x或y 
{n} 精确匹配n次 
{n,} 匹配n次以上 
{n,m} 匹配n-m次 
[xyz] 字符集(character set)，匹配这个集合中的任一一个字符(或元字符) 
[^xyz] 不匹配这个集合中的任何一个字符 
[a-z] 字符范围。匹配指定范围内的任意字符。例如，“[a-z]”可以匹配“a”到“z”范围内的任意小写字母字符。
[^a-z] 负值字符范围。匹配任何不在指定范围内的任意字符。例如，“[^a-z]”可以匹配任何不在“a”到“z”范围内的任意字符。
. 匹配除“\n”之外的任何单个字符。要匹配包括“\n”在内的任何字符，请使用像“(.|\n)”的模式。
[\b] 匹配一个退格符 
\b 匹配一个单词的边界 
\B 匹配一个单词的非边界 
\cX 这儿，X是一个控制符，/\cM/匹配Ctrl-M 
\d 匹配一个字数字符，/\d/ = /[0-9]/ 
\D 匹配一个非字数字符，/\D/ = /[^0-9]/ 
\f 匹配一个换页符。等价于\x0c和\cL。
\n 匹配一个换行符 等价于\x0a和\cJ。
\r 匹配一个回车符 等价于\x0d和\cM。
\s 匹配一个空白字符，包括\n,\r,\f,\t,\v等 。等价于[ \f\n\r\t\v]。
\S 匹配一个非空白字符，等于/[^\n\f\r\t\v]/ 。[^ \f\n\r\t\v]。
\t 匹配一个制表符 。等价于\x09和\cI。
\v 匹配一个垂直制表符 等价于\x0b和\cK。
\w 匹配一个可以组成单词的字符(alphanumeric，这是我的意译，含数字)，包括下划线，如[\w]匹配"$5.98"中的5，等于[a-zA-Z0-9] 
\W 匹配一个不可以组成单词的字符，如[\W]匹配"$5.98"中的$，等于[^a-zA-Z0-9]。
\xn 匹配n，其中n为十六进制转义值。十六进制转义值必须为确定的两个数字长。例如，“\x41”匹配“A”。“\x041”则等价于“\x04&1”。正则表达式中可以使用ASCII编码。
\num 匹配num，其中num是一个正整数。对所获取的匹配的引用。例如，“(.)\1”匹配两个连续的相同字符。
\n 标识一个八进制转义值或一个向后引用。如果\n之前至少n个获取的子表达式，则n为向后引用。否则，如果n为八进制数字（0-7），则n为一个八进制转义值。
\nm 标识一个八进制转义值或一个向后引用。如果\nm之前至少有nm个获得子表达式，则nm为向后引用。如果\nm之前至少有n个获取，则n为一个后跟文字m的向后引用。如果前面的条件都不满足，若n和m均为八进制数字（0-7），则\nm将匹配八进制转义值nm。
\nml 如果n为八进制数字（0-3），且m和l均为八进制数字（0-7），则匹配八进制转义值nml。
\un 匹配n，其中n是一个用四个十六进制数字表示的Unicode字符。例如，\u00A9匹配版权符号（©）。
```

`.*`与`.*?`的区别是前者是贪婪匹配后者是非贪婪匹配模式。`.+`与`.+?`也是一样


```

(x)	
像下面的例子展示的那样，它会匹配 'x' 并且记住匹配项。其中括号被称为捕获括号。

模式 /(foo) (bar) \1 \2/ 中的 '(foo)' 和 '(bar)' 匹配并记住字符串 "foo bar foo bar" 中前两个单词。模式中的 \1 和 \2 表示第一个和第二个被捕获括号匹配的子字符串，即 foo 和 bar，匹配了原字符串中的后两个单词。注意 \1、\2、...、\n 是用在正则表达式的匹配环节，详情可以参阅后文的 \n 条目。而在正则表达式的替换环节，则要使用像 $1、$2、...、$n 这样的语法，例如，'bar foo'.replace(/(...) (...)/, '$2 $1')。$& 表示整个用于匹配的原字符串。
---------------------------------------
(?:x)	
匹配 'x' 但是不记住匹配项。这种括号叫作非捕获括号，使得你能够定义与正则表达式运算符一起使用的子表达式。看看这个例子 /(?:foo){1,2}/。如果表达式是 /foo{1,2}/，{1,2} 将只应用于 'foo' 的最后一个字符 'o'。如果使用非捕获括号，则 {1,2} 会应用于整个 'foo' 单词。更多信息，可以参阅下文的 Using parentheses 条目.
---------------------------------------
x(?=y)	
匹配'x'仅仅当'x'后面跟着'y'.这种叫做先行断言。

例如，/Jack(?=Sprat)/会匹配到'Jack'仅仅当它后面跟着'Sprat'。/Jack(?=Sprat|Frost)/匹配‘Jack’仅仅当它后面跟着'Sprat'或者是‘Frost’。但是‘Sprat’和‘Frost’都不是匹配结果的一部分。
---------------------------------------
(?<=y)x	
匹配'x'仅仅当'x'前面是'y'.这种叫做后行断言。

例如，/(?<=Jack)Sprat/会匹配到' Sprat '仅仅当它前面是' Jack '。/(?<=Jack|Tom)Sprat/匹配‘ Sprat ’仅仅当它前面是'Jack'或者是‘Tom’。但是‘Jack’和‘Tom’都不是匹配结果的一部分。
---------------------------------------
x(?!y)	
仅仅当'x'后面不跟着'y'时匹配'x'，这被称为正向否定查找。

例如，仅仅当这个数字后面没有跟小数点的时候，/\d+(?!\.)/ 匹配一个数字。正则表达式/\d+(?!\.)/.exec("3.141")匹配‘141’而不是‘3.141’
---------------------------------------
(?<!y)x	
仅仅当'x'前面不是'y'时匹配'x'，这被称为反向否定查找。

例如, 仅仅当这个数字前面没有负号的时候，/(?<!-)\d+/ 匹配一个数字。
/(?<!-)\d+/.exec('3') 匹配到 "3".
/(?<!-)\d+/.exec('-3') 因为这个数字前有负号，所以没有匹配到。
---------------------------------------
x|y	
匹配‘x’或者‘y’。

例如，/green|red/匹配“green apple”中的‘green’和“red apple”中的‘red’

```

## 应用总结

### 验证连续数字是否有重复

```js
"bcae1958fiefadf1958fef".match(/^.*?(\d{4})(?:(?!\1).)*\1/)
```

### 验证是否有重复字符

```js

"bcae1958fiqpdljwrxy".match(/^.*?(\w)(?:(?!\1).)*\1/)

```
### ip地址的正则

```js
/^((([1-9]?\d)|(1\d\d)|(2[0-4]\d)|(25[0-5]))\.){3}(([1-9]?\d)|(1\d\d)|(2[0-4]\d)|(25[0-5]))$/.test('0.255.255.0')
```

###  12位数字，其中不能出现6位连续相同数字

```js

'123777890987'.match(/^(?:([0-9])(?!\1{5})){12}$/)

```

### A-Z以内不重复的10个字母

方法一：

```js
^(?:([A-Z])(?!.*?\1)){10}$
```

方法二：

```js
'asdfghjklp'.match(/^(?:([a-z])(?=((?!\1).)*$)){10}$/)
```

### 千位分隔符(js 实现)

```js

function thousandBitSeparator(num) {
    return num && num
        .toString()
        .replace(/(\d)(?=(\d{3})+\.)/g, function($0, $1) {
            return $1 + ",";
        });
}
console.log(thousandBitSeparator(-1234567.9012));
```


```js

var a = 1;
function b(){
    var a=2;
    function c(){
        console.log(a)
    }
    return c;
}

b()();
```



> 作者：CUGGZ
> 链接：https://juejin.cn/post/7025771605422768159
