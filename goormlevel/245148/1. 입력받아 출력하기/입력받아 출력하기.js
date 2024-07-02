const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

let N;
let A, B;

rl.on('line', (input) => {
  if (N === undefined) {
    N = parseInt(input);
  } else if (A === undefined && B === undefined) {
    [A, B] = input.split(' ');
    rl.close();
  }
});

rl.on('close', () => {
  let result = '';

  for (let i = 1; i <= N; i++) {
    for (let j = 1; j <= N; j++) {
      if ((i * j) % 2 === 1) {
        result += A;
      } else {
        result += B;
      }
      if (j < N) {
        result += ' ';
      }
    }
    if (i < N) {
      result += '\n';
    }
  }

  console.log(result);
});