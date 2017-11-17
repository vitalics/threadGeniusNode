let data;
var xhr = new XMLHttpRequest();
xhr.open('GET', 'http://localhost:8000/getCatalogs.json', true);
xhr.onload = async () => {
    console.log('DONE', xhr.status);
    data = await xhr.responseText;
    console.log(data);
    let dataSelector = document.querySelector('#catalogs');

    dataSelector.innerHTML += data;
};
xhr.send();

