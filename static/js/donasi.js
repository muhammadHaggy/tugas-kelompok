getDataDonasi()

async function getDataDonasi() {
    $.getJSON("/donasi/get-data-donasi/", showDonasi);
}

async function showDonasi(json) {
    document.getElementById('card-makanan').innerHTML = ""
    document.getElementById('card-pendidikan').innerHTML = ""

    let cardMakanan = ``
    let cardPendidikan = ``
    let temp = ``
    let counterMakanan = 0
    let counterPendidikan = 0

    // dataDonasi.forEach(donasi => {
    $.each(json.data, function (index, donasi) {
        let rupiahIDR = Intl.NumberFormat("id", {
            style: "currency",
            currency: "IDR",
        });

        const target = rupiahIDR.format(`${donasi.fields.target}`)
        const terkumpul = rupiahIDR.format(`${donasi.fields.terkumpul}`)
                  
        temp = `\n
        <div class="col-12 col-md-4" style="margin-bottom: 20px;">
            <div class="card">
                <div class="picture">
                    <img src="${donasi.fields.urlFoto}">
                </div>
    
                <div class="card-content">
                    <div>
                        <h3 class="title">${donasi.fields.nama}</h3>
                        <p class="author">Digalang oleh: ${donasi.fields.penggalang}</p>
                        <p class="target">Target: ${target}</p>
                        <p class="terkumpul">Terkumpul: ${terkumpul}</p>
                    </div>

                      <div class="div-button">
                        <button class="button-card pull-right">
                            <a href="/donasi/bayar/${donasi.pk}" style="text-decoration: none; color: white;">
                                Lihat Detail
                            </a>
                        </button>
                      </div>

                </div>
            </div>
        </div>
        `

        if (donasi.fields.tipe == "Makanan") {
            if (counterMakanan%3 == 0) {
                cardMakanan += `\n<div class="row">`
            }

            cardMakanan += temp
            counterMakanan++

            if (counterMakanan%3 == 0) {
                cardMakanan += `\n</div>`
            }
        }
        
        if (donasi.fields.tipe == "Pendidikan") {
            if (counterPendidikan%3 == 0) {
                cardPendidikan += `\n<div class="row">`
            }

            cardPendidikan += temp
            counterPendidikan++

            if (counterPendidikan%3 == 0) {
                cardPendidikan += `\n</div>`
            }
        }    
    });

    document.getElementById('card-makanan').innerHTML = cardMakanan
    document.getElementById('card-pendidikan').innerHTML = cardPendidikan
}
