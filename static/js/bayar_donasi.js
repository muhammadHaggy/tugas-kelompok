function bayar(id) {
    const message = document.getElementById('success')
    let url = '/donasi/bayar/proses/' + id

    fetch(url, {
        method: "POST",
        body: new FormData(document.querySelector('#bayar-donasi'))
    }).then(updateTerkumpul)
    document.getElementById('input-nominal').value = ''
    message.classList.replace('success-hide', 'success')
    setTimeout(hapusMessage, 3000)
    return false
}

function hapusMessage() {
    const message = document.getElementById('success')
    message.classList.replace('success', 'success-hide')
}

async function getDataDonasiId(id) {
    let url = '/donasi/get-data-donasi-id/' + id
    return fetch(url).then((result) => result.json())
}

async function updateTerkumpul() {

    const id = document.getElementById('id-donasi').innerHTML
    const data = await getDataDonasiId(id)
    document.getElementById('terkumpul').innerHTML = ""

    let donasiTerkumpul = `Donasi terkumpul: `
    let jumlah = data.jumlah
    const jumlahFormatted = rupiahIDR.format(jumlah)

    donasiTerkumpul += jumlahFormatted
    document.getElementById('terkumpul').innerHTML = donasiTerkumpul
}

let rupiahIDR = Intl.NumberFormat("id", {
    style: "currency",
    currency: "IDR",
});

const target = document.getElementById('target').innerHTML
document.getElementById('target').innerHTML = 'Target: ' + rupiahIDR.format(target)

updateTerkumpul(document.getElementById('id-donasi').innerHTML)