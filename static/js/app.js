/** 
 * Joseph Malisov
 * July 2020
 * 
 */

var origin = window.location.origin;
var my_url = window.location.href;
var id_url = my_url.split(origin + '/')[1]
var todo_url = origin + "/todo/" + id_url


ID_COLUMN = "id";
TITLE_COLUMN = "title"
DESCRIPTION_COLUMN = "description"
IS_DONE_COLUMN = "_is_done"
IS_DELETED_COLUMN = "_is_deleted"
CREATED_ON_COLUMN = "created"
DUE_DATE_COLUMN = "due"
USER_ID_COLUMN = "userid"


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
        // if (userInput.length < 1) {
        //     return;
        // }

        $("#results").empty();

        var client = new HttpClient();
        client.get(todo_url, function(response) {
            console.log(response);
            response = JSON.parse(response);
            console.log(response);
            addItems(response);

            renderAll(todo_items);
        });

    } catch (exception) {
        console.log("Error: " + exception);
    }
}

function addButton() {
    $("#addCard").toggle();
}

function addNote() {
    // var myusername = $("#username").val();
    //TODO: fix this username biz
    var myusername = ""

    var mytext = $("#newTitle").val();
    var mydescription = $("#newDescription").val();

    console.log(mytext);
    console.log(mydescription);


    var myObj = { username: myusername, text: mytext, description: mydescription, list: id_url };
    var jsonObject = JSON.stringify(myObj);
    console.log(JSON.parse(jsonObject));

    //post the new note
    $.post(todo_url, jsonObject, function(response) { updateResults() })
}

function deleteButton(id) {
    myObj = { id: id }
    $.post(origin + "/todo/del", JSON.stringify(myObj), function(response) {
        $("#" + id).remove();
        delete todo_items[`${id}`];
    })
}

function checkButton(id) {
    $.post(origin + "/todo/done", JSON.stringify(id), function(response) {
        curr_item = todo_items[`${id}`]

        $("#" + id).remove();
        curr_item.set("isDone", !curr_item["isDone"])
        renderItem(curr_item)
    })
}

function editButton(id) {
    titleSelector = $(`#${id}`).find(".title")
    descSelector = $(`#${id}`).find(".description")

    if (titleSelector.attr('contentEditable') == 'true') {
        mytitle = titleSelector.text();
        mydescription = descSelector.text();

        myObj = {
            [ID_COLUMN]: id,
            [TITLE_COLUMN]: mytitle,
            [DESCRIPTION_COLUMN]: mydescription
        }

        //put request
        $.post(origin + "/todo/edit", JSON.stringify(myObj), function(response) {
            curr_item = todo_items[`${id}`]
            curr_item.set("title", mytitle)
            curr_item.set("description", mydescription)

            titleSelector.attr('contentEditable', 'false')
            descSelector.attr('contentEditable', 'false')

            //add a border to indicate edit state
            titleSelector.removeClass("border rounded")
            descSelector.removeClass("border rounded")
        })
        return
    }

    //make content editable
    titleSelector.attr('contentEditable', 'true')
    descSelector.attr('contentEditable', 'true')

    //add a border to indicate edit state
    titleSelector.addClass("border rounded")
    descSelector.addClass("border rounded")

    console.log(`Editing #${id}`)
}


function search() {
    $("#results").empty()
    $("#results-done").empty()

    userInput = $("#userInput").val() //user enters nothing or clears the box
    if (userInput == "" | userInput == null) {
        return renderAll(todo_items)
    }

    found = {};
    for (i in todo_items) {
        userInputLower = userInput.toLowerCase()
        thisTitle = todo_items[i]["title"].toLowerCase().includes(userInputLower)
        thisDescription = todo_items[i]["description"].toLowerCase().includes(userInputLower)
        if (thisTitle || thisDescription) {
            myId = todo_items[i]["id"]
            found[`${myId}`] = todo_items[i]
        }
    }
    renderAll(found)
}

function copylink() {

    var dummy = document.createElement('input'),
        text = window.location.href;

    document.body.appendChild(dummy);
    dummy.value = text;
    dummy.select();
    document.execCommand('copy');
    document.body.removeChild(dummy);
}

//fetch notes
updateResults();