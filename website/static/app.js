
 //start of new trial

  // Get the select element and button
const songSelect = document.getElementById('song-select');
const playButton = document.getElementById('play-button');

// Create an object to store the song URLs
const songUrls = {
  song1: 'sound/sound 1.mp3',
  song2: 'sound/sound 2.mp3',
  song3: 'sound/sound 3.mp3',
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