// Run by Node.js
const readline = require('readline');

(async () => {
	let rl = readline.createInterface({ input: process.stdin });
	let answer = ""
	let N = 0
	for await (const line of rl) {
		N = parseInt(line, 10);
	}
	while(N > 0) {
			answer += N % 2;
			N = Math.floor(N / 2)
			if(Math.floor(N) === 0) break;
	}	
	console.log(answer.split('').reverse().join(""));
	rl.close();
	
	process.exit();
})();
