function DownloadButton(props){
    return  <button class="btn btn-dark mx-auto d-flex btn-lg">
        <a href="{{ lab_object.file.url }}" style="color: white;">Загрузить</a>
    </button>;
}

ReactDOM.render(<DownloadButton/>,
    document.getElementById('download'))