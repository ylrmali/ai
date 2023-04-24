upload_input = document.getElementById('upload')
upload_label = document.getElementById('id_zip_file_label')

upload_input.onchange = event => {
    console.log(event);
    const [file] = [upload_input.files];
    const fileName = file[0]['name'];
    upload_label.innerHTML = "<i class=\"fa-solid fa-folder\" style=\"color: #ebc50a;font-size: 64px\"></i>" +
        `${fileName}`;

}