
function refresh_todos() {
  var todoList = $
  $.getJSON("/todos", function (data) {  
    for (let todo of data) {
      $("<li>" + todo.id + " - " + todo.todo + "</li>").appendTo($("#todolist"));
      console.log(JSON.stringify(todo));
    }  
  });
}

refresh_todos();