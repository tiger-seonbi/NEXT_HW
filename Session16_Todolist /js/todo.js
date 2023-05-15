const todoForm = document.getElementById("todo-form");
const todoList = document.getElementById("todo-list");
const submitBtn = document.querySelector(".submitBtn");
let local_array = [];
const todo_array = 'todo_array';



function submitAddTodo(event){
    event.preventDefault(); //새로고침 방지
    const todoValue = document.querySelector("#content")
    const todo_value = todoValue.value; 
    const new_todo = {text: todo_value, id: Date.now(), };
    local_array.push(new_todo);
    //window.localStorage.setItem(todo_array , local_array);
    todoValue.value = '';
    paintTodo(new_todo);
    saveTodo();
};

function paintTodo(new_todo) {

    //console.log(typeof(todowork_str));
    const todo_ul_li = document.createElement('li');
    todo_ul_li.id = new_todo.id;
    const todo_content = document.createElement('span');
    todo_content.innerHTML = new_todo.text;
    const todo_delete_btn = document.createElement('button');
    todo_delete_btn.innerHTML = 'X';
    todo_delete_btn.addEventListener('click', deleteTodo);
    todoList.appendChild(todo_ul_li);
    todo_ul_li.appendChild(todo_content);
    todo_ul_li.appendChild(todo_delete_btn);
};

function deleteTodo(event) {
    const li = event.target.parentElement;
    li.remove();
  
    local_array = local_array.filter((item) => item.id !== parseInt(li.id));
    window.localStorage.setItem(todo_array, JSON.stringify(local_array));
};

function saveTodo() {
    window.localStorage.setItem(todo_array, JSON.stringify(local_array));
};

let temp = window.localStorage.getItem(todo_array);

if (temp !== null) {
    const temp_parsed = JSON.parse(temp);
    let local_array = temp_parsed;
    //console.log(local_array);
    local_array.forEach(element => paintTodo(element));
};

todoForm.addEventListener('submit', submitAddTodo);