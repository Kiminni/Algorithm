// Run by Node.js

const readline = require("readline");
const rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout
});
rl.on("line", function(line) {
	let answer = line.split(" ");
	let filtered = answer.filter((ans) => ans !== " " && ans !== "");
	console.log(filtered.length);
	rl.close();
	
}).on("close", function() {
	process.exit();
});