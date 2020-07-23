document.addEventListener("DOMContentLoaded", () => {
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
    console.log(url)
    fetch(url+'/upload', {
      method: 'POST',
      body: formData
    })
    .then(response => response.json())
    .then(data => {
      console.log('data: ', data)
    })
    .catch(e => {
      console.log('error in fetch: ', e)
    })

  }

})