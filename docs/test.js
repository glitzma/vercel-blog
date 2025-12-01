// function f(count) {
//     console.log("foo==>",`foo${count}`);
//     setTimeout(() => { console.log(`bar${count}`); });
//     // Promise.resolve().then(() => { console.log(`baz${count}`); });
// }
// f(1)
// f(2)
// setTimeout(()=>{f(3)})

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

// function palindromeCharacters () {
//     const str = 'ab3ccba';
//     const charCount = {};
//     for (const char of str) {
//         charCount[char] = (charCount[char] || 0) + 1;
//     }
//     let oddCount = 0;
//     for (const count of Object.values(charCount)) {
//         if (count % 2 !== 0) {
//             oddCount++;
//         }
//     }
//     return oddCount <= 1;
// }

// function palindromeCharacters () {
//     const str = 'abc2cba0';
//     const charSet = new Set();
//     for (const char of str) {
//         if (charSet.has(char)) {
//             charSet.delete(char);
//         } else {
//             charSet.add(char);
//         }
//     }
//     return charSet.size <= 1;
// }

function palindromeCharacters () {
    const str = 'ab2ccba';
    let bitVector = 0;
    for (const char of str) {
        const charCode = char.charCodeAt(0);
        const mask = 1 << charCode;
        bitVector ^= mask;
    }
    return (bitVector & (bitVector - 1)) === 0;
}
// 如果字符集合已知且很小（例如只考虑小写英文字母 a–z），把字符映射到索引 0..25：
// index = charCode - 'a'.charCodeAt(0)
// mask = 1 << index
// 这样位向量只需 26 位，安全且高效。
// 如果字符集合不受限（任意 Unicode），不要用位操作，改用 Set 或 Map（空间 O(k)，k = 不同字符数），也很简单且正确。
// 如果确实想处理大字符集但仍要位向量，可使用 BigInt 位操作并映射到稳定的索引（但 BigInt 也无法直接用 charCode 作为大位移索引，仍需映射不同字符到不同索引）。

console.log(palindromeCharacters());