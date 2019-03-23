"use strict"

const URL = "https://inventory.djoamersfoort.nl"
const API = {
    get: {
        items() {
            return `${URL}/api/v1/items`
        },
        itemById(id) {
            return `${URL}/api/v1/item/${id}`
        },
        itemSearch(keyword) {
            return `${URL}/api/v1/items/search/${keyword}`
        },
        location(id) {
            return `${URL}/api/v1/location/${id}`
        },
        locationPhoto(id) {
            return `${URL}/api/v1/location/${id}/photo`
        }
    }
}

function renderList(items) {
    const list = document.querySelector("#results tbody")
    list.innerHTML = ""
    for (let item of items) {
        const record = document.createElement("tr")
        record.innerHTML = `
        <td>${item.name}</td>
        <td>${item.description}</td>
        <td>${item.url}</td>
        <td>${item.location}</td>
        <td>${item.properties}</td>`
        // record.setAttribute("data-location-id", item.location_id)
        record.onclick = () => {
            showLocation(item.location_id)
        }
        list.appendChild(record)
    }
}

function renderLocation(location) {
    const card = document.getElementById("location")
    card.innerHTML = `
    <div class="card-image">
        <img src="data:image/png;base64,${location.photo}">
        <span class="card-title">${location.name}</span>
    </div>
    <div class="card-content">
        <p>${location.description}</p>
    </div>`
}

function search() {
    const query = searchField.value
    if (query === "") {
        renderList([])
        return
    }
    if (query.length < 3) return;
    fetch(API.get.itemSearch(query))
        .then(response => response.json())
        .then(result => {
            if (result.result === "ok") {
                renderList(result.items)
            } else {
                showOopsieWoopsie()
            }
        })
        .catch(err => {
            showOopsieWoopsie()
        })
}

function showLocation(id) {
    fetch(API.get.location(id))
        .then(response => response.json())
        .then(result => {
            if (result.result === "ok") {
                renderLocation(result.location)
            } else {
                showOopsieWoopsie()
            }
        })
        .catch(err => {
            showOopsieWoopsie()
        })
}

function showOopsieWoopsie() {
    const modal = document.getElementById("oopsie-woopsie")
    const instance = M.Modal.getInstance(modal)
    instance.open()
}

// Executing
const searchField = document.getElementById("search")
const searchButton = document.getElementById("search-btn")

searchField.onkeyup = search
searchButton.onclick = search

const modals = document.querySelectorAll(".modal")
const modalInstances =  M.Modal.init(modals)
