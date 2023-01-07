const audioTag = document.getElementById("player");
const transcriptDiv = document.getElementById("transcript");
const audioPlayer = document.querySelector(".audio-player");

let playCtx = customAudioPlayer(audioTag);

let guid = window.navigator.userAgent.replace(/\D+/g, '');

let text = '';
let allChunks = [];
let allTexts = [];
let stopped = 0;

function pauseAudio(audio, btn) {	
	btn.classList.remove("pause");
	btn.classList.add("play");
	audio.pause();
}

function customAudioPlayer(audio) {
	const playBtn = audioPlayer.querySelector(".controls .toggle-play");
	const timeline = audioPlayer.querySelector(".timeline");
	const progressBar = audioPlayer.querySelector(".progress");
	const volumeBtn = audioPlayer.querySelector(".volume-button");
	const volumeEl = audioPlayer.querySelector(".volume-container .volume"); 

	timeline.addEventListener("click", e => {
		const timelineWidth = window.getComputedStyle(timeline).width;
		const timeToSeek = e.offsetX / parseInt(timelineWidth) * audio.duration;
		audio.currentTime = timeToSeek;
	}, false);

	playBtn.addEventListener(
		"click",
		() => {
			if (audio.paused) {
				playBtn.classList.remove("play");
				playBtn.classList.add("pause");
				audio.play();
			} else {
				pauseAudio(audio, playBtn);
			}
		},
		false
	);

	volumeBtn.addEventListener("click", () => {	
		audio.muted = !audio.muted;
		if (audio.muted) {
			volumeEl.classList.remove("fa-volume-up");
			volumeEl.classList.add("fa-volume-off");
		} else {
			volumeEl.classList.add("fa-volume-up");
			volumeEl.classList.remove("fa-volume-off");
		}
	});

	/*setInterval(() => {
		progressBar.style.width = audio.currentTime / audio.duration * 100 + "%";	
		//if (audio.currentTime >= audio.duration) {
			//pauseAudio(audio, playBtn);
		//}
	}, 500);*/

	function getTimeCodeFromNum(num) {
		let seconds = parseInt(num);
		let minutes = parseInt(seconds / 60);
		seconds -= minutes * 60;
		const hours = parseInt(minutes / 60);
		minutes -= hours * 60;

		if (hours === 0) return `${minutes}:${String(seconds % 60).padStart(2, 0)}`;
		return `${String(hours).padStart(2, 0)}:${minutes}:${String(
			seconds % 60
		).padStart(2, 0)}`;
	}

	return playBtn;
}

//function liveAudioSpeechRecognition() {
let recordBtn = document.getElementById("record");
let stopBtn = document.getElementById("stop");

if (navigator.mediaDevices) {
	navigator.mediaDevices.getUserMedia({audio: true})
	.then((stream) => {
		const mediaRecorder = new MediaRecorder(stream, {
			mimeType: 'audio/webm; codecs=opus'
		})

		recordBtn.onclick = () => {
			allChunks = [];
			allTexts = [];
			audioTag.src = "";
			transcriptDiv.innerHTML = `<span>Re-annotating..</span>`;
			console.log('start recording');
			stopped = 0;
			mediaRecorder.start();
			recordBtn.style.background = "red";
			record.style.color = "white";
		}

		stopBtn.onclick = (e) => {
			console.log('stop recording');
			stopped = 1;
			mediaRecorder.stop();
			record.style.background = "";
			record.style.color = "black";	
		}

		setInterval(function() { 
			if(mediaRecorder.state == "recording") {
				mediaRecorder.stop();	
			}	
		}, 2000);

		mediaRecorder.ondataavailable = (e) => {
			console.log('ondataavailable1 fired!');
			allChunks.push(e.data);
			if (!stopped) {
				let fd = new FormData();
				fd.append('audio_blob', new Blob([e.data]), `${guid}.webm`)
				fd.append('browser_id', guid)

				console.log('resuming media and sending audio request..');

				mediaRecorder.start();
				fetch("/", {
					method: "post",
					body: fd,  
				})
				.then((response) => response.json())
				.then((data) => {
					text = data.msg;
					if (!text.includes('err_msg')) {
						allTexts.push(text);
						transcriptDiv.innerHTML = `<span>${allTexts.join(' ')} </span>` 
					} 
				}); 
			} 	
		}
	})
	.catch((err) => {
		console.error(`The following error occurred: ${err}`);
	})
}
//}

//liveAudioSpeechRecognition();






