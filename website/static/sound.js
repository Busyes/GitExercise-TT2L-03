
 //start of new trial

  // Get the select element and button
const songSelect = document.getElementById('song-select');
const playButton = document.getElementById('play-button');
const stopSongButton = document.getElementById('stop-song-button')

// Create an object to store the song URLs
const songUrls = {
  song1: 'static/sound/sound 1.mp3',
  song2: 'static/sound/sound 2.mp3',
  song3: 'static/sound/sound 3.mp3',

  // Add more songs to the object
};

// Add an event listener to the button
playButton.addEventListener('click', () => {
  // Get the selected song value
  const selectedSong = songSelect.value;
  // Play the selected song
  if (selectedSong) {
    const audio = new Audio(songUrls[selectedSong]);
    audio.play();
  } else {
    alert('Please select a song!');
  }
});

// Stop song button
stopSongButton.addEventListener('click', () => {
  // Stop the current audio
  audio.stop();
});

const audioFiles = [
  { src: 'static/sound/sound 1.mp3', element: document.getElementById('audio1') },
  { src: 'static/sound/sound 2.mp3', element: document.getElementById('audio2') },
  { src: 'static/sound/sound 3.mp3', element: document.getElementById('audio3') }
];

// Play the first audio file
audioFiles[0].element.play();

// Pause the second audio file
audioFiles[1].element.pause();

// Stop the third audio file
audioFiles[2].element.stop();