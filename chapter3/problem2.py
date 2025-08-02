# write a program to fill in a letter template given below with name and date
letter = '''
        Dear <|Name|>,
        Yoou are selected!
        <|Date|>
        '''


print(letter.replace("<|Name|>","Anurag").replace("<|Date|>","02 August 2025"))
