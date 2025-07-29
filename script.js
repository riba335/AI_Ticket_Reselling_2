
fetch('https://ai-ticket-reselling-2.onrender.com/events')
    .then(response => response.json())
    .then(data => {
        const tableBody = document.querySelector("#eventsTable tbody");
        data.forEach(event => {
            const row = document.createElement("tr");
            row.innerHTML = `
                <td>${event.name}</td>
                <td>${event.date}</td>
                <td>${event.location}</td>
                <td>${event.price} €</td>
                <td>${event.profit} €</td>
                <td>${event.score}</td>
            `;
            tableBody.appendChild(row);
        });
    })
    .catch(error => {
        console.error("Chyba pri načítaní údajov:", error);
    });
