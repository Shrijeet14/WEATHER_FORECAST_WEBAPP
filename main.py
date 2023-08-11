import streamlit as st 
import plotly.express as px
from backend import get_data

st.set_page_config(layout="centered",
                   page_title="Weather Forecast Web App",
                   page_icon=":sun:")


st.title("Weather Forecast For The Next Days")
place=st.text_input("PLACE :-")
forecast_days=st.slider('FORECAST DAYS :-', 1, 5 ,key="slider",help="Select the number of days to forecast")
view_type=st.selectbox('Select Data To View', ['Temperature', 'Sky' , 'Humidity'] , key="view")

st.subheader(f"{view_type} for the next {forecast_days} days in {place}")



if place:

    try:
        filtered_data=get_data(place,forecast_days)
        dates= [dict['dt_txt'] for dict in filtered_data]
        if(view_type=="Temperature"):
            
            # getting the final data as list
            filtered_data_temp= [dict['main']['temp']-273 for dict in filtered_data]
            filtered_data_temp_feel= [dict['main']['feels_like']-273 for dict in filtered_data]
            filtered_data_mintemp= [dict['main']['temp_min']-273 for dict in filtered_data]
            filtered_data_maxtemp= [dict['main']['temp_max']-273 for dict in filtered_data]

            # plotting the data
            figure_temp = px.line(x=dates,y=filtered_data_temp , labels={"x": "Date" , "y":"Temperature(C)"})

            figure_temp_feel = px.line(x=dates,y=filtered_data_temp_feel , labels={"x": "Date" , "y":"Actual Temperature Feels Like(C)"})

            figure_maxtemp = px.line(x=dates,y=filtered_data_maxtemp , labels={"x": "Date" , "y":"Maximum Temperature(C)"})

            figure_mintemp = px.line(x=dates,y=filtered_data_mintemp , labels={"x": "Date" , "y":"Minimum Temperature(C)"})

            st.plotly_chart(figure_temp)
            st.plotly_chart(figure_temp_feel)
            st.plotly_chart(figure_maxtemp)
            st.plotly_chart(figure_mintemp)

        elif(view_type=='Humidity'):

            # getting the final data as list
            filtered_data_humidity= [dict['main']['humidity'] for dict in filtered_data]

            # plotting the data
            figure_humidity = px.line(x=dates,y=filtered_data_humidity , labels={"x": "Date" , "y":"Relative  Humidity"})

            st.plotly_chart(figure_humidity)

        elif(view_type=="Sky"):

            # getting the final data as list
            filtered_data_sky= [dict['weather'][0]['main'] for dict in filtered_data]
            filtered_data_sky_description= [dict['weather'][0]['description'] for dict in filtered_data]
            image_dict={'Clear':'images/clear.png','Clouds':'images/cloud.png','Rain':'images/rain.png','Snow':'images/snow.png'}

            image_paths=[image_dict[conditions] for conditions in filtered_data_sky]
            
            caption_weather= [item2+'  '+item1 for item1, item2 in zip(filtered_data_sky_description, dates)]
            
            # plotting the data
            st.image(image_paths,width=115 , caption=caption_weather)
        else:
            print("Requested Weather Type Not Available")

    except KeyError :
        st.write("The City You Entered Doesn't Exist")

