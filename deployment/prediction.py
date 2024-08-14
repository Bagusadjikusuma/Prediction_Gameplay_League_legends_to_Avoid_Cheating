import streamlit as st
import pandas as pd
import numpy as np
import pickle
import json
from PIL import Image
#Load All files
#Load model



with open('best_pipe_SVM.pkl', 'rb') as file_3:
  best_pipe_svm = pickle.load(file_3)



def run():
        #tambahkan gambar
    image = Image.open('jinxlol.jpg')
    st.image(image, caption = 'Analysis League Legends Rank Diamond')
    with st.form('form_League_Legends'):
        #nama, value untuk default value
        GameID = st.text_input('gameId', value = ' ')

        #blueWardsPlaced, min_value untuk minimum nilai yang bisa diisi, max_value maksimum nilai yang bisa diisi
        blueWardsPlaced = st.number_input('blueWardsPlaced', value = 1, min_value = 0, max_value = 60, help = 'fill with wards places')

        #blueWardsDestroyed 
        blueWardsDestroyed = st.number_input('blueWardsDestroyed', value = 2, min_value = 0, help = 'fill with wards destroyed')

        #blueWardsDestroyed 
        blueFirstBlood = st.number_input('blueFirstBlood', value = 3, min_value = 0, help = 'fill with Blue First Blood')
        
        #blueWardsDestroyed 
        blueKills = st.number_input('blueKills', value = 3, min_value = 2, help = 'fill with Blue Kills')

        #blueWardsDestroyed 
        blueDeaths = st.number_input('blueDeaths', value = 2, min_value = 1, help = 'fill with Blue Deaths')

        #blueWardsDestroyed 
        blueAssists = st.number_input('blueAssists', value = 1, min_value = 0, help = 'fill with Assists By Blue Team')
        st.markdown('---')
        
        blueEliteMonsters = st.slider('blueEliteMonsters', value = 0, min_value = 0, max_value = 1)

        blueDragons = st.slider('blueDragons', value = 0, min_value = 0, max_value = 1)

        # st.markdown('---')
        #index untuk default value di selctbox/radio button
        blueHeralds = st.selectbox('blueHeralds', ('0', '1'), index = 0)
        
        blueTowersDestroyed = st.slider('blueTowersDestroyed', value = 0, min_value = 0, max_value = 4)

        # defensive_work_rate = st.radio('Defensive Work Rate', ('Low', 'Medium', 'High'), index = 1)
        st.markdown('---')
        blueTotalGold = st.number_input('blueTotalGold', min_value = 100, max_value = 20000, value = 100)
        blueAvgLevel = st.number_input('blueAvgLevel', min_value = 0.0, max_value = 100.0, value = 0.0, step = 0.01)
        blueTotalExperience = st.number_input('blueTotalExperience', min_value = 11000, max_value = 20000, value = 11000)
        blueTotalMinionsKilled = st.number_input('blueTotalMinionsKilled', min_value = 98, max_value = 500, value = 99)
        blueTotalJungleMinionsKilled = st.number_input('blueTotalJungleMinionsKilled', min_value = 0, max_value = 100, value = 0)
        blueGoldDiff = st.number_input('blueGoldDiff', min_value = -100, max_value = 500, value = 50)
        blueExperienceDiff = st.number_input('blueExperienceDiff', min_value = -10000, max_value = 25000, value = 100)
        blueCSPerMin = st.number_input('blueCSPerMin', min_value = 0.0, max_value = 40.0, value = 1.0)
        blueGoldPerMin = st.number_input('blueGoldPerMin', min_value = 500.0, max_value = 50000.0, value = 1000.0)


        #bikin submit button form
        submitted = st.form_submit_button('Predict')
        
    data_inf = {
        'gameId': GameID,
        'blueWardsPlaced': blueWardsPlaced,
        'blueWardsDestroyed': blueWardsDestroyed,
        'blueFirstBlood':blueFirstBlood,
        'blueKills':blueKills,
        'blueDeaths':blueDeaths,
        'blueAssists':blueAssists,
        'blueEliteMonsters':blueEliteMonsters,
        'blueDragons':blueDragons,
        'blueHeralds':blueHeralds,
        'blueTowersDestroyed':blueTowersDestroyed,
        'blueTotalGold':blueTotalGold,
        'blueAvgLevel':blueAvgLevel,
        'blueTotalExperience':blueTotalExperience,
        'blueTotalMinionsKilled':blueTotalMinionsKilled,
        'blueTotalJungleMinionsKilled':blueTotalJungleMinionsKilled,
        'blueGoldDiff':blueGoldDiff,
        'blueExperienceDiff':blueExperienceDiff,
        'blueCSPerMin':blueCSPerMin,
        'blueGoldPerMin':blueGoldPerMin
    }
    data_inf = pd.DataFrame([data_inf])
    st.dataframe(data_inf)

    if submitted:
        # #split between numerical and categorical columns
        # data_inf_nums = data_inf[num_columns]
        # data_inf_cate = data_inf[cat_columns]

        # #feature scaling and encoding

        # data_inf_num = pd.DataFrame(data_inf_nums, columns=num_columns)
        # data_inf_cat = pd.DataFrame(data_inf_cate, columns=cat_columns)
        # data_inf_final = np.concatenate([data_inf_num,data_inf_cat], axis = 1)

        # # Ubah hasil concatenate menjadi DataFrame
        # data_inf_final = pd.DataFrame(data_inf_final, columns=num_columns + cat_columns)

        # #predict using linear reg model

        pred_inf_final = best_pipe_svm.predict(data_inf)

        st.write('## Blue Wins : ', str(int(pred_inf_final)))
        #tambahkan gambar
        image = Image.open('depan.jpg')
        st.image(image, caption = 'Analysis League Legends Rank Diamond')


if __name__ == '__main__':
   run()


