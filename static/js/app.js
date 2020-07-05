/** 
 * Joseph Malisov
 * July 2020
 * 
 */

var origin = window.location.origin;

//credit to https://stackoverflow.com/questions/247483/http-get-request-in-javascript
var HttpClient = function() {
    this.get = function(aUrl, aCallback) {
        var anHttpRequest = new XMLHttpRequest();
        anHttpRequest.onreadystatechange = function() {
            if (anHttpRequest.readyState == 4 && anHttpRequest.status == 200)
                aCallback(anHttpRequest.responseText);
        }

        anHttpRequest.open("GET", aUrl, true);
        anHttpRequest.send(null);
    }
}

//UPDATING HTML

function updateResults() {
    try {
        var resultsElement = document.getElementById("results"); //get the html element where we will display results
        resultsElement.innerHTML = null; //get rid of any old results
        var userInput = document.getElementById("userInput").value; //get whatever is in the text field
        // if (userInput.length < 1) {
        //     return;
        // }


        var client = new HttpClient();
        client.get(origin + "/todo/" + userInput, function(response) {
            console.log(response);
            response = JSON.parse(response);
            console.log(response);
            for (i in response["Title"]) { //loop to add results
                var p = document.createElement("p");
                var node = document.createTextNode(response["Title"][i] +
                    ",  " + response["Description"][i]);
                p.appendChild(node);
                resultsElement.appendChild(p);
            }
        });

    } catch (exception) {
        console.log("Error: " + exception);
    }
}

updateResults();