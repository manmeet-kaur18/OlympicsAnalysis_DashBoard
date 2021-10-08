import streamlit as st
import pandas as pd
import preprocessor,helper
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.figure_factory as ff
import plotly.graph_objects as go


df = pd.read_csv('athlete_events.csv')
region_df = pd.read_csv('noc_regions.csv')
gdp_df = pd.read_csv('gdp.csv')
pop_df = pd.read_csv('Population.csv')
df = preprocessor.preprocess(df,region_df)

st.sidebar.title("Olympics Analysis")
st.sidebar.image('https://upload.wikimedia.org/wikipedia/en/b/b1/Olympic_Rings.svg')
user_menu = st.sidebar.radio(
    'Select an Option',
    ('Medal Tally','Overall Analysis','Country-wise Analysis','Athlete wise Analysis')
)

if user_menu == 'Medal Tally':
    st.sidebar.header("Medal Tally")
    years,country = helper.country_year_list(df)

    selected_year = st.sidebar.selectbox("Select Year",years)
    selected_country = st.sidebar.selectbox("Select Country", country)

    medal_tally = helper.fetch_medal_tally(df,selected_year,selected_country)
    if selected_year == 'Overall' and selected_country == 'Overall':
        st.title("Overall Tally")
    if selected_year != 'Overall' and selected_country == 'Overall':
        st.title("Medal Tally in " + str(selected_year) + " Olympics")
    if selected_year == 'Overall' and selected_country != 'Overall':
        st.title(selected_country + " overall performance")
    if selected_year != 'Overall' and selected_country != 'Overall':
        st.title(selected_country + " performance in " + str(selected_year) + " Olympics")
    st.table(medal_tally)

if user_menu == 'Overall Analysis':
    editions = df['Year'].unique().shape[0] - 1
    cities = df['City'].unique().shape[0]
    sports = df['Sport'].unique().shape[0]
    events = df['Event'].unique().shape[0]
    athletes = df['Name'].unique().shape[0]
    nations = df['region'].unique().shape[0]

    st.title("Top Statistics")
    col1,col2,col3 = st.columns(3)
    with col1:
        st.header("Editions")
        st.title(editions)
    with col2:
        st.header("Hosts")
        st.title(cities)
    with col3:
        st.header("Sports")
        st.title(sports)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.header("Events")
        st.title(events)
    with col2:
        st.header("Nations")
        st.title(nations)
    with col3:
        st.header("Athletes")
        st.title(athletes)

    nations_over_time = helper.data_over_time(df,'region')
    fig = px.line(nations_over_time, x="Edition", y="region")
    st.title("Participating Nations over the years")
    st.plotly_chart(fig)

    events_over_time = helper.data_over_time(df, 'Event')
    fig = px.line(events_over_time, x="Edition", y="Event")
    st.title("Events over the years")
    st.plotly_chart(fig)

    athlete_over_time = helper.data_over_time(df, 'Name')
    fig = px.line(athlete_over_time, x="Edition", y="Name")
    st.title("Athletes over the years")
    st.plotly_chart(fig)

    st.title("No. of Events over time(Every Sport)")
    fig,ax = plt.subplots(figsize=(20,20))
    x = df.drop_duplicates(['Year', 'Sport', 'Event'])
    ax = sns.heatmap(x.pivot_table(index='Sport', columns='Year', values='Event', aggfunc='count').fillna(0).astype('int'),
                annot=True)
    st.pyplot(fig)

    st.title("Most successful Athletes")
    sport_list = df['Sport'].unique().tolist()
    sport_list.sort()
    sport_list.insert(0,'Overall')

    selected_sport = st.selectbox('Select a Sport',sport_list)
    x = helper.most_successful(df,selected_sport)
    st.table(x)

