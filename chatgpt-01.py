import openai
import streamlit as st

OPENAI_API_KEY = '8c91c5c7058847f3820f9d7c12bbb1fb' 
OPENAI_AZURE_ENDPOINT = 'https://sktfly-ai.openai.azure.com/'
OPENAI_API_TYPE = "azure"
OPENAI_API_VERSION = "2023-05-15"


openai.api_key = OPENAI_API_KEY
openai.azure_endpoint = OPENAI_AZURE_ENDPOINT
openai.api_type = OPENAI_API_TYPE
openai.api_version = OPENAI_API_VERSION

st.header("ai시인",
          divider='rainbow',)

name = st.text_input('시인 이름')

if name:
    st.write('안녕하세요', name, '님')

subject = st.text_input('주제')
content = st.text_area('내용')

button = st.button('Send')

if button:
    with st.spinner('시를 작성중입니다...'):
        response = openai.chat.completions.create(
            model="dev-gpt-35-turbo",
            temperature=1,
            messages=[
                {'role':'system','content':'You are a chatbot.'},
                {'role':'user','content':name + '님의 시입니다.'},
                {'role':'user','content':'주제: ' + subject},
                {'role':'user','content':'내용: ' + content},
                {'role':'user','content':'이 내용으로 시를 지어줘'}
            ]
        )
    st.write(response.choices[0].message.content)
    st.success('시가 완성되었습니다.')