// Run by Node.js
const readline = require('readline');

(async () => {
	let rl = readline.createInterface({ input: process.stdin });
	let total = 0;
	let count = 0;
	let budget = 0;
	let arr = [];
	let t = 0;
	for await (const line of rl) {
		arr = line.split(" ");
		if(total === 0 && count === 0) {
			count = parseInt(arr[0]);
			budget = parseInt(arr[1]);
			continue;
		}
		t += solution(parseInt(arr[0]), parseInt(arr[1]));
	}
	if(t > budget) console.log("No");
	else console.log(budget - t);
	process.exit();
})();

function solution(count, budget) {
	return count * budget;
}
