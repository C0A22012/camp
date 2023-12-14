async function callApi() {
    let element = document.getElementById("search-text");
    console.log(element.value);
    const res = await fetch('http://127.0.0.1:8000word=' + element.value)
        .then(result => result.json())
        .then((output) => {
            console.log('Output: ', output);
            let tmpVal = output["date"];
            console.log( String(tmpVal) );
        }).catch(err => console.error(err));
};
    
    // const res = await fetch('http://127.0.0.1:8000')
    //   .then(result => result.json())
