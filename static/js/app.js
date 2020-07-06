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
    this.post = function(aUrl, aCallback) {
        var anHttpRequest = new XMLHttpRequest();
        anHttpRequest.onreadystatechange = function() {
            if (anHttpRequest.readyState == 4 && anHttpRequest.status == 200)
                aCallback(anHttpRequest.responseText);
        }

        anHttpRequest.open("POST", aUrl, true);
        anHttpRequest.send(null);
    }
}

//UPDATING HTML

function updateResults() {
    try {
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
                $("#results").append(`
                <div class="card bg-success m-4">
                    <div class="card-header">
                        <h6>${response["Title"][i]}</h6>
                    </div>
                    <div class="card-body">
                        <h6>${response["Description"][i]}</h6>
                    </div>
                </div>`);
            }
        });

    } catch (exception) {
        console.log("Error: " + exception);
    }
}

updateResults();

function addButton() {
    $("#addCard").toggle();
}

function addNote() {
    var mytext = $("#newTitle").val();
    var mydescription = $("#newDescription").val();

    console.log(mytext);
    console.log(mydescription);


    var myObj = { text: mytext, description: mydescription };
    var jsonObject = JSON.stringify(myObj);
    console.log(JSON.parse(jsonObject));


    //post the new note
    $.post("/todo/", jsonObject, updateResults())
}