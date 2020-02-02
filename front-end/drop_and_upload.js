//FIX uploadImage function at the bottom

let dropArea = document.getElementById("drop-area");
let textBox = document.getElementById('text-box');
let img_dict = new Object();

//Creates event listeners for the actions of the user in the drop-area
['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
    dropArea.addEventListener(eventName, preventDefaults, false)
});

Object.size = function(obj) {
    var size = 0, key;
    for (key in obj) {
        if (obj.hasOwnProperty(key)) size++;
    }
    return size;
};

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


//For each image in the array, upload it and display name
function handleFiles(files) {
    //Changes files from FileList into array
    files = [...files]
    files.forEach(uploadImage)
        //uploadImage(files[files.length-1])
    files.forEach(viewImageNames)
    files.forEach(previewImage)
}

//Image preview (currently displays the "Name: Img-name")
function viewImageNames(image) {
    let reader = new FileReader()
    reader.readAsDataURL(image)
    reader.onloadend = function() {
        let img = document.createElement('img')
        img.src = reader.result
        //document.getElementById('gallery').appendChild(img)
        document.getElementById('gallery_names').innerHTML += '<p class="name-img">' + textBox.value + ': ' + image.name + '</p>'
        
        
    }
}

function previewImage(image) {
    let reader = new FileReader()
    reader.readAsDataURL(image)
    reader.onloadend = function() {
        let img = document.createElement('img')
        img.src = reader.result;
        document.getElementById('gallery').className = 'small';
        document.getElementById('gallery').appendChild(img);
    }
}

function uploadImage(img) {
    //TODO: Use Google Photos API to upload the images
    
    //textBox.value: Name (text)
    //img: File object of Image
    
    if(img_dict[textBox.value] == undefined) {
        //                   Just [img] here will not print anything
        console.log(typeof img)
        img_dict[textBox.value] = [img]
    } else {
        img_dict[textBox.value].push(img)
    }
    
    //fix
    console.log(JSON.stringify(img_dict))
}

document.getElementById('deleteAll').onclick = function() {
    document.getElementById('gallery_names').innerHTML = '';
    document.getElementById('gallery').innerHTML = '';
    document.getElementById('gallery').style.display = 'none';
    for (var i in img_dict) delete img_dict[i];
};


document.getElementById('preview').onclick = function() {
    document.getElementById('gallery').className = 'small';
    document.getElementById('gallery').style.display = 'block';
}



function print_dict(the_keys) {
    for(var i = 0; i<Object.size(img_dict); i++) {
        console.log(img_dict[the_keys[i]].name)
    }
}