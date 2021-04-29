def Reception_desk(name):
 import streamlit as st
# import speaktest as sp

 choice = st.sidebar.selectbox("メニュー",('menu','regist','training','buy','sell'))
 
 if choice == "regist":
 	st.subheader("this is Adventurer registration")
 
 elif choice == "LOGIN":
 		st.subheader("this is login screen")
 elif choice == "training":
 		st.subheader("this is training")
 
 
 import pandas as pd
 import numpy as np
 import pandas as pd
# a = sp.speak()
 st.subheader("初めてギルドにいらした方は ")
 st.subheader("最初に登録をお済ませください。")
 st.subheader("登録がお済みになられてから ")
 st.subheader("ギルドのサービスをご利用できます。 ")
 h_name = st.text_input ("ハンドルネームを下のテキストボックスにご入力ください。")
 return
