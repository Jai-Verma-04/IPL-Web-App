<div>
    <p> 
    <img src = "https://i.imgur.com/Y4OBbBG.png"; width = 100px; justify-content:right;>
    </p>

</div>

# IPLAnalytica
## Description
Welcome to IPLAnalytica Web App!
* This project is a data analysis and visualization tool for exploring statistics related to the **Indian Premier League (IPL) Cricket data**. 

* The project provides insights into player and team performances, match statistics, and an added functionality to generate scorecard of a particular match.

* The project is built upon the [streamlit](https://streamlit.io/) app framework to create a web app and help users better understand the insights gained from the data analysis of the [IPL Data](https://www.kaggle.com/datasets/patrickb1912/ipl-complete-dataset-20082020) using Python's [Pandas](https://pandas.pydata.org/) library.

* To find images for players/stadiums/team logos the project uses the [Google-Images-Search](https://pypi.org/project/Google-Images-Search/) Python library that uses Google [Custom Search API](https://console.developers.google.com/).

## Accessing the project:
To access the webpage of this project, [click here](https://iplanalytica.streamlit.app/)

In cases where you are getting something like the below image, just hit the **"Yes, get the app back up"** button and wait for the web app to launch.
![Logo](https://docs.streamlit.io/images/streamlit-community-cloud/app-state-zzzz.png)

## Running locally from your system

To run the project on your local machine run the following commands in your **command prompt** one by one.

1. Clone the github repository:

```bash
  git clone https://github.com/Jai-Verma-04/IPLAnalytica.git
```
2. Change current directory to IPLAnalytica folder
```bash
  cd path/to/folder/IPLAnalytica
```
3. Create a virtual environment (optional):
```bash
python -m venv /path/to/folder/IPLAnalytica
```
3. Install the required dependencies using:
```bash
pip install requirements.txt
```
4. The run the app using streamlit command:
```bash
streamlit run HOME.py
```
The app will open in your web browser, where you can navigate through the various pages.

# Screenshots of the website 👇
<div style="display: flex; flex-wrap: wrap; justify-content: center;">
  <img src="https://i.imgur.com/Cx1bytH.png" style="width: 300px; margin: 15px;" />
  <img src="https://i.imgur.com/1qoPaxL.png" style="width: 300px; margin: 15px;" />
  <img src="https://i.imgur.com/zp852WF.png" style="width: 300px; margin: 15px;" />
  <img src="https://i.imgur.com/rVBKD2A.png" style="width: 300px; margin: 15px;" />
  <img src="https://i.imgur.com/o8nCLxX.png" style="width: 300px; margin: 15px;" />
  <img src="https://i.imgur.com/ZVygxSD.png" style="width: 300px; margin: 15px;" />
  <img src="https://i.imgur.com/wzu7tZg.png" style="width: 300px; margin: 15px;" />
  <img src="https://i.imgur.com/jDPRUZG.png" style="width: 300px; margin: 15px;" />
</div>

## Lessons Learned
* The IPL Analytics Project provided valuable experience in **cleaning, filtering, and extracting insights** from large datasets using Pandas. 

* The implementation involved applying advanced **data manipulation techniques, including filtering, grouping, and aggregation**, to derive meaningful patterns and trends from the data. 

* To improve performance, the csv files were cleaned and converted to **.parquet data** files which greatly boosts the data reading/writing operations.

* The project also demonstrated the effective use of **Streamlit for deploying an interactive web application**, enabling seamless presentation of insights to users. 

## Known Issues/Bugs
1. UI not optimized to view from a phone.  
2. Player images might not exactly match the name of the player (though very few cases).  
→ This is because the data had the names of the palyers with First name initial and last name.  
→ For ex. A player named "T Kohli" had the same image as "V Kohli".  
→ This is because I used google_images_search api to extract these images and it is not feasible to check that each and every player's image matches its name.  


## Feedback
For any **feedback/suggestion/improvement** to the project, you can contact me on my email at [vermajai2004@gmail.com](mailto:vermajai2004@gmail.com) or Open a GitHub Issues [here](https://github.com/Jai-Verma-04/IPLAnalytica/issues)