# Olympics Data Analysis Web Application

This is a Streamlit web application dashboard which is developed to review the relevance of population & GDP to countries' performances at the Olympics. In doing this, aim was to  choose a "modern" subset of Olympic Games, ranging from 1960 to 2016 to align with our economic and demographic data. As there is a larger breadth of competing countries in this range and a better record of population and wealth statistics. The term “modern” can be better understood by our Parameters. The web Application gives an insight into how different factors are correlated with each other and how it impacts the performance of a particular country in olympics. This dashboard was made to look into various issues of why 2020 Games Postponed due to COVID? which is a great topic to look into. What’s the relevance of population & GDP to countries' performance at the Olympics.

# Dataset Link

For making the above dashboard the following dataset has been used:
- https://www.kaggle.com/heesoo37/120-years-of-olympic-history-athletes-and-results

# Live Demo

The user can easily access the web application dashboard by clicking on the below link:
- https://olympic-analysis-dashboard.herokuapp.com/

# Parameters

- Date range is from 1960 to 2016. This reflects the combined data from the World Bank and Olympic Data that overlapped for this project.
- Country names and boundaries have changed in the last sixty years. As an example: if you are looking for the full Olympic history of a country that was renamed - like Russia - you will need to look for both the Soviet Union and Russia.
- Not all countries have competed in both the Summer and Winter Olympics, and thus you may see some "blank" graphs due to non-participation.
- Winter and Summer Olympics were held in the same year until 1992, until they split into separate four-year cycles. The next Winter Olympics was held in 1994.

# Tech Stack

- Streamlit
- Python (Version == 3.79)

# Features of Web Portal
## Medal Tally Page

In the overall analysis, the user can easily compare the medals won by different countries and see the country with the highest medals count till 2016. Also, in this page the user can easily see the medals received by a particular country in a particular year by easily selecting the required year or the country through the dropdown in the bottom left of the UI.

![medaltally](https://user-images.githubusercontent.com/43933680/137168390-87590809-8a56-4241-bff3-77d997a7f126.png)

## Overall Analysis

This section of the Web application focuses on giving a detailed overall statistics related to the no of events taken place till date, no of atheltes who have participated in the olympics from various countries in past 120 years from 2016. It provides a medium through which user could easily visualize number of events that have taken place per sport in a particular year using a heatmap. It also gives an insight into top players which comes with an option to filter the view according to the preference of sport or see an overall comparison.

![overall1](https://user-images.githubusercontent.com/43933680/137169646-20531895-c24a-4ae3-8c95-22361e65625f.PNG)
![overall2](https://user-images.githubusercontent.com/43933680/137169685-26bc9e42-315f-4574-90f4-dfc831e7c68d.PNG)
![overall5](https://user-images.githubusercontent.com/43933680/137169735-b7aa0dba-0c9c-4c18-b64d-78562687038f.PNG)
![overall7](https://user-images.githubusercontent.com/43933680/137169749-74d83cca-24a5-4d47-8601-1280d5c7b76a.PNG)

## Country Wise Analysis

The user lands into a page where he could select a country from the below left dropdown and analyze it separetely in detail. The analytics in this section includes the GDP, Population and participation comparison over the years and how they are correlated can be easily visualized by a following plot, how the country atheletes have performed in various sports year wise, gender ration of participation from the countary in 120 years and a view of how the medal in various categories varied with reapect to the winter and summer olympics. 

![cwise3](https://user-images.githubusercontent.com/43933680/137170579-6abd1f1b-e1b2-4207-99d7-d6b5b5b9c0f5.PNG)
![cwise1](https://user-images.githubusercontent.com/43933680/137170602-702db32b-f914-4de3-80bb-f7a2437f783b.PNG)![cwise5](https://user-images.githubusercontent.com/43933680/137170590-48ff0b39-dac1-47c6-b073-647c348ad241.PNG)
![cwise6](https://user-images.githubusercontent.com/43933680/137170595-a24ad235-ab38-46ea-838f-414d38976f98.PNG)

## Athelete Wise Analysis

This section focuses on comparing physiques and age of different atheletes from various countaries and gives an insight into the optimal factors for a medalists participating in the olympics. It has also a secton where the user can view the distribution of the age with the different sports in the olympics over all the years.

![medal1](https://user-images.githubusercontent.com/43933680/137171069-ec5ea1c7-da63-4572-8152-9a835c106305.PNG)
![medal2](https://user-images.githubusercontent.com/43933680/137171078-876a148b-6bed-4509-a583-352bf80067c7.PNG)
![medal3](https://user-images.githubusercontent.com/43933680/137171081-a96762e7-2fb1-4455-be39-3bc59e6d8a92.PNG)

# Novelty

- A simple and efficient UI/UX used in the web portal which makes understanding of the analytics easier.
- A platform where we can easily compare and analyze the GDP, Population and the medal counts of various countaries with each other and also view there participation trend by a single click.
- Through this platform we can easily compare the medalists from various countaries and find out the optimal height, weight and age of the atheletes who are winning the medals during olympics.
- A quick insight into the gender ratio in Olympics on overall basis as well as countary wise with further details by year wise.

# Flowchart of Methodology
![Methodology](https://user-images.githubusercontent.com/43933680/137181353-364ae547-0bca-45a4-88f0-fcc833f645f3.jpg)

# Observations

What was observed in the visualizations is that there appeared to be a correlation between medal counts and GDP. Which would suggest that further analysis could be done on the statistical significance of this visible correlation.
However, still there is no apparent correlation between medal counts and population. Which would deter us from further analysis.


