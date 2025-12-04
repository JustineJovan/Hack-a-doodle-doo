const textBox = document.querySelector("#user-input");
const sendButton = document.querySelector("#send-question");

const mUser = document.querySelector(".messages");
const mBot = document.querySelector(".messages");

let userTurn = true;
let botTurn = false;

async function sendMessage(textValue){
  const DnewMUser = document.createElement("div");
    DnewMUser.classList.add("message-user");

    const newMUser = document.createElement("p");
    newMUser.textContent = textValue;

    DnewMUser.appendChild(newMUser);
    mUser.appendChild(DnewMUser);

    try{
      const response = await fetch("http://127.0.0.1:5000/ask",{method:"POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({question: textValue})
      });
      const data = await response.json();

      const DnewMBot = document.createElement("div");
      DnewMBot.classList.add("message-bot");

      const newMBot = document.createElement("p");
      newMBot.textContent = data.answer;

      DnewMBot.appendChild(newMBot);
      mBot.appendChild(DnewMBot);
    } catch(err){
      console.error(err);
    }
}

textBox.addEventListener('keydown', function(e){
  if(e.key === 'Enter' && userTurn == true && botTurn == false){
    if(e.shiftKey || textBox.value.trim() == ""){
      return;
    }
    else{
    let textValue = textBox.value.trim();
    e.preventDefault();
    console.log(textValue);
    userTurn = false;
    botTurn = true;
    textBox.value="";

    sendMessage(textValue).then(() => {
      userTurn = true;
      botTurn = false;
    });
    }
  }
});

sendButton.addEventListener('click', async function(){
  if(textBox.value == "" && userTurn == true && botTurn == false){
    return;
  }else if(userTurn == true && botTurn == false){
  let textValue = textBox.value;
  console.log(textValue);
  textBox.value="";

    const DnewMUser = document.createElement("div");
    DnewMUser.classList.add("message-user");

    const newMUser = document.createElement("p");
    newMUser.textContent = textValue;

    DnewMUser.appendChild(newMUser);
    mUser.appendChild(DnewMUser);

    userTurn = false;
    botTurn = true;
    
    const response = await fetch('http://127.0.0.1:5000/ask', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({question: textValue})
    });
    const data = await response.json();
    const botAnswer = data.answer;

    // Add bot message
    const DnewMBot = document.createElement("div");
    DnewMBot.classList.add("message-bot");
    const newMBot = document.createElement("p");
    newMBot.textContent = botAnswer;
    DnewMBot.appendChild(newMBot);
    mBot.appendChild(DnewMBot);

    userTurn = true;
    botTurn = false;
  }
});