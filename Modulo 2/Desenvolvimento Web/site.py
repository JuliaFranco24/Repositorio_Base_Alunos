import streamlit as st

coluna=st.columns(4)
numero= st.text_input('Digite um número:  ')
numero2= st.text_input('Digite um número2: ')


# numero3= st.text_input('Digite um número:')
# numero4=st.text_input('Digite um número:    ')
# numero5=st.text_input('Digite um número:      ')
# numero6=st.text_input('Digite um número:       ')
# numero7=st.text_input("Digite um número:        ")
# numero8=st.text_input("Digite um número:         ")


with coluna[0]:
    
    if st.button('Clique para somar'):
        resultado= int(numero)+ int(numero2)
        st.write(resultado)
with coluna[1]:
   
   if st.button('Clique para dividir'):
       resultado2= int(numero)/ int(numero2)
       st.write(resultado2)

with coluna[2]:

    if st.button("Clique para subtrair"):
        resultado3= int(numero)-int(numero2)
        st.write(resultado3)

with  coluna[3]:

    if st.button("Clique para multiplicar:"):
        resultado4=int(numero)*int(numero2)
        st.write(resultado4)

  

 # type: ignore # ig
 
 
 
 
 
