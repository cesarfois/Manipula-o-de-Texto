


with open('cesar.dwcontrol', 'w', encoding='utf-8') as arquivo:
    #OBRIGATORIO <ControlStatements xmlns="http://dev.docuware.com/Jobs/Control" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
    arquivo.write("<ControlStatements xmlns=\"http://dev.docuware.com/Jobs/Control\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\">\n\n")
    arquivo.write("<Page>\n\n")

    arquivo.write(" <Field dbName=\"EMPRESA\" type=\"Text\" value=\"Peters Engineering\"/>\n")
  

    # Obrigatorio  
    arquivo.write("\n</Page>")
    arquivo.write("\n</ControlStatements>")








# <ControlStatements xmlns="http://dev.docuware.com/Jobs/Control" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">

# <Page>
# <Field dbName="EMPRESA" type="Text" value="Peters Engineering"/>
# <Field dbName="RESPONSAVEL" type="Text" value="Construction"/>
# <Field dbName="REVISOR" type="Text" value="Area determination"/>
# <Field dbName="TIPO_DE_DOCUMENTO" type="Text" value="invoice"/>

# </Page>
# </ControlStatements>