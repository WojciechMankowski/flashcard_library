console.log("Hello World!");

function add_input(){
    var input = document.createElement("input");
    var input_definition = document.createElement("input");
    input.type = "text";
    input.name = "concept";
    input_definition.type = "text";
    input_definition.name = "definition";
    add_label("concept", "Pojęcie");
    document.getElementById("box_form").appendChild(input);
    add_label("definition", "Definicja");
    document.getElementById("box").appendChild(input_definition);
}

function add_label(name, name_pl){
    var label = document.createElement("label");
    label.innerHTML = name_pl;
    label.for = name;
    var box =  document.getElementById("box_form");
    console.log(box);
    box.appendChild(label);
}