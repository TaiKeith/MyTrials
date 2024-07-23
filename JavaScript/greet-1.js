const readline = require('readline');

const rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout
});

rl.question('Enter your name: ', (name) => {
	const greeting = "Hello ";
	console.log(greeting + name);
	rl.close();
});
