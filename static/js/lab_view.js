function get_file() {
    const category_id = "{{ lab_object.category.id }}";
    var request = new XMLHttpRequest();

    function reqReadyStateChange() {
        if (request.readyState == 4 && request.status == 200)
            location.reload();
    }
    request.open("GET", "{% url 'inc_download_category' %}?" + `category=${category_id}&lab={{ lab_object.id }}`);
    request.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    request.onreadystatechange = reqReadyStateChange;
    request.send();
    window.location.href = '{{ lab_object.file.url }}';
}

function add_reputation(){
    alert({{ user.get_fullname }})
}


function sub_reputation(){
  
}