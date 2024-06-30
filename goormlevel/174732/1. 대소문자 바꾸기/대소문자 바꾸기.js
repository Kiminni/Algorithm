// Run by Node.js
const readline = require('readline');

(async () => {
	let rl = readline.createInterface({ input: process.stdin });
	let newLine = "";
	let answer = "";
	for await (const line of rl) {
		newLine = line;
		rl.close();
	}
	for (const n of newLine) {
		if(n >= "a" && n <= "z") answer += n.toUpperCase();
		else if(n >= "A" && n <= "Z") answer += n.toLowerCase();
	}
	console.log(answer);
	process.exit();
})();
