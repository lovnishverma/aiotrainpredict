var button = document.getElementById("myButton");

button.onclick = function () {
  alert("Hello, World");
}

function refresh_todos() {
  var todoList = $
  $.getJSON("/todos", function (data) {  
    for (let todo of data) {
      $("<li>x</li>").appendTo("#todolist")
      console.log(JSON.stringify(todo));
    }  
  });
}

refresh_todos();