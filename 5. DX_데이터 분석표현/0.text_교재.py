import streamlit as st
import pandas as pd

st.markdown('# Unit 1. Text elements')
st.caption('text 참고사이트: https://docs.streamlit.io/library/api-reference/text')


st.markdown('## 1. title, header, subheader, caption')

st.title('This is the title')
st.header('This is the header')
st.subheader('This is the subheader')
st.text('This is the text')
st.caption('Caption in small font')


# st.markdown('## 2. Markdown')

# st.markdown('# This is a Markdown title')
# st.markdown('## This is a Markdown header')
# st.markdown('### This is a Markdown subheader')
# st.markdown('This is the markdown')
# st.markdown('This is **the markdown 진하게**')
# st.markdown('This is _the markdown 기울임_')
# st.markdown('This is *the markdown 기울임*')
# st.markdown('This is **_the markdown 진하고 기울임_**')

# st.markdown('- item \n'
#             '  - item \n'    # 최소 2칸
#             '  - item \n'
#             '    - item \n'  # 최소 4칸
#             '- item ')

# st.markdown('1. item 1\n'
#             '   1. item 1.1\n'   # 최소 3칸
#             '   1. item 1.2\n'
#             '      1. item 1.2.1\n'  # 최소 6칸
#             '1. item 2')

# st.text('1. item 1\n'
#             '   1.1. item 1.1\n'   # 최소 3칸
#             '   1.2. item 1.2\n'
#             '      1.2.1. item 1.2.1\n'  # 최소 6칸
#             '2. item 2')

# st.markdown('## 3. divider')
# st.divider()

# st.markdown('## 4. Code, Latex')
# st.code('x=1234')
# st.latex(r''' a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} = \sum_{k=0}^{n-1} ar^k = a \left(\frac{1-r^{n}}{1-r}\right) ''') 

# st.markdown('## 5. Write')
# st.markdown('String, data_frame, chart, graph, LaTex 등의 objects를 App에  출력할 수 있다.')
# st.caption('참고사이트: https://docs.streamlit.io/library/api-reference/write-magic/st.write')

# st.write('this is a string write')
# st.write('Hello, *World!* 😄')

# df = pd.DataFrame({'first column': [1, 2, 3, 4],'second column': [10, 20, 30, 40]})
# st.write('Below is a DataFrame:', df, 'Above is a dataframe.')


# 파일실행: File > New > Terminal(anaconda prompt) → python -m streamlit run streamlit\0.text_교재.py