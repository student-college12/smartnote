function addTask() {
  let task = document.getElementById("taskInput").value;

  if (task === "") {
    alert("Please enter a task");
    return;
  }

  let li = document.createElement("li");
  li.textContent = task;

  let btn = document.createElement("button");
  btn.textContent = "Delete";
  btn.className = "delete-btn";

  btn.style.marginLeft = "10px";

  btn.onclick = function () {
    li.remove();
  };

  li.appendChild(btn);
  document.getElementById("taskList").appendChild(li);

  document.getElementById("taskInput").value = "";
}