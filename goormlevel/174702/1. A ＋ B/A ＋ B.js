// Run by Node.js
const readline = require('readline');

(async () => {
	let rl = readline.createInterface({ input: process.stdin });
	let arr = [];
	for await (const line of rl) {
		arr = line.split(" ");
		rl.close();
	}
	let n1 = parseInt(arr[0]);
	let n2 = parseInt(arr[1]);
	console.log(n1 + n2);
	process.exit();
})();
