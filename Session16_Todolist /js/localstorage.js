const username = document.querySelector('.username');
const usernameWrapper = document.querySelector('.usernameWrapper');
const header = document.querySelector('#header');


function checkusername() {
    const checkName = window.localStorage.getItem("username");
    if (checkName) {
        usernameWrapper.style.display ="none";
        header.innerHTML = `<h1> ${window.localStorage.getItem(
            "username"
        )} 의 Todo List</h1><button type="button" onclick="resetUsername()">초기화</button>`; 
    } else {
        usernameWrapper.style.display = "flex";
        header.innerHTML = " ";
    }
}

checkusername();

function setUsername() {
    const usernamevalue = username.value;
    window.localStorage.setItem('username', usernamevalue);
    username.value = '';
    checkusername();
}

function resetUsername() {
    window.localStorage.removeItem("username");
    console.log("username 초기화");
    checkusername();
}