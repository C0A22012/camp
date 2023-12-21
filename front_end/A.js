inu = "aiue"
async function callApi() {
    let element = document.getElementById("search-text");
    console.log(element.value);
    
    fetch('http://127.0.0.1:8000/camp?word=' + String(element.value))
    .then((data) => data.json())
    .then((data) => {
        // data.json() // {"result": ""}
        const s = document.querySelector('.s');
        console.log(data)
        s.innerText = data["result"];
        
    })
};

// const s = document.querySelector('.s');
// s.innerText = "Hello!";