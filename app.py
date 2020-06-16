import pandas as pd
file = "book1.xlsx"
data = pd.read_excel(file, "Hoja1") #reading file

titles = data['title'].values.tolist()
actives = data['active'].values.tolist()
descriptions = data['description'].values.tolist()

list_ = []

# getting length of list 
length = len(titles) 
    


def start():
    x = input('press anything to begin')
    continue_c = True


    # Iterating the index 
    # same as 'for i in range(len(list))' 
    for i in range(length): 
        print(titles[i])
        print(actives[i])
        print(descriptions[i])
        titleH2 = titles[i]
        activeNumb = actives[i]
        descriptionP = descriptions[i]
        
        new_element = f'<li><div class="policyObject"><div style="display: flex;align-items: center;width: 32%;margin-left: 1%;"><input type="radio"><div style="margin-left: 5%;"> <h2 style="font-size: 2vh; font-family: ProximaNova-Regular;"> {titleH2} </h2> <h3 style="font-family: ProximaNova-Regular;font-size: 2vh;color: #1C8098;">{activeNumb}</h3></div></div><div style="width: 60%;font-family: ProximaNova-Regular;font-size: 2vh">{descriptionP}</div></div></li>'
        print(new_element)

        list_.append(new_element)

    #We convert list onto a string so we don't have commas
    final_s = ""
    final_s = final_s.join(list_)
    
    print("**************************************************************************")
    print(" FINAL RESULT FINAL RESULT FINAL RESULT FINAL RESULT FINAL RESULT ")
    print("**************************************************************************")
    print(final_s)



start()