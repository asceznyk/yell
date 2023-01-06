let record = document.getElementById("record")
let stop = document.getElementById("stop")
let transcript = document.getElementById("transcript")

let guid = window.navigator.userAgent.replace(/\D+/g, '');

let chunks = [];
let allTexts = [];
let text = '';

if (navigator.mediaDevices) {
  navigator.mediaDevices.getUserMedia({audio: true})
  .then((stream) => {
    const mediaRecorder = new MediaRecorder(stream, {mimeType: 'audio/webm; codecs=opus'})

    record.onclick = () => {
      console.log('start recording');
      mediaRecorder.start();
      record.style.background = "red";
      record.style.color = "black";
    }

    stop.onclick = () => {
      console.log('stop recording');
      mediaRecorder.stop();
      record.style.background = "";
      record.style.color = "";
    }

    mediaRecorder.onstop = (e) => {
      e.preventDefault();
    }

    setInterval(function() { 
      if(mediaRecorder.state == "recording") {
        mediaRecorder.stop();

        mediaRecorder.ondataavailable = (e) => { 
          chunks.push(e.data); 
          let fd = new FormData();
          fd.append('audio_blob', new Blob(chunks), `${guid}.webm`)
          fd.append('browser_id', guid)
          mediaRecorder.start();

          console.log('sending audio request..');
          fetch("/", {
            method: "post",
            body: fd,  
          })
          .then((response) => response.json())
          .then((data) => {
            text = data.msg;
            if (!text.includes('err_msg')) {
              allTexts.push(text);
              transcript.innerHTML = `<span>${allTexts.join(' ')} </span>` 
            } 
            chunks = [];
          });  
        }
      }
    }, 4000); 
  })
  .catch((err) => {
    console.error(`The following error occurred: ${err}`);
  })
}









