function opt1() {
  var x = (document.getElementById("Column1").innerHTML =
    '<th scope="col">IDnt</th>');
}

function opt2() {
  var x = (document.getElementById("Column2").innerHTML =
    '<th scope="col">IDnt</th>');
}

function change_tbl() {
  var Str = "";
}

function hideFunction() {
  var x = document.getElementById("table2");
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
  var y = document.getElementById("table3");
  if (y.style.display === "none") {
    y.style.display = "block";
  } else {
    y.style.display = "none";
  }
}

function hideFunction2() {
  var x = document.getElementById("table1");
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
}
function open() {
  window.open("{% url 'add-item' %}");
}
