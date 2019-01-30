var button = document.getElementById("myButton");

button.onclick = function () {
  alert("Hello, World");
}

function refresh_todos() {
  $.get("/todos", function (data) {
    for (let todo of data) {
      console.log(todo);
    }  
  });
}

refresh_todos();