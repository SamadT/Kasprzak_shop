let button = document.querySelector("#more_button");
let cover_block = document.querySelector('#Over_block');
let modal_block = document.querySelector('#Modal_window');
let cancel_button = document.getElementById('Cancel_button');
[button, cancel_button].forEach((elem) => {
    elem.addEventListener("click", function(e){
        cover_block.classList.toggle('show_block');
        modal_block.classList.toggle('changing_flow');
    });
});