const gpt_url = "http://127.0.0.1:8000/chat_bot/gpt/"

function createChatThreadElement(name){
    const li = document.createElement('li');
    li.classList.add("nav-item");
    li.classList.add("mx-3");
    li.classList.add("text-muted");
    li.classList.add("side-nav-bar");
    
    const a = document.createElement("a");
    a.classList.add("nav-link");
    a.classList.add("active");
    a.href = "#";
    a.innerText = name;

    li.appendChild(a);

    return li;
}

function createChatElementMessage(message, sender) {
    var userIconElement = document.createElement("img");
    userIconElement.setAttribute("src", `media/icon/${sender}.png`);
    userIconElement.setAttribute("width", "30");
    userIconElement.setAttribute("height", "30");

    var userNameElement = document.createElement("div");
    userNameElement.classList.add("user-name");
    userNameElement.innerText = sender

    var userPartElement = document.createElement("div");
    userPartElement.className = "chat-user-part";
    userPartElement.appendChild(userIconElement);
    userPartElement.appendChild(userNameElement);

    const messageElement = document.createElement('div');
    messageElement.className = "chat-message"
    messageElement.innerText = message;

    var displayElement = document.createElement("div");
    displayElement.className = "chat-element"
    displayElement.appendChild(userPartElement);
    displayElement.appendChild(messageElement);

    return displayElement;
}
function createChatElement(sender) {
    var userIconElement = document.createElement("img");
    userIconElement.setAttribute("src", `media/icon/${sender}.png`);
    userIconElement.setAttribute("width", "30");
    userIconElement.setAttribute("height", "30");

    var userNameElement = document.createElement("div");
    userNameElement.classList.add("user-name");
    userNameElement.innerText = sender

    var userPartElement = document.createElement("div");
    userPartElement.className = "chat-user-part";
    userPartElement.appendChild(userIconElement);
    userPartElement.appendChild(userNameElement);

    const messageElement = document.createElement('div');
    messageElement.className = "chat-message"

    var displayElement = document.createElement("div");
    displayElement.className = "chat-element"
    displayElement.appendChild(userPartElement);
    displayElement.appendChild(messageElement);

    return displayElement;
}

// async function sendMessage(message, thread_id) {  
//     var fetch_setting = 
//     { 
//         method: "POST", 
//         headers: { "Content-Type": "application/json", "X-CSRFToken": getCookie('csrftoken')}, 
//         body : JSON.stringify({ message: message })
//     }
//     const url = `http://127.0.0.1:8000/chat_bot/gpt/${thread_id}/`
//     return await fetch(url, fetch_setting)
//     // .then(response => response.json())
//     .catch(error => console.error('Error:', error));
// }

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}