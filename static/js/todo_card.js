// html text for card item

function todo_card_maker(response) {
    var bg_color = ""
    var check_button_color
    if (parseInt(response["_is_done"][i]) % 2 == "0") {
        bg_color = "bg-warning"
        check_button_color = "btn-dark"
    } else {
        bg_color = "bg-success"
        check_button_color = "btn-dark"
    }
    return `
<div class="card ${bg_color} m-4" id="${response["id"][i]}">
    <div class="card-header pb-0">
        <h4><b>${response["Title"][i]}</b></h4>
    </div>
    <div class="card-body">
        <h6>${response["Description"][i]}</h6>
    </div>
    <div class="card-footer">
        <div class="row">
            <div class="col">
                <button type="button" class="btn ${check_button_color} m-1" id="${response["id"][i]}" onclick="checkButton(this.id)">
                    <i class="fas fa-check-circle" style="font-size:2rem;color:green;"></i>
                </button>
            </div>
            <div class="col">
                <button type="button" class="material-icons btn btn-danger m-2" id="${response["id"][i]}" onclick="deleteButton(this.id)">
                    delete_forever
                </button>
            </div>
        </div>
    </div>
</div>`
}