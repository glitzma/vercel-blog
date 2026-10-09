---
title: "axios and promises"
date: 2018-06-07 00:00:00
permalink: /pages/e44648/
categories: 
  - 技术
  - 工作总结
tags: 
  - 
author: 
  name: mamingjuan
  link: https://github.com/happy760690
---

## axios

axios is a promise-based http library that can be used in browsers and node.js

- Create XMLHttpRequests from the browser
- Create http request from node.js
- Support Promise API
- Intercept requests and responses
- Convert request data and response data
- Cancel request
- Automatically convert JSON data
- Client support for defending against XSRF

##  promise usage documentation {#promise-用法文档}

[http://liubin.org/promises-book/#chapter1-what-is-promise](http://liubin.org/promises-book/#chapter1-what-is-promise)

[https://developers.google.com/web/fundamentals/primers/promises?hl=zh-cn](https://developers.google.com/web/fundamentals/primers/promises?hl=zh-cn)

[https://developers.google.com/web/fundamentals/primers/promises?hl=zh-cn#promise-api-reference](https://developers.google.com/web/fundamentals/primers/promises?hl=zh-cn#promise-api-reference)

### promise 

### Multiple requests in parallel {#多个请求并列}

```js
async tidyData(){
    for(let item of itemList){ // itemList存放axios请求
        let result = await item; 
        // TODO 其它事情....
    }
}

// 或者
var asyncIterable = {
  [Symbol.asyncIterator]() {
    return {
      i: 0,
      next() {
        if (this.i < 3) {
          return Promise.resolve({ value: this.i++, done: false });
        }

        return Promise.resolve({ done: true });
      }
    };
  }
};
(async function() {
   for await (num of asyncIterable) {
     console.log(num);
   }
})();
```

###  N concurrent requests {#n个并发请求}
Helper function to handle concurrent requests.

```sh
axios.all（iterable）
axios.spread（callback）
```

``` javascript
class Scheduler {
  constructor(num = 2) {
    this.count = 0 // 记录当前正在执行的任务数
    this.todoList = [] // 待执行的任务列表
    this.num = num // 并发最大数：最多可同时执行的任务个数
  }

  // 入列
  add(promiseCreator) {
    if(this.count < this.num) {
      this.count ++
      promiseCreator().then(() => this.dequeue())
    } else {
      this.todoList.push(promiseCreator())
    }
  }

  // 出队方法
  dequeue() {
    this.count --
    if(this.todoList.length > 0) {
      this.todoList.shift().then(() => this.dequeue())
    }
  }
}

const timeout = (time) => new Promise(resolve => {
  setTimeout(resolve, time)
})

const scheduler = new Scheduler()
const addTask = (time, order) => {
  scheduler.add(() => timeout(time).then(() => console.log(order)))
}

addTask(1000, '1')
addTask(500, '2')
addTask(300, '3')
addTask(100, '4')
addTask(400, '5')
addTask(200, '6')
addTask(300, '7')
// 2 3 4 1 6 5 7

// addTask(1000, '1')
// addTask(500, '2')
// addTask(300, '3')
// addTask(400, '4')
//  2314
```

## Execute multiple concurrent requests {#执行多个并发请求}

```javascript
function getUserAccount() {
  return axios.get('/user/12345');
}

function getUserPermissions() {
  return axios.get('/user/12345/permissions');
}

//注：axios.spread 用于拆分请求结果的。
//promise.all会返回一个数组

axios.all([getUserAccount(), getUserPermissions()])
  .then(axios.spread(function (acct, perms) {
    //两个请求现在都执行完成
  }));

```

## fetch manipulates http pipes {#fetch操纵http管道}

```javascript
fetch({
  url: 'https://m.douban.com/rexxar/api/v2/movie/电影ID/interests?start=0＆count=10&order_by=time'
}).then((res) => {
  console.log(res, '开心');
});

```

## axios、fetch、ajax(jquery)

axios and fetch are based on promise, and ajax is on callback.\
fetch is a new syntax that breaks away from xhr. It does not pass cookies by default and cannot monitor the request progress like xhr.
