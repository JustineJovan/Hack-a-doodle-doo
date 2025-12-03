const textBox = document.querySelector("#user-input");
const sendButton = document.querySelector("#send-question");

const mUser = document.querySelector(".message-user");
const mBot = document.querySelector(".message-bot");

let userTurn = true;
let botTurn = false;

textBox.addEventListener('keydown', function(e){
  if(e.key === 'Enter' && userTurn == true && botTurn == false){
    if(e.shiftKey || textBox.value == ""){
      return;
    }
    else{
    let textValue = textBox.value;
    e.preventDefault();
    console.log(textValue);

    const DnewMUser = document.createElement("div");
    DnewMUser.classList.add("message-user");

    const newMUser = document.createElement("p");
    newMUser.textContent = textValue;

    DnewMUser.appendChild(newMUser);
    mUser.appendChild(DnewMUser);
    userTurn = false;
    botTurn = true;
    textBox.value="";
    }
  }

  if(e.key === 'Control' && userTurn == false && botTurn == true){
    let textValue = textBox.value;
    e.preventDefault();
    console.log(textValue);

    const DnewMBot = document.createElement("div");
    DnewMBot.classList.add("message-user");

    const newMBot = document.createElement("p");
    newMBot.textContent = textValue;

    DnewMBot.appendChild(newMBot);
    mBot.appendChild(DnewMBot);
    userTurn = true;
    botTurn = false;
    textBox.value="";
    }
});

sendButton.addEventListener('click',function(e){
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
    
    textBox.value="";
  }
});


