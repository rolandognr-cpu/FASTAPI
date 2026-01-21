console.log('Hello from FastAPI!')

const alertPlaceholder = document.getElementById('liveAlertPlaceholder')
const formEl = document.querySelector('.form')
const emailField = document.getElementById('exampleInputEmail1')
const passwordField = document.getElementById('exampleInputPassword1')


const appendAlert = (message, type) => {
  const wrapper = document.createElement('div')
  wrapper.innerHTML = [
    `<div class="alert alert-${type} alert-dismissible" role="alert">`,
    `   <div>${message}</div>`,
    '   <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>',
    '</div>'
  ].join('')

  alertPlaceholder.append(wrapper)
}

formEl.addEventListener('submit', event => {
    event.preventDefault()
    const formData = new FormData(formEl)
    interestingData = {'email': formData.get('email'), 'password': formData.get('password')}
    
    fetch('http://127.0.0.1:8000/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(interestingData)
    }).then(res => res.json())
      .then(data => {
        console.log(data)
        const message = `User with email: ${data.email} has successfully been created`
        const type = 'success'
        appendAlert(message, type)

        emailField.value = ""
        passwordField.value = ""

    }).catch(error => console.log(error))
})