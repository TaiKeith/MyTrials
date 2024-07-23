document.addEventListener('DOMContentLoaded', function () {
	const loginButton = document.getElementById('loginButton');
	const loginContainer = document.querySelector('.loginContainer'); // Class Selector because in my html file, i used class="loginContainer" instead of id

	const signUpButton = document.getElementById('signUp');
	const signUpContainer = document.getElementById('signUpContainer');

	loginButton.addEventListener('click', function (e) {
		e.preventDefault();
		// Toggle the visibility of the login form
		loginContainer.style.display = loginContainer.style.display === 'none' ? 'block' : 'none';
	});

	signUpButton.addEventListener('click', function (e) {
		e.preventDefault();
		signUpContainer.style.display = signUpContainer.style.display === 'none' ? 'block' : 'none';
	});

	document.getElementById('loginForm').addEventListener('submit', function (e) {
		e.preventDefault();

		const username = document.getElementById('username').value;
		const password = document.getElementById('password').value;

		if (username === '@Tai_Keith' && password === 'Tai@3.142') {
			alert('Login Successful!');
		} else {
			alert('Login Failed. Please check your credentials!');
		}
	});

	document.getElementById('signUpForm').addEventListener('submit', function (e) {
		e.preventDefault();

		const firstPassword = document.getElementById('firstPassword').value;
		const secondPassword = document.getElementById('secondPassword').value;

		if (firstPassword === secondPassword) {
			alert('Password created Successfully!');
		} else {
			alert('Passwords mismatch. Please make sure they are the same!');
		}
	});
});
