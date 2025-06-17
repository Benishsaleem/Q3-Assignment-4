SENTENCE_START:str = "Panaversity is fun. I learned to program and used Python to make my " 

def main():
    adjective:str = str(input("\033[1;3m Please Enter an Adjective: \033[0m"))
    noun:str = str(input("\033[1;3m Please Enter a Noun: \033[0m"))
    verb:str = str(input("\033[1;3m Please Enter a Verb: \033[0m"))
    
    print(f"{SENTENCE_START} {adjective} {noun} {verb} !")
    
if __name__ == "__main__":
    main()

