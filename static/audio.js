let record = document.getElementById("record")
let stop = document.getElementById("stop")
let audio = document.getElementById("raudio")

let fin = document.getElementById("rupload");

let fd = new FormData();

let upload = (data) => {
  fetch('/', {
    method: 'POST',
    body: data
  })
};

let onSelectFile = () => {
  fd.append('audiof', fin.files[fin.files.length-1])
  upload(fd);
}
fin.addEventListener('change', onSelectFile, false);

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

          fetch("/", {
            method: "post",
            body: blob
          });
        }

        mediaRecorder.start()
      }
    }, 3000);
  })
  .catch((err) => {
    console.error(`The following error occurred: ${err}`);
  })
}






