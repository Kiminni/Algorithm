// Run by Node.js
const readline = require('readline');

(async () => {
	let rl = readline.createInterface({ input: process.stdin });
	
	for await (const line of rl) {
		const n = parseInt(line);
		let fac = 1;
		for (let i = 1; i <= n ; i++) {
			fac = (fac * i) % 1000000007;		
		}
		console.log(fac)
		rl.close();
	}
	process.exit();
})();
