async function sendMessage() {
    const userInput = document.getElementById("userInput").value;
    const response = await fetch("/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: userInput })
    });
    const data = await response.json();
    document.getElementById("chat").innerHTML += `<p><b>You:</b> ${userInput}</p>`;
    document.getElementById("chat").innerHTML += `<p><b>AI:</b> ${data.response}</p>`;
    document.getElementById("userInput").value = "";
}