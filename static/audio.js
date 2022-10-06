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

    setInterval(function(e) {
      const blob = new Blob(chunks, { 'type' : 'audio/ogg; codecs=opus' });
      chunks = [];
      const audioURL = URL.createObjectURL(blob);
      audio.src = audioURL;
      console.log("recorder paused");
      audio.play();
    }, 3000)

    mediaRecorder.onstop = (e) => {
      console.log("data available after MediaRecorder.stop() called.");
    }

    mediaRecorder.ondataavailable = (e) => {
      chunks.push(e.data);
    }
  })
  .catch((err) => {
    console.error(`The following error occurred: ${err}`);
  })
}



