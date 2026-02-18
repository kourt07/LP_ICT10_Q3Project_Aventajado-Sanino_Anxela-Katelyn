from js import document

players = ["Dennings","Hall","HarlowDe", "Luna", "De Leon", "Evangelista",
"Tolentino","Maddox","Ligaya","Javier","Roquez","Cruz","Sevilla",
"Ngee","Orto","Garcia","Ramos","Serville","Sta. Maria","Setenta",
"Tinio","Pascual","Tobe","Quezon"]

container = document.getElementById("player-container")

for x in players:
    if x == "Quezon":
        break

    item = document.createElement("div")
    item.textContent = x
    container.appendChild(item)