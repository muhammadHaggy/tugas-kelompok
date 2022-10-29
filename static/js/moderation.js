const formatter = new Intl.NumberFormat('id', {
    style: 'currency',
    currency: 'IDR',
})
async function showDonasi(json) {
    console.log(json)
    document.getElementById('card-makanan').innerHTML = "";
    document.getElementById('card-pendidikan').innerHTML = "";

    let cardMakanan = ``;
    let cardPendidikan = ``;
    let temp = ``;
    let counterMakanan = 0;
    let counterPendidikan = 0;

    $.each(json.data, function (index, donasi) {
        fields = donasi.fields
        console.log(fields.nama)
        temp = `\n
    <div class="col-12 col-md-4" style="margin-bottom: 20px;">
        <div class="card">
            <div class="picture">
                <img src="${fields.urlFoto}" height=80px>
            </div>

            <div class="text-muted text-center mb-3">
                Digalang oleh ${fields.penggalang}
            </div>

            <div class="card-content">
                <div class="text-center mb-5">
                    <h3 class="card-title mb-3">${donasi.fields.nama}</h3>
                    <p class="card-text">${donasi.fields.deskripsi}</p>
                </div>
                <div class="btn-group mb-4" role="group">
                    <button class="button-card approve" onclick="approve(${donasi.pk});">
                        Approve
                    </button>
                    <button class="button-card reject" style="background-color: red;" onclick="reject(${donasi.pk});">
                        Reject
                    </button>
                </div>
            </div>
            <div class="card-footer text-muted">
                Target: ${formatter.format(fields.target)}
            </div>
        </div>
    </div>
    `

        if (donasi.fields.tipe == "Makanan") {
            if (counterMakanan % 3 == 0) {
                cardMakanan += `\n<div class="row">`;
            }

            cardMakanan += temp;
            counterMakanan++;

            if (counterMakanan % 3 == 0) {
                cardMakanan += `\n</div>`;
            }
        }

        if (donasi.fields.tipe == "Pendidikan") {
            if (counterPendidikan % 3 == 0) {
                cardPendidikan += `\n<div class="row">`;
            }

            cardPendidikan += temp;
            counterPendidikan++;

            if (counterPendidikan % 3 == 0) {
                cardPendidikan += `\n</div>`;
            }
        }
    });
    if (cardMakanan == '') {
        cardMakanan = `
        <div class="text-center">
            <h5>No Queue</h5>
        </div>
        `
    }
    if (cardPendidikan == '') {
        cardPendidikan = `
        <div class="text-center">
            <h5>No Queue</h5>
        </div>
        `
    }

    document.getElementById('card-makanan').innerHTML = cardMakanan;
    document.getElementById('card-pendidikan').innerHTML = cardPendidikan;
}

function approve(pk) {
    $.get({
        url: `approve/${pk}`,
        success: function (data) {
            updateDonasi();
        },
    });
}
function reject(pk) {
    $.get({
        url: `reject/${pk}`,
        success: function (data) {
            updateDonasi();
        },
    });
}
$(document).ready(function () {
    updateDonasi();
})