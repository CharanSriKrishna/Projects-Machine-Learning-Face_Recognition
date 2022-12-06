import pandas as pd

def check():
    with open('attendance.csv', 'r+') as f:
        with open('present.csv','r+') as doc:
            my=doc.readlines()
            myDataList = f.readlines()
            for line in myDataList:
                entry = line.split(',')
                if(int(entry[3])>0):
                
                    doc.writelines(f'{entry[0]},present\n')
                else :
                    
                    doc.writelines(f'{entry[0]},late\n')

def soting():
    df=pd.read_csv("present.csv")
    sorted_df = df.sort_values(by=["name"], ascending=True)
    sorted_df.to_csv('present.csv', index=False)
