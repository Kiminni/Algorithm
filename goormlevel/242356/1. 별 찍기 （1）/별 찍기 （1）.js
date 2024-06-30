// Run by Node.js
const readline = require('readline');

(async () => {
	let rl = readline.createInterface({ input: process.stdin });
	
	for await (const line of rl) {
		const N = parseInt(line, 10);
		for (let i = 1; i <= N; i++) console.log("*".repeat(i));
		rl.close();
	}
	
	process.exit();
})();
