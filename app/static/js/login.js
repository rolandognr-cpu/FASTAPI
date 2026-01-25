console.log('Hello from FastAPI!')

const alertPlaceholder = document.getElementById('liveAlertPlaceholder')
const buttonEl = document.querySelector('button')
const emailField = document.getElementById('exampleInputEmail1')
const passwordField = document.getElementById('exampleInputPassword1')


function appendAlert(message, type) {
  const wrapper = document.createElement('div')
  wrapper.innerHTML = [
    `<div class="alert alert-${type} alert-dismissible" role="alert">`,
    `   <div>${message}</div>`,
    '   <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>',
    '</div>'
  ].join('')

  alertPlaceholder.append(wrapper)
}

buttonEl.addEventListener('click', event => {
    // event.preventDefault()
    // const formData = new FormData(formEl)
    interestingData = JSON.stringify({'email': emailField.value, 'password': passwordField.value})

    console.log(interestingData)
    
    fetch('http://127.0.0.1:8000/users', {
        headers:{
          'Content-Type': 'application/json'
        },
        method: 'POST',
        body: interestingData
    }).then(res => res.json())
      .then(data => {
        console.log(data)
        const message = `User with email: ${data.email} has successfully been created`
        const type = 'success'
        appendAlert(message, type)
        // emailField.value = ""
        // passwordField.value = ""
        // window.location.replace(`http://127.0.0.1:8000/users/${data.id}`);

    }).catch(error => console.log(error))
})