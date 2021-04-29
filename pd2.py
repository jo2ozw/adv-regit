#def Reception_(name)
import pandas as pd
import numpy as np
import pandas as pd
import regist as rg
import streamlit as st
#import speaktest as sp
st.header('受付窓口 チェック')
name = st.text_input('what your name')
choice = st.sidebar.selectbox("メニュー",('menu','冒険者登録','training','buy','sell'))

#if choice == "regist":
st.subheader("this is Adventurer registration")
rg.Registration(name)
#elif choice == "buy":
st.subheader("this is login screen")
#elif choice == "training":
st.subheader("this is training")

