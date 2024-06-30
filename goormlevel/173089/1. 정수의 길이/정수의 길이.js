// Run by Node.js
const readline = require('readline');

(async () => {
	let rl = readline.createInterface({ input: process.stdin });
	
	for await (const line of rl) {
		let ans = String(line).length;
		console.log(ans);
		rl.close();
	}
	
	process.exit();
})();
