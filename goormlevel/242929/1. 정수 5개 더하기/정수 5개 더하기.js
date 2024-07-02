// Run by Node.js
const readline = require('readline');

(async () => {
	let rl = readline.createInterface({ input: process.stdin });
	let ans = [];
	let sum = 0;
	for await (const line of rl) {
		ans = line.split(" ").map(Number);
		for(const a of ans) {
			sum += a;
		}
		rl.close();
	}
	console.log(sum);
	process.exit();
})();
