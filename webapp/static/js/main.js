

function createImage(url){
    var img = new Image()
    img.src = `/static/cards/${url}.svg`
    return img
}

function getNewData(){
    
    let request = new Request('/cards')

    var cardList = document.getElementById("cards");
    cardList.innerHTML = '';

    fetch(request)
    .then(response => response.json())
    .then(data => {

        data.forEach(element => {
            console.log(element)
            var ul = document.getElementById("cards");
            var li = document.createElement("li");
            li.appendChild(createImage(element));
            ul.appendChild(li);
        });
    });
}

// Get my button
document.getElementById("refresh").addEventListener('click', getNewData)

document.onload = getNewData()

