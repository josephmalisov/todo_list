/** 
 * Joseph Malisov
 * July 2020
 * 
 */

var origin = window.location.origin;

ID_COLUMN = "id";
TITLE_COLUMN = "Title"
DESCRIPTION_COLUMN = "Description"
IS_DONE_COLUMN = "_is_done"
IS_DELETED_COLUMN = "_is_deleted"
CREATED_ON_COLUMN = "CreatedOn"
DUE_DATE_COLUMN = "DueDate"
USER_ID_COLUMN = "UserId"


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
            addItems(response);

            renderAll();
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

function deleteButton(id) {
    $.post(origin + "/todo/del", JSON.stringify(id), function(response) {
        $("#" + id).remove();
        delete addItems["id"];
    })
}

function checkButton(id) {
    $.post(origin + "/todo/done", JSON.stringify(id), function(response) { updateResults() })
}

//fetch notes
updateResults();

//hide add display
$("#addCard").hide();

function dark_mode() {
    $("body").css('background-color', '#263c57')
}