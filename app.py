import streamlit as st
import joblib

def main():
    html_temp ="""
    <div style="background-color:lightgreen;padding:17px">
    <h2 style="color:darkblue";text-align:center> Health Insurance Cost Prediction Using ML </h2>
    </div>
    
    
    """
    
    
    st.markdown(html_temp,unsafe_allow_html=True)
    
    model=joblib.load('model_joblib_gr1')
    
    p1=st.slider('Enter Age', 18,100)
    s1= st.selectbox('sex', ('Male','Female'))
    
    if s1=='Male':
        p2=1
    else:
        p2=0
        
    p3=st.number_input('BMI')
    
    p4=st.slider('Amount of Children',0,4)
    
    s2=st.selectbox('Smoker', ('Yes', 'No'))
    
    if s2=='Male':
        p5=1 
    else:
        p5=0
    
    p6=st.slider("Enter region",1,4)
    
    if st.button('Predict'):
        pred=model.predict([[p1,p2,p3,p4,p5,p6]])
        
        st.balloons()
        st.success('Insurance cost {}'.format(round(pred[0],2)))

   




if __name__=='__main__':
    main()

