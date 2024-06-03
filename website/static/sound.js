// Get the select element and button
const songSelect = document.getElementById('song-select');
const playButton = document.getElementById('play-button');
const stopSongButton = document.getElementById('stop-song-button');

// Create an object to store the song URLs
const songUrls = {
  song1: 'static/sound/sound 1.mp3',
  song2: 'static/sound/sound 2.mp3',
  song3: 'static/sound/sound 3.mp3',
};

let currentAudio; // Declare the currentAudio variable outside the event listener

// Add an event listener to the button
playButton.addEventListener('click', () => {
  // Get the selected song value
  const selectedSong = songSelect.value;
  
  // Check if a song is selected
  if (selectedSong) {
    // Stop the current audio if it exists
    if (currentAudio) {
      currentAudio.pause();
      currentAudio.currentTime = 0;
    }
    
    // Play the selected song
    currentAudio = new Audio(songUrls[selectedSong]);
    currentAudio.play();
  } else {
    alert('Please select a song!');
  }
});

// Stop song button
stopSongButton.addEventListener('click', () => {
  // Stop the current audio if it exists
  if (currentAudio) {
    currentAudio.pause();
    currentAudio.currentTime = 0;
  }
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