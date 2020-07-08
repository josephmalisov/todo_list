// Todo_item.js

class Todo_item {
    constructor(id, title, description, isDone, isDeleted, createdOn, dueDate, userId) {
        this.id = id;
        this.title = title;
        this.description = description;
        this.isDone = isDone;
        this.isDeleted = isDeleted;
        this.createdOn = createdOn;
        this.dueDate = dueDate;
        this.userId = userId;
        this.renderItem = function() {
            todo_card_maker(this)
        }
    }
}