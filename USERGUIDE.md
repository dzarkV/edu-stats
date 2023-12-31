# Users guide

This project provides access to Colombian education indicators based on years.

The purpose of this project is to allow users to retrieve education indicators specific to Colombia :bar_chart:, such as enrollment rates by primary and secondary grades, and graduation rates, based on different years.

By using this project, users can easily access and analyze education data to gain insights into the educational landscape in Colombia over time. You just need to select the indicator and clic on **Run Query** button.

:notebook_with_decorative_cover: Note: This project consult a valid data source containing the education indicators for Colombia, organized by years, hosted in Google Big Query service.

## Run this project

First, open a terminal and clone this project on a folder with

```bash
mkdir folder
cd folder
git clone https://github.com/dzarkV/edu-stats.git
cd edu-stats 
```

Then you need to run `make get-credentials` to run activate.sh script. Or directly run it in your terminal:

```bash
chmod +x ./activate.sh && ./activate.sh
```

It will ask you for the name of the Slack channel to get the environment variables needed to run the project :closed_lock_with_key:.
After that, you can run (make sure you have Docker and Docker compose installed :whale2:):

```bash
docker compose up
```

You can see a brief explanation video about the project [this](https://youtu.be/AzVhnX6oH7w)
