//FIX uploadImage function at the bottom
const cloudName = 'dth0ow8ry';
const unsignedUploadPreset = 'l2ejxlbz';

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

function uploadImage(file) {
    //TODO: Use Google Photos API to upload the images
    
    //textBox.value: Name (text)
    //file: File object of Image
    
    if(img_dict[textBox.value] == undefined) {
        //                   Just [img] here will not print anything
        console.log(typeof file)
        img_dict[textBox.value] = [file]
    } else {
        img_dict[textBox.value].push(file)
    }
    
    
  var url = `https://api.cloudinary.com/v1_1/${cloudName}/upload`;
  var xhr = new XMLHttpRequest();
  var fd = new FormData();
  xhr.open('POST', url, true);
  xhr.setRequestHeader('X-Requested-With', 'XMLHttpRequest');

  // // Reset the upload progress bar
  //  document.getElementById('progress').style.width = 0;
  
  // // Update progress (can be used to show progress indicator)
  // xhr.upload.addEventListener("progress", function(e) {
  //   var progress = Math.round((e.loaded * 100.0) / e.total);
  //   document.getElementById('progress').style.width = progress + "%";

  //   console.log(`fileuploadprogress data.loaded: ${e.loaded},
  // data.total: ${e.total}`);
  // });

  xhr.onreadystatechange = function(e) {
    if (xhr.readyState == 4 && xhr.status == 200) {
      // File uploaded successfully
      var response = JSON.parse(xhr.responseText);
      // https://res.cloudinary.com/cloudName/image/upload/v1483481128/public_id.jpg
      var url = response.secure_url;
      // Create a thumbnail of the uploaded image, with 150px width
      var tokens = url.split('/');
      tokens.splice(-2, 0, 'w_150,c_scale');
      var img = new Image(); // HTML5 Constructor
      img.src = tokens.join('/');
      img.alt = response.public_id;
      document.getElementById('gallery').appendChild(img);
    }
  };

  fd.append('upload_preset', unsignedUploadPreset);
  fd.append('tags', 'browser_upload'); // Optional - add tag for image admin in Cloudinary
  fd.append('file', file);
  xhr.send(fd);
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