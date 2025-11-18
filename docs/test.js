function f(count) {
    console.log("foo==>",`foo${count}`);
    setTimeout(() => { console.log(`bar${count}`); });
    // Promise.resolve().then(() => { console.log(`baz${count}`); });
}
f(1)
f(2)
setTimeout(()=>{f(3)})

// function arrsort(arr) {
//     return arr.sort((a, b) => {
//         const len = Math.min(a.length, b.length);
//         for (let i = 0; i < len; i++) {
//             const diff = a.charCodeAt(i) - b.charCodeAt(i);
//             if (diff !== 0) {
//                 return diff;
//             }
//         }
//         return a.length - b.length;
//     });
// }

// console.log(arrsort(['3.1.1', '1.1.1', '2.5.4']));