if user_menu == 'Country-wise Analysis':

    st.sidebar.title('Country-wise Analysis')

    country_list = df['region'].dropna().unique().tolist()
    country_list.sort()

    selected_country = st.sidebar.selectbox('Select a Country',country_list)

    st.title(selected_country + " GDP, Population and Participation Tally over the years")

    data = {'Year':[],'GDP':[],'Population':[],'Total Participants':[]}
    temp_df = df[df["region"]==selected_country]
    temp = temp_df['Year'].unique()
    temp = sorted(temp)

    for year in temp:
        temp1 = temp_df[temp_df["Year"]==year]
        gdp_1 = gdp_df[gdp_df['Country Name']==selected_country]
        year1 = str(year) + " ["+"YR"+ str(year) +"]"

        if year1 in gdp_1.columns:
            pop_1 = pop_df[pop_df['Country Name']==selected_country]
            participants = temp1["Name"].nunique()
            if gdp_1[year1].iloc[0] != ".." and pop_1[year1].iloc[0]!= '..':
                data['Year'].append(year)
                data['GDP'].append(float(gdp_1[year1].iloc[0])/100000000)
                data['Population'].append(float(pop_1[year1].iloc[0])/1000000)
                data['Total Participants'].append(int(participants))
    st.table(data)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data['Year'], y=data['GDP'],
                    mode='lines',
                    name='GDP'))
    fig.add_trace(go.Scatter(x=data['Year'], y=data['Population'],
                    mode='lines+markers',
                    name='Population'))
    fig.add_trace(go.Scatter(x=data['Year'], y=data['Total Participants'],
                    mode='lines', name='Total Participants'))
    fig.update_layout(autosize=False,width=800,height=500,
    margin=dict(
        l=0,
        r=0,
        b=0,
        t=0,
        pad=4
    ),
    )
    st.plotly_chart(fig)


    country_df = helper.yearwise_medal_tally(df,selected_country)
    fig = px.line(country_df, x="Year", y="Medal")
    st.title(selected_country + " Medal Tally over the years")

    st.plotly_chart(fig)

    

    st.title(selected_country + " excels in the following sports")
    pt = helper.country_event_heatmap(df,selected_country)
    fig, ax = plt.subplots(figsize=(20, 20))
    ax = sns.heatmap(pt,annot=True)
    st.pyplot(fig)

    st.title("Top 10 athletes of " + selected_country)
    top10_df = helper.most_successful_countrywise(df,selected_country)
    st.table(top10_df)

    #sex Ratio

    st.title("Sex Ratio among Participating Atheletes " + selected_country)
    temp_df = df[['region', 'Sex']]
    temp_df = temp_df[temp_df["region"]==selected_country]
    
    final_df = {"Sex":["Male Atheletes","Female Atheletes"],
    "count":[temp_df['Sex'].tolist().count('M'),temp_df['Sex'].tolist().count('f')]}

    fig, ax = plt.subplots(figsize=(8, 8))
    # ax = sns.heatmap(pt,annot=True)
    colors = sns.color_palette('bright')[0:2]
    data = [temp_df["Sex"].value_counts()['F'],temp_df["Sex"].value_counts()['M']]
    ax = plt.pie(data, labels = final_df['Sex'], colors = ['yellow','pink'], autopct='%.0f%%')
    st.pyplot(fig) 

    # st.table(df[:100])
    
    st.title(selected_country + " Year wise Participation and Success Rate Analysis")
    temp_df = df[['Year','region','Medal','Name','Season']]
    temp_df = temp_df[temp_df['region']==selected_country]
    final_df = temp_df['Year'].unique()
    final_df = sorted(final_df)

    final_data = {'Year':[],'Gold':[],'Silver':[],'Bronze':[],'No. of Games Participated':[]}
    for year in final_df:
        
        temp = temp_df[temp_df["Year"]==year]
        goldcount = temp['Medal'].tolist().count('Gold')
        silvecount = temp['Medal'].tolist().count('Silver')
        bronzecount = temp['Medal'].tolist().count('Bronze')
        TotalParticipation = len(temp)

        final_data['Year'].append(year)
        final_data['Gold'].append(goldcount)
        final_data['Silver'].append(silvecount)
        final_data['Bronze'].append(bronzecount)
        final_data['No. of Games Participated'].append(TotalParticipation)

    st.table(final_data)

    st.title("Summer olympics vs Winter Olympics Medal Analysis")
    temp_df1 = temp_df[temp_df['Season']=="Summer"]
    temp_df2 = temp_df[temp_df['Season']=="Winter"]
    
    country_list = df['Season'].dropna().unique().tolist()
    country_list.sort()

    selected_sport = st.selectbox('Select a Season', country_list)
    final_data1 = {'Medals':['Gold','Silver','Bronze'],'Count':[]}

    if selected_sport == "Summer":
        if len(temp_df1) > 0:
            goldcounts = temp_df1["Medal"].tolist().count('Gold')
            silvercounts = temp_df1['Medal'].tolist().count('Silver')
            bronzecounts = temp_df1['Medal'].tolist().count('Bronze')
            final_data1['Count'].append(goldcounts)
            final_data1['Count'].append(silvercounts)
            final_data1['Count'].append(bronzecounts)
    else:
        if len(temp_df2) > 0:
            goldcountw = temp_df2["Medal"].tolist().count('Gold')
            silvercountw = temp_df2['Medal'].tolist().count('Silver')
            bronzecountw = temp_df2['Medal'].tolist().count('Bronze')
            final_data1['Count'].append(goldcountw)
            final_data1['Count'].append(silvercountw)
            final_data1['Count'].append(bronzecountw)
   

    if len(final_data1['Count']) > 0:
        fig = go.Figure(data=[go.Pie(labels=final_data1['Medals'], values=final_data1['Count'], hole=.2)]) 
        fig.update_layout(autosize=False,width=700,height=700)
        st.plotly_chart(fig)
    else:
        st.title("No Participation in this Season")

