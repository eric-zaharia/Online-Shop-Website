var lista = [];
var start = prompt('Daca vrei sa incepi, scrie y, altfel n');
var x = '';

function add() {
  var numeAd = prompt('Ce nume vrei sa adaugi?');
  lista.push(numeAd);
}

function remove() {
  var numeSters = prompt('Ce nume vrei sa stergi?');
  var index = lista.indexOf(numeSters);
  if (index !== -1) {
    lista.splice(index, 1);
  }
}

function display() {
  console.log(lista);
}

if(start === 'y') {
  while(x !== 'quit') {
    x = prompt('alege: add, remove, display sau quit')
    if (x === 'add') {
      add();
    }else if (x === 'display') {
      display();
    }else if (x === 'remove') {
      remove();
    }
  }
}

alert('Forta Dinamo aleeee');