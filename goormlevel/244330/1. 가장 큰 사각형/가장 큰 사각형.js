// Run by Node.js
const readline = require('readline');

(async () => {
	let rl = readline.createInterface({ input: process.stdin });
	let N = null, maximum = 0;
	for await (const line of rl) {
		if(N === null) {
			N = Number(line); 
			continue;
		}
		let str = line.split(" ").map(Number);
		if (str[0] * str[1] > maximum) maximum = str[0]* str[1];
		rl.close();
	}
	console.log(maximum);
	process.exit();
})();
