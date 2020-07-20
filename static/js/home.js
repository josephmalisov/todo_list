function newList() {
    url = "/newList"
    $.get(url, null, function(response) {
        window.location.href = response;
    })

}