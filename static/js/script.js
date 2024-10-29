/**
 * Variables
 */

const roomName = Math.random().toString(36).slice(2, 12)
const url = `ws://127.0.0.1:8000/ws/${roomName}/`;
const socket = new WebSocket(url);
const button = document.getElementById('button-input');
const chatbot = document.getElementById('chatbot');
const userInput = document.getElementById('text-input');

/**
 * Functions
 */

function scrollToBottom() {
  chatbot.scrollTop = chatbot.scrollHeight;
}

function sendMessage() {
  const userHTML = 
    `<hr><p class="user-text">User: <span>${userInput.value}</span></p>`;
  chatbot.innerHTML += userHTML;

  socket.send(
    JSON.stringify({
      'type': 'message',
      'message': userInput.value
    })
  );
  userInput.value = "";
  scrollToBottom();
}

/**
 * Event Listeners
 */

socket.onopen = function(e) {
  console.log('Connection Established');
}

socket.onclose = function(e) {
  console.log('Connection Lost');
}

socket.onmessage = function(e) {
  data = JSON.parse(e.data);
  console.log('DATA:', data);
  const botHTML = 
    `<p class="bot-text">Bot: ${data.title}<br><br><span>${data.message}</span></p>`;

  chatbot.innerHTML += botHTML;
  scrollToBottom();
}


button.onclick = function(e) {
  e.preventDefault();

  sendMessage();
}


userInput.onkeyup = function(e) {
  if (e.keyCode === 13) {
    sendMessage();
  }
}
