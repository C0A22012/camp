inu = "aiue"
async function callApi() {
    let element = document.getElementById("search-text");
    console.log(element.value);
    
    const res = await fetch('http://127.0.0.1:8000?word=' + element.value)
    .then((data) => {
        deta.json() // {"result": ""}
        const s = document.querySelector('.s');
        s.innerText =data.json()["result"];
        
    })
};

// const s = document.querySelector('.s');
// s.innerText = "Hello!";