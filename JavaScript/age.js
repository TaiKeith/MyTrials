const readline = require('readline');

const rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout
});

rl.question('Enter your name: ', (name) => {
	rl.question('Enter your age: ', (age) => {
		const greeting = "Hello ";
		console.log(greeting + name);
		console.log("You are " + age + " years old");
		rl.close();
	});
});
