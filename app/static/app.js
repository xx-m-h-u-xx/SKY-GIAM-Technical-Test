let formQuery = document.getElementById("form-query");
let inputName = document.getElementById("input-name");
let btnSubmit = document.getElementById("submit");

/* Submit event fires whenever user submits a form, prevent normal HTML form submission */
formQuery.addEventListener("submit", event => {
     event.preventDefault();
});


/* Fetch sends POST request to webserver when btnSubmit is clicked 
 * Awaits response from POST Fetch Request made to /webform */
btnSubmit.addEventListener("click", event => {

    let data = {
        'inputName': document.getElementById('input-name').value 
    };

    console.log(data);

    /* Fetch HTTP POST with JSON-encoded data with headers */
    fetch('/webform', {
            method: 'POST', 
            body: JSON.stringify(data),
            headers: {'Content-Type': 'application/json' }
    })

    /* Promise: Returned response from intial POST Fetch Request */
    .then((response) => {
        
        /* Handles error, depending on what status code the server responds with. */
        if (response.status !== 200) {
            console.log(`Ooops! There was a problem. Status code: ${response.status}`);
        }
    })

    /* Callback function, catching errors with Fetch request */
    .catch(function(error){
        console.log("Fetch error: " + error);
    });
}); 