let record = document.getElementById("record")
let stop = document.getElementById("stop")
let audio = document.getElementById("raudio")

if (navigator.mediaDevices) {
	console.log('getUserMedia supported.');

  const constraints = { audio: true };
  let chunks = [];

  navigator.mediaDevices.getUserMedia(constraints)
  .then((stream) => {

    const mediaRecorder = new MediaRecorder(stream);

    record.onclick = () => {
      mediaRecorder.start();
      console.log(mediaRecorder.state);
      console.log("recorder started");
      record.style.background = "red";
      record.style.color = "black";
    }

    stop.onclick = () => {
      mediaRecorder.stop();
      console.log(mediaRecorder.state);
      console.log("recorder stopped");
      record.style.background = "";
      record.style.color = "";
    }

    function sendAudio(url) {
      return fetch('/audio', {
        Method:'POST',
        Body: {'url': url} 
      })
    }

    async function recordMedia(e) { 
      if(mediaRecorder.state == "recording") {
        mediaRecorder.stop()
        
        mediaRecorder.onstop = (e) => {
          console.log(chunks.length)
          console.log("data available after MediaRecorder.stop() called.");
        }

        mediaRecorder.ondataavailable = (e) => {
          console.log('pushing to chunks')
          chunks.push(e.data);

          console.log(chunks.length)
          audio.src = URL.createObjectURL(
            new Blob(chunks, {'type':'audio/ogg; codecs=opus'})
          );
          //audio.play();
          let success = await sendAudio(audio.src)
        }

        mediaRecorder.start()
      }
    }

    setInterval(recordMedia, 3000);
  })
  .catch((err) => {
    console.error(`The following error occurred: ${err}`);
  })
}






