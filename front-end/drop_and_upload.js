let dropArea = document.getElementById("drop-area");

//Creates event listeners for the actions of the user in the drop-area
['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
    dropArea.addEventListener(eventName, preventDefaults, false)
});

function preventDefaults(e) {
    e.preventDefault();
    e.stopPropagation();
}

['dragenter', 'dragover'].forEach(eventName => {
    dropArea.addEventListener(eventName, highlight, false)
});

['dragleave', 'drop'].forEach(eventName => {
    dropArea.addEventListener(eventName, unhighlight, false)
})

function highlight(e) {
    dropArea.classList.add('highlight')
}

function unhighlight(e) {
    dropArea.classList.remove('highlight')
}


//Handles when image is dropped
dropArea.addEventListener('drop', handleDrop, false)
function handleDrop(e) {
    let dt = e.dataTransfer
    let files = dt.files
    handleFiles(files)
}

function handleFiles(files) {
    //For each image in the array, upload it
    ([...files]).forEach(uploadImage)
}

function uploadImage(image) {
    //TODO: Use Google Photos API to upload the images
    console.log(image.name)
}