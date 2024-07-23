document.addEventListener('DOMContentLoaded', function () {
	const loginButton = document.getElementById('loginButton');
	const loginContainer = document.getElementById('loginContainer');

	loginButton.addEventListener('click', function (e) {
		e.preventDefault();
		// Toggle the visibility of the login form
		loginContainer.style.display = loginContainer.style.display === 'none' ? 'block' : 'none';
	});

	document.getElementById('loginForm').addEventListener('submit', function (e) {
		e.preventDefault();

		const username = document.getElementById('username').value;
		const password = document.getElementById('password').value;

		if (username === '@Tai_Keith' && password === 'Tai_Keith@3.142') {
			alert('Login Successful!');
		} else {
			alert('Login failed. Please check your credentials!');
		}
	});
});
