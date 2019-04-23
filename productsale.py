
import pandas as pd

dataPath = './Data/'

# Load json data to dataframe
data = pd.read_json(dataPath+'20190207_transactions.json', orient='columns', lines=True)





