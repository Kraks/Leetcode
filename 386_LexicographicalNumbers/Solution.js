/**
 * @param {number} n
 * @return {number[]}
 */
var lexicalOrder = function(n) {
  return trampoline(thunked.bind(undefined, n, function(x) {return x;}));
};

var thunked = function(to, cont) {
  var cal = function(from, lst, cont) {
    lst.push(from);
    if (from*10 <= to) {
      return cal.bind(undefined, from*10, lst, function(lst) {
        if ((from+1)%10 !== 0 && from+1 <= to) {
          return cal.bind(undefined, from+1, lst, cont);
        }
        return cont.bind(undefined, lst);
      });
    }
    if ((from+1)%10 !== 0 && from+1 <= to) {
      return cal.bind(undefined, from+1, lst, cont);
    }
    return cont.bind(undefined, lst);
  };
  return cal.bind(undefined, 1, [], cont);
};

function trampoline(fn) {
  var op = fn;
  while (typeof op === 'function') {
    op = op();
  }
  return op;
}

console.log(lexicalOrder(9));
console.log(lexicalOrder(13));
console.log(lexicalOrder(103));

