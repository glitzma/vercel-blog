---
title: "A very useful one-line JavaScript code"
date: 2016-11-02 09:51:37
permalink: /pages/a61298/
categories:
  - 前端
  - JavaScript文章
tags:
  - JavaScript
author: CUGGZ
---

## 1\. Date processing {#一、日期处理}

### 1. Is the inspection date valid? {#_1-检察日期是否有效}

This method is used to check whether the given date is valid:

```javascript
const isDateValid = (...val) => !Number.isNaN(new Date(...val).valueOf());

isDateValid("December 17, 1995 03:24:00");  // true
复制代码
```

### 2. Calculate the interval between two dates {#_2-计算两个日期之间的间隔}

This method is used to calculate the time between two dates:

```javascript
const dayDif = (date1, date2) => Math.ceil(Math.abs(date1.getTime() - date2.getTime()) / 86400000)

dayDif(new Date("2021-11-3"), new Date("2022-2-1"))  // 90
复制代码
```

There are still 90 days until Chinese New Year~

### 3. Find the day of the year a date falls on {#_3-查找日期位于一年中的第几天}

This method is used to detect what day of the year a given date falls:

```javascript
const dayOfYear = (date) => Math.floor((date - new Date(date.getFullYear(), 0, 0)) / 1000 / 60 / 60 / 24);

dayOfYear(new Date());   // 307
复制代码
```

More than 300 days have passed in 2021~

### 4. time formatting {#_4-时间格式化}

This method can be used to convert time into hour:minutes:seconds format:

```javascript
const timeFromDate = date => date.toTimeString().slice(0, 8);

timeFromDate(new Date(2021, 11, 2, 12, 30, 0));  // 12:30:00
timeFromDate(new Date());  // 返回当前时间 09:00:00
复制代码
```

## 2\. String processing {#二、字符串处理}

### 1. Capitalize the first letter of a string {#_1-字符串首字母大写}

This method is used to capitalize the first letter of an English string:

```javascript
const capitalize = str => str.charAt(0).toUpperCase() + str.slice(1)

capitalize("hello world")  // Hello world
复制代码
```

### 2. flip string {#_2-翻转字符串}

This method is used to flip a string and return the flipped string:

```javascript
const reverse = str => str.split('').reverse().join('');

reverse('hello world');   // 'dlrow olleh'
复制代码
```

### 3. random string {#_3-随机字符串}

This method is used to generate a random string:

```javascript
const randomString = () => Math.random().toString(36).slice(2);

randomString();
复制代码
```

### 4. truncate string {#_4-截断字符串}

This method truncates a string at a specified length:

```javascript
const truncateString = (string, length) => string.length < length ? string : `${string.slice(0, length - 3)}...`;

truncateString('Hi, I should be truncated because I am too loooong!', 36)   // 'Hi, I should be truncated because...'
复制代码
```

### 5. Remove HTML from string {#_5-去除字符串中的html}

This method is used to remove HTML elements from a string:

```javascript
const stripHtml = html => (new DOMParser().parseFromString(html, 'text/html')).body.textContent || '';
复制代码
```

## 3\. Array processing {#三、数组处理}

### 1. Remove duplicates from array {#_1-从数组中移除重复项}

This method is used to remove duplicates from an array:

```javascript
const removeDuplicates = (arr) => [...new Set(arr)];

console.log(removeDuplicates([1, 2, 2, 3, 3, 4, 4, 5, 5, 6]));
复制代码
```

### 2. Determine whether the array is empty {#_2-判断数组是否为空}

This method is used to determine whether an array is an empty array. It will return a Boolean value:

```javascript
const isNotEmpty = arr => Array.isArray(arr) && arr.length > 0;

isNotEmpty([1, 2, 3]);  // true
复制代码
```

### 3. Merge two arrays {#_3-合并两个数组}

You can use the following two methods to merge two arrays:

```javascript
const merge = (a, b) => a.concat(b);

const merge = (a, b) => [...a, ...b];
复制代码
```

## 4\. Digital operations {#四、数字操作}

### 1. Determine whether a number is odd or even {#_1-判断一个数是奇数还是偶数}

This method is used to determine whether a number is odd or even:

```javascript
const isEven = num => num % 2 === 0;

isEven(996);
复制代码
```

### 2. Get the average of a set of numbers {#_2-获得一组数的平均值}

```javascript
const average = (...args) => args.reduce((a, b) => a + b) / args.length;

average(1, 2, 3, 4, 5);   // 3
复制代码
```

### 3. Get a random integer between two integers {#_3-获取两个整数之间的随机整数}

This method is used to get a random integer between two integers

```javascript
const random = (min, max) => Math.floor(Math.random() * (max - min + 1) + min);

random(1, 50);
复制代码
```

### 4. Round to specified digits {#_4-指定位数四舍五入}

This method is used to round a number to the specified number of places:

```javascript
const round = (n, d) => Number(Math.round(n + "e" + d) + "e-" + d)

round(1.005, 2) //1.01
round(1.555, 2) //1.56
复制代码
```

## 5\. Color operation {#五、颜色操作}

### 1. Convert RGB to sixteen mechanism {#_1-将rgb转化为十六机制}

This method can convert an RGB color value into a hexadecimal value:

```javascript
const rgbToHex = (r, g, b) => "#" + ((1 << 24) + (r << 16) + (g << 8) + b).toString(16).slice(1);

rgbToHex(255, 255, 255);  // '#ffffff'
复制代码
```

