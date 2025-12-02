const textBox = document.querySelector("#user-input");
const sendButton = document.querySelector("#send-question");

 let textValue = textBox.value;

textBox.addEventListener('keydown', function(e){
  if(e.key === 'Enter'){
    if(e.shiftKey){
      return;
    }else{
     e.preventDefault();
    console.log(textValue);
    textBox.value= "";
    }
  }
});

sendButton.addEventListener('click',function(){
    console.log(textValue);
    textBox.value="";
});