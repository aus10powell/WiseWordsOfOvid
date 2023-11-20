const fs = require('fs');
const csv = require('csv-parser');
const Twit = require('twit');

// Create a ConfigParser object
const config = new configparser();

// Read the INI file
config.read('config.ini');

// Twitter API keys and access tokens
const T = new Twit({
  consumer_key: config.get('TwitterAPI', 'consumer_key'),
  consumer_secret: config.get('TwitterAPI', 'consumer_secret'),
  access_token: config.get('TwitterAPI', 'access_token'),
  access_token_secret: config.get('TwitterAPI', 'access_token_secret'),
});

// Path to your CSV file
const csvFilePath = './ovid_quotes.csv';

// Function to read the CSV file and get an array of text values
function readCsvAndGetTextArray(csvFilePath) {
  return new Promise((resolve, reject) => {
    const textArray = [];

    fs.createReadStream(csvFilePath)
      .pipe(csv())
      .on('data', (row) => {
        if (row.Quote) {
          textArray.push(row.Quote);
        }
      })
      .on('end', () => {
        resolve(textArray);
      })
      .on('error', (error) => {
        reject(error);
      });
  });
}

// Function to post a random tweet
async function postRandomTweet() {
  try {
    // Read the CSV file and get an array of text values
    const textArray = await readCsvAndGetTextArray(csvFilePath);

    // Choose a random text from the array
    const randomText = textArray[Math.floor(Math.random() * textArray.length)];

    // Tweet the random text
    T.post('statuses/update', { status: randomText }, (err, data, response) => {
      if (err) {
        console.error('Error posting tweet:', err);
      } else {
        console.log('Tweet posted successfully!');
      }
    });
  } catch (error) {
    console.error('Error reading CSV file:', error);
  }
}

// Post a random tweet immediately for testing
postRandomTweet();
