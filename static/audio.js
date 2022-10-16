let record = document.getElementById("record")
let stop = document.getElementById("stop")
let audio = document.getElementById("raudio")
let transcript = document.getElementById("transcript")

let guid = window.navigator.userAgent.replace(/\D+/g, '');

if (navigator.mediaDevices) {

  let chunks = [];
  let resMsg = "";
  let timeInt = 4000;
  let elapsed = 0;
  let totalTxt = '';
  let text = '';

  navigator.mediaDevices.getUserMedia({ audio: true })
  .then((stream) => {

    const mediaRecorder = new MediaRecorder(stream, {mimeType: 'audio/webm; codecs=opus'})

    record.onclick = () => {
      mediaRecorder.start();
      record.style.background = "red";
      record.style.color = "black";
    }

    stop.onclick = () => {
      mediaRecorder.stop();
      record.style.background = "";
      record.style.color = "";
    }

    setInterval(function(e) { 
      if(mediaRecorder.state == "recording") {
        mediaRecorder.stop() 

        mediaRecorder.ondataavailable = (e) => {
          chunks.push(e.data);

          let blob = new Blob(chunks)
          audio.src = URL.createObjectURL(blob) 

          let fd = new FormData();
          fd.append('audio_blob', blob, `${guid}.webm`)
          fd.append('browser_id', guid)

          fetch("/", {
            method: "post",
            body: fd,
            
          })
            .then((response) => response.json())
            .then((data) => {
              console.log(data)
              resMsg = data; 
            });

          text = resMsg.msg; 
          if (!text.includes('err_msg')) {
            transcript.innerHTML = `<span> ${text} </span>` 
          }
        }

        mediaRecorder.start()
        elapsed += 500;

        console.log(elapsed)
        if (elapsed >= timeInt) {
          elapsed = 0;
          chunks = [];
          //totalTxt = text;
        }
      }
    }, 500); 
  })
  .catch((err) => {
    console.error(`The following error occurred: ${err}`);
  })
}









