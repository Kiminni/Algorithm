// Run by Node.js
const readline = require('readline');

(async () => {
	let rl = readline.createInterface({ input: process.stdin });
	let arr = [];
	let sum = 0;
	for await (const line of rl) {
		arr = line.split(" ");
		rl.close();
	}
	let n1 = parseFloat(arr[0]);
	let n2 = parseFloat(arr[1]);
	sum = (n1 + n2)
	console.log(sum.toFixed(6));
	process.exit();
})();
