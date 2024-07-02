// Run by Node.js
const readline = require('readline');

(async () => {
	let rl = readline.createInterface({ input: process.stdin });
	let arr = [];
	let num = 0;
	for await (const line of rl) {
		if (num === 0) num = Number(line);
		else {
			arr = line.split(" ").map(Number);
			if(arr[0] < arr[1]) console.log("Sunflower");
			else if(arr[0] === arr[1]) console.log("Tulip");
			else console.log("Rose");
		}
		rl.close();
	}
	
	process.exit();
})();
