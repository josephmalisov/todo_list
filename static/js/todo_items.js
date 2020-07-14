// todo_items

var todo_items = {};

function addItems(response) {
    try {
        for (j in response["id"]) {
            todo_items[`${response[ID_COLUMN][j]}`] = new Todo_item(
                response[ID_COLUMN][j],
                response[TITLE_COLUMN][j],
                response[DESCRIPTION_COLUMN][j],
                response[IS_DONE_COLUMN][j],
                response[IS_DELETED_COLUMN][j],
                response[CREATED_ON_COLUMN][j],
                response[DUE_DATE_COLUMN][j],
                response[USER_ID_COLUMN][j])
            console.log(`added ${j} to todo_items\n`)
        }
        console.log(todo_items)
    } catch (exception) {
        console.log("Error: " + exception);
    }
}

function renderAll(items_list) {
    for (i in items_list) {
        renderItem(items_list[i])
    }
}

function renderItem(item) {
    var isDone = item["isDone"] % 2;
    if (!isDone) {
        $("#results").append(todo_card_maker(item))
    } else {
        $("#results-done").append(todo_card_maker(item))
    }
}