# WiseWordsOfOvid Twitter Bot

## Overview

Account @ [WiseWordsofOvid](https://twitter.com/WiseWordsOfOvid)

This repository contains code for a Twitter bot that tweets daily quotes from the Latin author Ovid. The bot fetches quotes from a curated dataset, formats them, and posts them on Twitter daily. This README provides an overview of the project, its structure, and key steps for setup and usage.

## Project Structure: Main Tasks:
* 1) Generate New Quotes:
   * **Methods Explored:**
      1) <u>Sentence similarity baseline:</u> Split each document into sentences and calculate the pairwise similarity between each sentence and each known quote. Randomly select sentences falling within the range of low to medium similarity, such as comparing the known quote 'The cause is hidden. The effect is visible to all.' to the generated quote 'And she confirmed her threats by the event,' which exhibits a similarity score of 0.24.
      **Take-away:** Holds more promise in many ways than a RAG-based retreival because you can apply more strict heuristics whereas with RAG you are constantly playing around with prompts which tend to repeat and also hallucinate.
      2) <u>RAG-based</u>
         * Posts quotes with commentary prompted by GPT-3 Turbo that are retrieved via Llama-indexing based sentence retrieval
         * Additional "memorable" quotes are retrieved using Langchain. [quote_retrieval](./notebooks/quote_retrieval.ipynb)
* 2) Replies to noteable Twitter accounts
* 3) [RAG](https://www.promptingguide.ai/techniques/rag)-based replies to @WiseWordsofOvide

## ML
### Hallucinations
Hallucinations (at the time of this), is a catch-all that basically means the model making something up that isn't really there.
* Interestingly, some of the hallucinations generate quotes that aren't even there but sound great. This quotes could be considered desirable as there is no infringment and represent the character of the bot: *The tongue is the instrument of the greatest good and the greatest evil that is in man.*

### Fine-tuning hand-picked responses


## Deployment
Digital Ocean Droplets

### Directories and Files:

- **data/:** Contains the dataset (`ovid_quotes.csv`) with Ovid's quotes in English and Latin. Full books as well:
   - Lovers Assistant
   - Last Poems
   - Metamorphoses
   - Fasti
   - Amours
   - Heroides
   - RemediaAmoris
   - The Poems of Exile (Tristia)

- **notebooks/:** Jupyter notebook for data exploration (`exploration.ipynb`).

- **src/:** Source code for the Twitter bot, including utility functions (`conn_utils.py`) and the main bot script (`ovid_bot.py`).

- **.github/workflows/:** GitHub Actions workflow for scheduling daily tweets (`tweet_schedule.yml`).

- **config.ini:** Configuration file for Twitter API keys and secrets.

- **.gitignore:** Specifies files and directories to be ignored by Git.

- **LICENSE:** License file.

- **README.md:** Project overview and guide.

- **requirements.txt:** List of project dependencies.

## Stretch Goal
~~Be able to gain enough followers/revenue to support infrastructure and lisence costs to support bot.~~ Follow-up: Does not seem feasible or even possible. See tweet by creator [@ZacksJerryRig](https://twitter.com/ZacksJerryRig/status/1759435310491144200)


## License

This project is licensed under the [MIT License](LICENSE).

## References
**Authorship Attribution/Verification**
   * [Who Wrote it and Why? Prompting Large-Language Models for Authorship Verification](https://arxiv.org/pdf/2310.08123.pdf)
