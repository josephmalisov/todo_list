/** 
 * Joseph Malisov
 * July 2020
 * 
 */

var origin = window.location.origin;

var items = []

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

        $("#results").empty();

        var client = new HttpClient();
        client.get(origin + "/todo/" + userInput, function(response) {
            console.log(response);
            response = JSON.parse(response);
            console.log(response);
            for (i in response["Title"]) { //loop to add results
                $("#results").append(todo_card_maker(response));
                var currItem = []
                for (j in response) {
                    currItem.push(response[j][i])
                }
                items.push(currItem)
            }
        });

    } catch (exception) {
        console.log("Error: " + exception);
    }
}

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
    $.post(origin + "/todo", jsonObject, function(response) { updateResults() })
}

function deleteButton() {

}

//fetch notes
updateResults();

//hide add display
$("#addCard").hide();

function deleteButton(id) {
    $.post(origin + "/todo/del", JSON.stringify(id), function(response) { updateResults() })
}

function dark_mode() {
    $("body").css('background-color', '#263c57')
}