// Run by Node.js
const readline = require('readline');

(async () => {
	let rl = readline.createInterface({ input: process.stdin });
	let num = 0;
	let sum = 0;
	let arr = [];
	for await (const line of rl) {
		if (num === 0) {
			num = Number(line);
		} else {
			if(sum < 0) {
				console.log("fail");
				return ;
			}
			arr = line.split(" ");
			if (arr[0] === "in"){
				sum += Number(arr[1]);
			}
			else {
				sum -= Number(arr[1]);
			}
		}
		rl.close();
	}
	if(sum > 0) {
		console.log("success");
	}
	else {
		console.log("fail");
	}
	process.exit();
})();
