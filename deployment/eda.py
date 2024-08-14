import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image

def run():
    #membuat judul
    st.title('LEAGUE LEGENDS ')

    #membuat sub header
    st.subheader('Evaluation Gameplay')

    #tambahkan gambar
    image = Image.open('kdalol.jpg')
    st.image(image, caption = 'Analysis League Legends Rank Diamond')

    #menambahkan deskripsi
    st.write('This Page made by bagus')

    # #font size
    # #font terbesar
    # st.write('# Halo')
    # st.write('## Halo')
    # #bold
    st.write('**Machine Learning**')
    # #italic
    st.write('*This machine learning was created to evaluate the Machine Learning concept in Phase 1 learning in the supervised learning model. apply Classification with the selected Dataset being high_diamond_ranked_10min, here I will evaluate one of the League Legends games with the multiplayer Online Battle Arena (MOBA) game type. In the first 10 minutes of the initial game statistics on one of the tiers/rankings, namely Diamond Rank, with the aim of helping the Game Developers RIOT to improve Arena Battle which is more balanced between the Blue Team and the Red Team, where the victory between these 2 teams affects the game scheme that should be there can be more balance between the abilities of player 1 and the others. by taking the pov game from the Blue Team with 1 game containing 10, blue team 5 players as well as the read team.*')

    #mmebuat batas dengan garis lurus
    st.markdown('---')

    #show dataframe
    data = pd.read_csv('high_diamond_ranked_10min.csv')
    st.dataframe(data)

    #membuat bar plot
    st.write('#### Blue Wins')
    fig = plt.figure(figsize=(15,5))
    sns.countplot(x='blueWins', data = data)
    st.pyplot(fig)
    st.write('*as you can see here from the 3000 data obtained, the victory of the blue team itself and the defeat they received can be said to be balanced but it does not rule out the possibility that there will be an absolute defeat, the cause of which must be known.*')
    #membuat plotly plot
    #membandingkan ratingpemain bola dengan proce nya
    st.write('#### Plotly plot - Blue Kills vs blue Total Exp ')
    fig = px.scatter(data, x = 'blueKills', y = 'blueTotalExperience', hover_data = ['blueKills', 'blueTotalExperience'])
    st.plotly_chart(fig)
    st.write('*Blue Kills vs blue Total Exp, this will affect what if the blue team gets a kill with the final result of the match getting the total exp*')

    #membuat histogram
    st.write('#### Total Minions Killed by Blue Team')
    fig = plt.figure(figsize=(15,5))
    sns.histplot(data['blueTotalMinionsKilled'], bins = 30, kde = True)
    st.pyplot(fig)
    st.write('*By looking at the Total Minions Killed by Blue Team, you can see that killing minions in the battle arena is necessary to achieve victory for the Blue Team itself.*')

    #membuat plotly plot
    #membandingkan gold diff dengan bluedeaths dengan proce nya
    st.write('#### Plotly plot - Blue Deaths vs blueGoldDiff')
    fig = px.scatter(data, x = 'blueDeaths', y = 'blueGoldDiff', hover_data = ['blueDeaths', 'blueGoldDiff'])
    st.plotly_chart(fig)
    st.write('*with the large number of deaths experienced by the blue team it will also affect the difference in gold they will receive*')
    
    #membuat histogram berdasarkan input user
    st.write('#### Histogram input by user')
    option = st.selectbox('Pilih column : ', ('blueAssists', 'blueTotalGold', 'blueAvgLevel', 'blueTotalMinionsKilled'))
    fig = plt.figure(figsize=(15,5))
    sns.histplot(data[option], bins = 30, kde = True)
    st.pyplot(fig)
    st.write('*You can also see assists, total gold, avg level, blueTotalMinionsKilled, on the blue team where this will also affect the blue teams from teh winning*')

    # #membuat plotly plot
    # #membandingkan ratingpemain bola dengan proce nya
    # st.write('#### Plotly plot - ')
    # fig = px.scatter(data, x = 'limit_balance', y = 'default_payment_next_month', hover_data = ['Name', 'Age'])
    # st.plotly_chart(fig)
    #tambahkan gambar
    image = Image.open('depan.jpg')
    st.image(image, caption = 'Analysis League Legends Rank Diamond')
if __name__ == '__main__':
    run()
