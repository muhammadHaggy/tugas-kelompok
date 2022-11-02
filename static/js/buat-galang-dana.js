function createGalangDana() {
    fetch('/galang-dana/add/', {
        method: "POST",
        body: new FormData(document.querySelector("#formGalangDana"))
    }).then(res => {
        if (res.status == 201) {
            $("#modalGalangDanaDibuat").modal("show")
        } else {
            $("#modalFormBelumTerisi").modal("show")
        }
    })
    return false
}

document.getElementById("buatGalangDana").onclick = createGalangDana