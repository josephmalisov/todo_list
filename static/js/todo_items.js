// todo_items

var todo_items = {};

function addItems(response) {
    ID_COLUMN = "id";
    TITLE_COLUMN = "Title"
    DESCRIPTION_COLUMN = "Description"
    IS_DONE_COLUMN = "_is_done"
    IS_DELETED_COLUMN = "_is_deleted"
    CREATED_ON_COLUMN = "CreatedOn"
    DUE_DATE_COLUMN = "DueDate"
    USER_ID_COLUMN = "UserId"

    console.log(response[IS_DELETED_COLUMN][0])

    try {
        for (j in response["id"]) {
            todo_items[`${j}`] = new Todo_item(
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

function renderAll() {
    for (i in todo_items) {
        todo_card_maker(i)
    }
}