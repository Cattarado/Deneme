function hesapla() {

    var toplam = 0;
    if (document.getElementById("kucuk").checked) {
        toplam += 17;
    }
    else if (document.getElementById("orta").checked) {
        toplam += 22;
    }
    else
        toplam += 27;

    if (document.getElementById("kalın").checked) {
        toplam += 2;
    }

    if (document.getElementById("peynir").checked) {
        toplam += 3;
    }
    if (document.getElementById("sogan").checked) {
        toplam += 1.5;
    }
    if (document.getElementById("ybiber").checked) {
        toplam += 1;
    }
    if (document.getElementById("kbiber").checked) {
        toplam += 2;
    }
    if (document.getElementById("ancuez").checked) {
        toplam += 3;
    }

    if ((document.getElementById("peynir").checked && document.getElementById("ybiber").checked) ||
        (document.getElementById("kbiber").checked) && document.getElementById("ancuez")) {
        toplam -= 2;
    }
    alert("Toplam tutar :" + toplam + " TL");
}