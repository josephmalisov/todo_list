// html text for card item

function todo_card_maker(response) {
    return `
<div class="card bg-success m-4" id="${response["id"][i]}">
    <div class="card-header">
        <h6>${response["Title"][i]}</h6>
    </div>
    <div class="card-body">
        <h6>${response["Description"][i]}</h6>
    </div>
    <div class="card-footer">
        <div class="row">
            <div class="col">
                <button type="button" class="material-icons btn btn-danger m-2" id="${response["id"][i]}" onclick="deleteButton(this.id)">delete_forever
                </button>
            </div>
        </div>
    </div>
</div>`
}