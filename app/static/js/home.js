document.addEventListener("DOMContentLoaded", () => {
  var body = document.getElementsByTagName('body')[0]
  var readyToUpload = false
  var form = document.getElementsByName('my-form')[0]
  var uploadBtn = document.querySelector("#upload-btn")
  var file;
  form.addEventListener("change", () => {
    if(form.files.length == 1) {
      if(form.files[0].type.split('/')[0] == "image" && form.files[0].size/1024/1024 <= 5) {
        readyToUpload = true
        file = form.files[0]
      }
    }
  })

  uploadBtn.addEventListener('click', (e) => {
    e.preventDefault()
    if(!readyToUpload) return;
    uploadFile(file)
  })

  function uploadFile() {
    const formData = new FormData()
    formData.append('image-file', file)
    formData.append('user-name', "Sam")
    url = window.location.origin;
    fetch(url+'/upload', {
      method: 'POST',
      body: formData
    })
    // .then(response => response.json())
    // .then(data => {
    //   console.log('data: ', data)
    // })
    .then(res => res.blob())
    .then(blob => {
      displayImageFromBlob(blob)
    })
    .catch(e => {
      console.log('error in fetch: ', e)
    })
  }

  function displayImageFromBlob(blob) {
    var blobUrl = URL.createObjectURL(blob)
    var imgElement = createElement('img', '', '', [], {}, {'src': blobUrl})
    body.appendChild(imgElement)
  }

})

function createElement(tagName, className, text, childElements, cssProperties, elementAttributes) {
  var e = document.createElement(tagName)
  if(className !== '') e.classList.add(className)
  if(text !== '') e.appendChild(document.createTextNode(text)) 
  if(childElements.length > 0) {
    childElements.forEach(child => {
      e.appendChild(child)
    })
  }
  Object.keys(cssProperties).forEach(key => {
    e.style[key] = cssProperties[key]
  })
  Object.keys(elementAttributes).forEach(key => {
    e[key] = elementAttributes[key]
  })
  return e
}