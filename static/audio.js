let record = document.getElementById("record")
let stop = document.getElementById("stop")
let audio = document.getElementById("raudio")

if (navigator.mediaDevices) {

  const constraints = { audio: true };
  let chunks = [];

  navigator.mediaDevices.getUserMedia(constraints)
  .then((stream) => {

    const mediaRecorder = new MediaRecorder(stream);

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

          let blob = new Blob(chunks, {'type':'audio/wav; codecs=opus'})
          audio.src = URL.createObjectURL(blob)

          let xhr = new XMLHttpRequest()
          xhr.onload=function(e) {
          if(this.readyState === 4) {
              console.log("Server returned: ",e.target.responseText);
            }
          };
          let audioData = new FormData()
          audioData.append('audio', blob, 'sample.wav')
          xhr.open("POST", "/", true)
          xhr.send(audioData)

        }

        mediaRecorder.start()
      }
    }, 3000);
  })
  .catch((err) => {
    console.error(`The following error occurred: ${err}`);
  })
}






