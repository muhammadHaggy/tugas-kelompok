function bayar(id) {
    const message = document.getElementById('success')
    let url = '/donasi/bayar/proses/' + id

    fetch(url, {
        method: "POST",
        body: new FormData(document.querySelector('#bayar-donasi'))
    }).then()
    document.getElementById('input-nominal').value = ''
    message.classList.replace('success-hide', 'success')
    setTimeout(hapusMessage, 3000)
    return false
}

function hapusMessage() {
    const message = document.getElementById('success')
    message.classList.replace('success', 'success-hide')
}