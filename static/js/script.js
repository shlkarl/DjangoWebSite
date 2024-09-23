
alert('Данный сайт демонстрирует возможности html для создания интернет страниц, некоторые возможности каскадных таблиц стилей css, а так же основы языка javascript');

function showprod() {
    var popup = document.getElementById("1");
    if (popup.style.display === "none") {
        popup.style.display = "block";
    } else {
        popup.style.display = "none";
    }
}
function showus() {
    var popup = document.getElementById("2");
    if (popup.style.display === "none") {
        popup.style.display = "block";
    } else {
        popup.style.display = "none";
    }
}
function showser() {
    var popup = document.getElementById("3");
    if (popup.style.display === "none") {
        popup.style.display = "block";
    } else {
        popup.style.display = "none";
    }
}
function enter() {
    const popWin = window.open('LK', 'LK',
        'top=150, left=100, width=750, height=500')
}

