const input = document.getElementById('upload-file');

input.addEventListener('change', (e) => {
    var result = e.target.files[0];
    var reader = new FileReader();
    reader.readAsText(result);
    reader.addEventListener('load', function () {
        const list = reader.result.split('\r\n');
        const newList = Array(9);
        for (let i = 0; i < list.length; i++) {
            newList[i] = list[i].split(',').map(Number);;
        }
        const numbers = form.number;
        for (let i = 0; i < numbers.length; i++) {
            numbers[i].value = "";
            if (newList[Math.floor(i / 9)][i % 9] != 0) {
                numbers[i].value = newList[Math.floor(i / 9)][i % 9];
            }
        }
    })
});