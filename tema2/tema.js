var tds = document.querySelectorAll("td");

function clear(elem) {
	elem.textContent = "";
	contor = 0;
	checkTurn();
}

document.getElementById('unu').addEventListener("click", function () {
	for (var i = 0; i < tds.length; ++i) {
		clear(tds[i]);
	}
});

function rand() {
	var x = Math.floor(Math.random() * 10 % 9);
	if (positions[x].textContent == "") {
		positions[x].textContent = '0';
		event.stopImmediatePropagation();
		checkTurn();
	}else{
		rand();
	}
}

function checkTurn() {
	document.getElementById('trei').disabled = true;
    document.getElementById('trei').value = "Please wait...";
    return true;
}

function resetTurn() {
    document.getElementById('trei').disabled = false;
    document.getElementById('trei').value = "Submit";
  }

var positions = [8];
positions[0] = document.getElementById('one');
positions[1] = document.getElementById('two');
positions[2] = document.getElementById('three');
positions[3] = document.getElementById('four');
positions[4] = document.getElementById('five');
positions[5] = document.getElementById('six');
positions[6] = document.getElementById('seven');
positions[7] = document.getElementById('eight');
positions[8] = document.getElementById('nine');

var contor = 0;
checkTurn();
for (var i = 0; i < 9; ++i) {
		tds[i].addEventListener("click", function () {	
			if (contor % 2 == 0) {
				if (this.textContent == "") {
					this.textContent = "X";
				}
				if(contor != 8) {
					resetTurn();
				}

				contor++;
			}
		});
		document.getElementById('trei').addEventListener("click", function () {
			rand();
			contor++;
		});

}

document.getElementById('doi').addEventListener("click", function () {
	checkTurn();
	var contor2 = 0;
	if (positions[0].textContent == positions[1].textContent) {
		if (positions[0].textContent == positions[2].textContent) {
			if (positions[0].textContent == 'X') {
				console.log('Ai castigat');
				contor2++;
			}
		}
	} 
	if (positions[0].textContent == positions[4].textContent) {
		if (positions[4].textContent == positions[8].textContent) {
			if (positions[0].textContent == 'X') {
				console.log('Ai castigat');
				contor2++;
			}
		}
	}
	if (positions[0].textContent == positions[3].textContent) {
		if (positions[0].textContent == positions[6].textContent) {
			if (positions[0].textContent == 'X') {
				console.log('Ai castigat');
				contor2++;
			}
		}
	}
	if (positions[3].textContent == positions[4].textContent) {
		if (positions[3].textContent == positions[5].textContent) {
			if (positions[3].textContent == 'X') {
				console.log('Ai castigat');
				contor2++;
			}
		}
	}
	if (positions[6].textContent == positions[7].textContent) {
		if (positions[6].textContent == positions[8].textContent) {
			if (positions[6].textContent == 'X') {
				console.log('Ai castigat');
				contor2++;
			}
		}
	}
	if (positions[1].textContent == positions[4].textContent) {
		if (positions[1].textContent == positions[7].textContent) {
			if (positions[1].textContent == 'X') {
				console.log('Ai castigat');
				contor2++;
			}
		}
	}
	if (positions[2].textContent == positions[5].textContent) {
		if (positions[2].textContent == positions[8].textContent) {
			if (positions[2].textContent == 'X') {
				console.log('Ai castigat');
				contor2++;
			}
		}
	}
	if (positions[2].textContent == positions[4].textContent) {
		if (positions[2].textContent == positions[6].textContent) {
			if (positions[2].textContent == 'X') {
				console.log('Ai castigat');
				contor2++;
			}
		}
	}

	if (contor2 == 0) {
		console.log('Nu ai castigat');
	}
	
});
