import sys
sys.path.insert(0, './app')
from app.Application import Application

app = Application()
app.log('2019-07-15_data.json').classifier('WordPress').process().toCsv()
