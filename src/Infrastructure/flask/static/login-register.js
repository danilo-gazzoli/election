
const container = document.getElementById('container');
const registerBnt = document.getElementById('register');
const loginBnt = document.getElementById('login');


// const client = new Client();
// client.setEndpoint('https://cloud.appwrite.io/v1');
// client.setProject('67190bf20007156de551');

// const account = new Account(client);

// export {account, client};

// const acount = new Acount(client);
// async function handleLogin() {
//     acount.createOAuth2Session(
//         'google',
//         'http://localhost:5000/',
//         'http://localhost:5000/'
//     )
// }

registerBnt.addEventListener('click', () => {
    container.classList.add("active");
});

loginBnt.addEventListener('click', () => {
    container.classList.remove("active");
});