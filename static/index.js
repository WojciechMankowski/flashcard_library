console.log("Hello World!");

function add_input(){
    var input = document.createElement("input");
    var input_definition = document.createElement("input");
    var image = document.createElement("input");
    input.type = "text";
    input.name = "concept";
    input_definition.type = "text";
    input_definition.name = "definition";
    image.type = "file";
    image.name = "file";
    image.accept = "image/*";
    add_label("concept", "Pojęcie");
    document.getElementById("box_form").appendChild(input);
    add_label("definition", "Definicja");
    document.getElementById("box_form").appendChild(input_definition);
    add_label("file", "Obrazek");
    document.getElementById("box_form").appendChild(image);

}

function add_label(name, name_pl){
    var label = document.createElement("label");
    label.innerHTML = name_pl;
    label.for = name;
    var box =  document.getElementById("box_form");
    console.log(box);
    box.appendChild(label);
}
function check_menu(){
    let menu = document.getElementsByClassName("navbar-toggler");
    menu.ariaExpanded = "false";
    console.log(menu.ariaExpanded);
    menu.ariaExpanded = "true";
    }
