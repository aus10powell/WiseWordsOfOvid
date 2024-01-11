# WiseWordsOfOvid

## Dataset
| Quote                                          | Quote in Latin                               | Work                       |
|------------------------------------------------|-----------------------------------------------|----------------------------|
| Love is a thing full of anxious fears.          | Res est solliciti plena timoris amor.         | Heroides (The Heroines) I |
| Now are fields of corn where Troy once stood.   | Iam seges est ubi Troia fuit.                 | Heroides (The Heroines) I |
| We're slow to believe what wounds us.           | Tarde quae credita laedunt credimus.          | Heroides (The Heroines) II|



Creating a Twitter bot that tweets daily quotes from the Latin author Ovid involves several steps. Below is a plan outlining the key tasks to achieve this:

## Steps
~~### 1. Set Up Twitter Developer Account:~~

~~1.1 **Create a Twitter Developer Account:**~~
   ~~- Go to the [Twitter Developer](https://developer.twitter.com/) website and create an account.~~

~~1.2 **Create a Twitter App:**~~
   ~~- Create a new Twitter App in the Developer Dashboard. This will provide you with API keys and tokens necessary for accessing the Twitter API.~~

~~### 2. Choose a Programming Language:~~

~~2.1 **Select a Language:**~~
   ~~- Choose a programming language to build the bot. Popular choices include Python, Node.js, or Ruby.~~

~~### 3. Access Ovid's Quotes:~~

~~3.1 **Find a Source of Quotes:**~~
   ~~- Locate a reliable source of Ovid's quotes in Latin and English translation. This could be a website, a database, or a collection of Ovid's works.~~

~~### 4. Set Up a Code Repository:~~

~~4.1 **Create a GitHub Repository:**~~
   ~~- Create a GitHub repository to store your bot's code. This allows for version control and collaboration.~~

### 5. Code the Bot:

SEE: [100 days of code twtter bot](https://github.com/freeCodeCamp/100DaysOfCode-twitter-bot)

~~5.1 **Install Necessary Libraries:**~~
   ~~- If using Python, install libraries like Tweepy for Twitter API access.~~

5.2 **Create a Script:**
   ~~- Write a script that fetches a daily quote from the Ovid source, formats it, and posts it to Twitter using the Twitter API.~~

### 6. Schedule Daily Tweets:

6.1 **Use a Scheduler:**
   ~~- Employ a scheduler (e.g., cron jobs for Unix-based systems or Task Scheduler for Windows) to run your script daily and post a new quote.~~

### 7. Add Variety and Engagement:
7.0 **Add to Quote Bank**
   * **Approaches:**
      * Sentences similarity
      * Novel paper approach


7.2 **Randomize Quotes:**
   - Consider randomizing the selection of quotes to add variety. Using a formual from quote_retrieval.ipynb randomly select a post based on rolling window.

~~7.3 **Investigate Different Retrieval Capabilities**~~
   - Investigate to see if possible use for retreiving useful quotes.
   ~~- https://github.com/tigerlab-ai/tiger~~
   ~~- https://www.anyscale.com/blog/a-comprehensive-guide-for-building-rag-based-llm-applications-part-1~~

7.4 **Interactivity:**
   - Allow users to interact with the bot, perhaps by responding to tweets with specific keywords or by providing feedback.
   - Twitterbot that retweets, favorites and follows: https://www.digitalocean.com/community/tutorials/how-to-create-a-twitterbot-with-python-3-and-the-tweepy-library

7.5 **Reply**
* Use OpenAI to generate a "cute remark"
* Create a Q/A model to select an appropriate quote
   * Dual-encoder approach since I'm essentially doing this anyway for the quote retrieval.
   * Conditional Response: Intent classification then determine if responding with a quote/joke/general comment
      * See: [Contextual Chatbots with Tensorflow](https://chatbotsmagazine.com/contextual-chat-bots-with-tensorflow-4391749d0077)

### 8. Test and Debug:

8.1 **Test in a Sandbox:**
   - Use a test Twitter account or a sandbox environment to avoid accidental posting on your main account.

8.2 **Debugging:**
   - Ensure error handling in your script and debug any issues that arise during testing.

### 9. Deploy:

9.1 **Deploy to Hosting Service:**
   ~- If necessary, deploy your bot to a hosting service to ensure it runs consistently.~

### 10. Monitor and Maintain:

10.1 **Monitoring:**
    - Regularly monitor the bot's activity and check for any issues.
    ~~- Set up local tests to run~~

10.2 **Maintenance:**
    - Update the bot if there are changes in the Twitter API or if improvements can be made.
    - Connect to Github Actions

### 11. Respect Twitter Policies:

11.1 **Review Twitter Policies:**
    - Familiarize yourself with and adhere to Twitter's automation rules and policies. (ongoing)

11.2 **Avoid Spammy Behavior:**
    - Ensure your bot provides value without being spammy or overly frequent. 

### 12. Share and Promote:

12.1 **Promote on Social Media:**
    - Share your bot on social media to attract users interested in Latin literature.

12.2 **Engage with Followers:**
    - Respond to mentions and engage with followers to build a community around your bot.

Remember to respect copyright and intellectual property laws when using Ovid's quotes, and give proper attribution if required. Additionally, always prioritize user experience and avoid any behavior that may violate Twitter's policies.


### 13. Add AI
#### Account Tweets
   * Incorporate GPT to add highlights to quote (or not?) 
   * **Generate new inspiring quotes from existing corpus:**
      * 

#### Accout Follow Replies
   * Abiliity to detect an account tweet and reply to it
   * Reply relevance

#### Review:
- https://www.youtube.com/watch?v=yLWLDjT01q8&ab_channel=GregKamradt%28DataIndy%29
