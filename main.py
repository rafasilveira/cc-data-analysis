from os import listdir
from os.path import isfile, join

print('💰 Credit Card data analyzer')
try:
  files = [f for f in listdir('input') if isfile(join('input', f))]
  if not files:
    raise('')
except:
  print('No data found! 👀 ')
  print('Please create a input directory and place your files inside, as described in the README')
  quit()


csvs = sorted([f for f in files if f.split('.')[-1] == 'csv'])

if len(csvs) > 1:
  print('Joining CSV files... 🙄')

  with open('temp.csv', 'w+') as tmp:

    tmp.write('date,category,title,amount\n')

    for item in csvs:
      print(f'joining {item}')
      with open(f'input/{item}', 'r') as csv:
        csv.readline() # ignore header
        for line in csv:
          tmp.write(line)
        csv.close()
        tmp.write('\n')
    print(f'finished joining files 👍')
    tmp.close()
      
        