### 2. Get random hex color {#_2-获取随机十六进制颜色}

This method is used to obtain a random hexadecimal color value:

```javascript
const randomHex = () => `#${Math.floor(Math.random() * 0xffffff).toString(16).padEnd(6, "0")}`;

randomHex();
复制代码
```

## 6\. Browser operation {#六、浏览器操作}

### 1. Copy content to clipboard {#_1-复制内容到剪切板}

This method uses navigator.clipboard.writeText to copy text to the clipboard:

```javascript
const copyToClipboard = (text) => navigator.clipboard.writeText(text);

copyToClipboard("Hello World");
复制代码
```

### 2. Clear all cookies {#_2-清除所有cookie}

This method accesses cookies and clears all cookies stored in the web page by using document.cookie:

```javascript
const clearCookies = document.cookie.split(';').forEach(cookie => document.cookie = cookie.replace(/^ +/, '').replace(/=.*/, `=;expires=${new Date(0).toUTCString()};path=/`));
复制代码
```

### 3. Get selected text {#_3-获取选中的文本}

This method gets the text selected by the user through the built-in getSelection property:

```javascript
const getSelectedText = () => window.getSelection().toString();

getSelectedText();
复制代码
```

### 4. Check if it is dark mode {#_4-检测是否是黑暗模式}

This method is used to detect whether the current environment is in dark mode. It is a Boolean value:

```javascript
const isDarkMode = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches

console.log(isDarkMode)
复制代码
```

### 5. Scroll to top of page {#_5-滚动到页面顶部}

This method is used to return to the top of the page:

```javascript
const goToTop = () => window.scrollTo(0, 0);

goToTop();
复制代码
```

### 6. Determine whether the current tab page is active {#_6-判断当前标签页是否激活}

This method is used to detect whether the current tab has been activated:

```javascript
const isTabInView = () => !document.hidden;
复制代码
```

### 7. Determine whether the current device is an Apple device {#_7-判断当前是否是苹果设备}

This method is used to detect whether the current device is an Apple device:

```javascript
const isAppleDevice = () => /Mac|iPod|iPhone|iPad/.test(navigator.platform);

isAppleDevice();
复制代码
```

### 8. Whether to scroll to the bottom of the page {#_8-是否滚动到页面底部}

This method is used to determine whether the page has reached the bottom:

```javascript
const scrolledToBottom = () => document.documentElement.clientHeight + window.scrollY >= document.documentElement.scrollHeight;
复制代码
```

### 9. Redirect to a URL {#_9-重定向到一个url}

This method is used to redirect to a new URL:

```javascript
const redirect = url => location.href = url

redirect("https://www.google.com/")
复制代码
```

### 10. Open browser print box {#_10-打开浏览器打印框}

This method is used to open the browser's print box:

```javascript
const showPrintDialog = () => window.print()
复制代码
```

## 7\. Other operations {#七、其他操作}

### 1. random boolean {#_1-随机布尔值}

This method can return a random Boolean value. Use Math.random() to get a random number from 0 to 1. Compared with 0.5, there is a half probability of getting a true or false value.

```javascript
const randomBoolean = () => Math.random() >= 0.5;

randomBoolean();
复制代码
```

### 2. variable exchange {#_2-变量交换}

You can use the following form to swap the values of two variables without using a third variable:

```javascript
[foo, bar] = [bar, foo];
复制代码
```

### 3. Get the type of variable {#_3-获取变量的类型}

This method is used to get the type of a variable:

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

### 4. Conversion between Fahrenheit and Celsius {#_4-华氏度和摄氏度之间的转化}

This method is used to convert between Celsius and Fahrenheit:

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

### 5. Check if the object is empty {#_5-检测对象是否为空}

This method is used to detect whether a JavaScript object is empty:

```javascript
const isEmpty = obj => Reflect.ownKeys(obj).length === 0 && obj.constructor === Object;
复制代码
```

## Regular basic syntax {#正则基本语法}

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

The difference between `.*` and `.*?` is that the former is a greedy matching mode and the latter is a non-greedy matching mode.The same goes for `.+` and `.+?`


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

## Application summary {#应用总结}

### Verify whether consecutive numbers are repeated {#验证连续数字是否有重复}

```js
"bcae1958fiefadf1958fef".match(/^.*?(\d{4})(?:(?!\1).)*\1/)
```

### Verify if there are duplicate characters {#验证是否有重复字符}

```js

"bcae1958fiqpdljwrxy".match(/^.*?(\w)(?:(?!\1).)*\1/)

```
### IP address regularity {#ip地址的正则}

```js
/^((([1-9]?\d)|(1\d\d)|(2[0-4]\d)|(25[0-5]))\.){3}(([1-9]?\d)|(1\d\d)|(2[0-4]\d)|(25[0-5]))$/.test('0.255.255.0')
```

###  12 digits, 6 consecutive identical digits cannot appear in it {#_12位数字-其中不能出现6位连续相同数字}

```js

'123777890987'.match(/^(?:([0-9])(?!\1{5})){12}$/)

```

### 10 non-repeating letters within A-Z {#a-z以内不重复的10个字母}

Method one:

```js
^(?:([A-Z])(?!.*?\1)){10}$
```

Method two:

```js
'asdfghjklp'.match(/^(?:([a-z])(?=((?!\1).)*$)){10}$/)
```

### Thousands separator (js implementation) {#千位分隔符-js-实现}

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



> Author: CUGGZ
> Link: https://juejin.cn/post/7025771605422768159
