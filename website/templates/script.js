function storeUserSession(sessionData) {
    fetch('/store_session', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(sessionData),
    })
    .then((response) => response.json())
    .then((data) => {
      console.log('Success:', data);
    })
    .catch((error) => {
      console.error('Error:', error);
    });
  }
  
  // Example usage:
  const sessionData = {
    userId: 123,
    sessionToken: 'abcdefg12345',
  };
  storeUserSession(sessionData);