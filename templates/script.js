document.getElementById("userForm").addEventListener("submit", function(e) {

    e.preventDefault();

    const name = document.getElementById("name").value;
    const age = document.getElementById("age").value;

    fetch("/save", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            name: name,
            age: age
        })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("message").innerText = data.message;
    });

});