if user_menu == 'Athlete wise Analysis':
    athlete_df = df.drop_duplicates(subset=['Name', 'region'])

    x1 = athlete_df['Age'].dropna()
    x2 = athlete_df[athlete_df['Medal'] == 'Gold']['Age'].dropna()
    x3 = athlete_df[athlete_df['Medal'] == 'Silver']['Age'].dropna()
    x4 = athlete_df[athlete_df['Medal'] == 'Bronze']['Age'].dropna()

    fig = ff.create_distplot([x1, x2, x3, x4], ['Overall Age', 'Gold Medalist', 'Silver Medalist', 'Bronze Medalist'],show_hist=False, show_rug=False)
    fig.update_layout(autosize=False,width=800,height=600)
    st.title("Distribution of Age")
    st.plotly_chart(fig)

    x = []
    name = []
    famous_sports = ['Basketball', 'Judo', 'Football', 'Tug-Of-War', 'Athletics',
                     'Swimming', 'Badminton', 'Sailing', 'Gymnastics',
                     'Art Competitions', 'Handball', 'Weightlifting', 'Wrestling',
                     'Water Polo', 'Hockey', 'Rowing', 'Fencing',
                     'Shooting', 'Boxing', 'Taekwondo', 'Cycling', 'Diving', 'Canoeing',
                     'Tennis', 'Golf', 'Softball', 'Archery',
                     'Volleyball', 'Synchronized Swimming', 'Table Tennis', 'Baseball',
                     'Rhythmic Gymnastics', 'Rugby Sevens',
                     'Beach Volleyball', 'Triathlon', 'Rugby', 'Polo', 'Ice Hockey']
    for sport in famous_sports:
        temp_df = athlete_df[athlete_df['Sport'] == sport]
        x.append(temp_df[temp_df['Medal'] == 'Gold']['Age'].dropna())
        name.append(sport)

    fig = ff.create_distplot(x, name, show_hist=False, show_rug=False)
    fig.update_layout(autosize=False, width=800, height=600)
    st.title("Distribution of Age wrt Sports(Gold Medalist)")
    st.plotly_chart(fig)

    sport_list = df['Sport'].unique().tolist()
    sport_list.sort()
    sport_list.insert(0, 'Overall')

    st.title('Height Vs Weight')
    selected_sport = st.selectbox('Select a Sport', sport_list)
    temp_df = helper.weight_v_height(df,selected_sport)
    fig,ax = plt.subplots()
    ax = sns.scatterplot(temp_df['Weight'],temp_df['Height'],hue=temp_df['Medal'],style=temp_df['Sex'],s=60)
    st.pyplot(fig)

    st.title("Men Vs Women Participation Over the Years")
    final = helper.men_vs_women(df)
    fig = px.line(final, x="Year", y=["Male", "Female"])
    fig.update_layout(autosize=False, width=800, height=600)
    st.plotly_chart(fig)



