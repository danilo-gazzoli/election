const container = document.getElementById('container');
const registerBnt = document.getElementById('register');
const loginBnt = document.getElementById('login');

registerBnt.addEventListener('click', () => {
    container.classList.add("active");
});

loginBnt.addEventListener('click', () => {
    container.classList.remove("active");
});