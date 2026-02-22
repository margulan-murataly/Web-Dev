const input = document.getElementById("item-name");
const add = document.getElementById("add-item");
const list = document.getElementById("item-list");
const form = document.getElementById("forma");
add.addEventListener("click", function() {
    const text = input.value.trim();

    if(!text) {
        return;
    }

    const li = document.createElement("li");
    li.textContent = text;

    const del = document.createElement("button");


    del.className = "delete";
    

    li.appendChild(del);

    list.appendChild(li);

    input.value = "";
})

form.addEventListener("click", function() {
    li.remove();
})