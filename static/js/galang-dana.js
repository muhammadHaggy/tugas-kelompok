async function getUser() {
    return fetch("/galang-dana/get-user-count/").then((res) => res.json())
}
async function showUserCount() {
    const user = await getUser()
    let userCount = user.length

    document.getElementById("donatur-count").innerHTML = userCount
}
showUserCount()
setInterval(showUserCount, 1000)