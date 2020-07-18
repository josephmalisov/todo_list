function newList() {
    url = "/newList"
    $.get(url, null, function(response) {
        newURL = JSON.stringify(response)
        window.location.href = newURL;
    })

}