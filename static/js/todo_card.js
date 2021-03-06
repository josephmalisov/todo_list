// html text for card item

function todo_card_maker(todo_item) {
    try {
        console.log(todo_item)
        var isDone = todo_item["isDone"] % 2;
        var bg_color = ""
        var check_button_color
        if (isDone) {
            bg_color = "bg-success"
            check_button_color = "btn-dark"
        } else {
            bg_color = "orange"
            check_button_color = "btn-dark"
        }
        return `
<div class="card ${bg_color} m-4" id="${todo_item["id"]}">
    <div class="card-header pb-0">
        <div class="row">
            <div class="col-8">
                <h4><b class="title p-1">${todo_item["title"]}</b></h4>
            </div>
        </div>
    </div>
    <div class="card-body">
        <h6 class="description p-1">${todo_item["description"]}</h6>
    </div>
    <div class="card-footer p-1">
            <div class="row mx-auto">
                <div class="col">
                    <button type="button" class="btn ${check_button_color} m-0 border border-dark" id="${todo_item["id"]}" onclick="checkButton(this.id)">
                        <i class="fas fa-check-circle" style="font-size:2rem;color:green;"></i>
                    </button>
                </div>
                <div class="col my-auto">
                    <button type="button" class="material-icons btn btn-danger m-0 border-dark" id="${todo_item["id"]}" onclick="deleteButton(this.id)">
                        delete_forever
                    </button>
                </div>
                <div class="col my-auto">
                    <button type="button" class="material-icons btn btn-info m-0 border-dark" id="${todo_item["id"]}" onclick="editButton(this.id)">
                        <i class="fas fa-pencil-alt"></i>
                    </button>
                </div>
            </div>
        </div>
    </div>
</div>`
    } catch (e) {
        console.log("Error: " + e)
    }
}