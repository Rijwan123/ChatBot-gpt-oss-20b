const messageInput = document.getElementById("message");
const chatBox = document.getElementById("chatBox");
const sendButton = document.getElementById("sendButton");


// Send message when Enter is pressed
messageInput.addEventListener("keydown", function (event) {

    if (event.key === "Enter") {
        event.preventDefault();
        sendMessage();
    }

});


async function sendMessage() {

    const message = messageInput.value.trim();

    if (!message) {
        return;
    }


    // Remove welcome screen after first message
    const welcome = document.querySelector(".welcome");

    if (welcome) {
        welcome.remove();
    }


    // Show user message
    addMessage(message, "user");


    // Clear input
    messageInput.value = "";


    // Disable controls while waiting
    sendButton.disabled = true;
    messageInput.disabled = true;


    // Show loading animation
    const loadingId = showLoading();


    try {

        const response = await fetch(
            "https://chatbot1-rose-nine.vercel.app/chat",
            {
                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify({
                    message: message
                })
            }
        );


        console.log("Status:", response.status);


        const data = await response.json();

        console.log("Backend response:", data);


        if (!response.ok) {

            throw new Error(
                data.detail || "Backend returned an error."
            );
        }


        // Remove loading animation
        removeLoading(loadingId);


        // Show AI response
        addMessage(
            data.response,
            "ai"
        );

    }

    catch (error) {

        removeLoading(loadingId);

        console.error("Chat Error:", error);

        addMessage(
            "Error: " + error.message,
            "ai"
        );
    }


    // Enable controls again
    sendButton.disabled = false;
    messageInput.disabled = false;

    messageInput.focus();
}



function addMessage(text, sender) {

    const row = document.createElement("div");
    const messageDiv = document.createElement("div");
    const label = document.createElement("div");
    const content = document.createElement("div");


    if (sender === "user") {

        row.className = "message-row user-row";
        messageDiv.className = "message user-message";
        label.textContent = "You";

    }

    else {

        row.className = "message-row ai-row";
        messageDiv.className = "message ai-message";
        label.textContent = "AI Assistant";
    }


    label.className = "message-label";

    content.textContent = text;


    messageDiv.appendChild(label);
    messageDiv.appendChild(content);

    row.appendChild(messageDiv);

    chatBox.appendChild(row);


    scrollToBottom();
}



function showLoading() {

    const id = "loading-" + Date.now();


    const row = document.createElement("div");

    row.className = "message-row ai-row";
    row.id = id;


    row.innerHTML = `
        <div class="message ai-message">

            <div class="message-label">
                AI Assistant
            </div>

            <div class="loading">
                <span></span>
                <span></span>
                <span></span>
            </div>

        </div>
    `;


    chatBox.appendChild(row);

    scrollToBottom();

    return id;
}



function removeLoading(id) {

    const loadingElement =
        document.getElementById(id);

    if (loadingElement) {
        loadingElement.remove();
    }
}



function scrollToBottom() {

    chatBox.scrollTop =
        chatBox.scrollHeight;
}