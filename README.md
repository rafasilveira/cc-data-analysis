# CC Data Analysis

## About
How much do I spend? Where is my money going? How is my financial habits changing through time?
> ⚠️ **disclaimer**: this is a work in progress

## What's inside
- [x] Read CSV files
- [x] Create aggregated CSV
- [x] Store data in a sqlite database
- [ ] Do some data analysis
- [ ] Match credit card expenses with account statement
- [ ] Create markdown report

## How to use
I have Nubank. Things will be easier if you use it too. If you don't, you might have to do some parsing beforehand.

- Create a directory called `input`
- Paste your csv files there
- Install dependencies
- `python3 main.py`

### Dependencies
- unidecode `pip3 install unidecode`
- matplotlib `pip3 install matplotlib`

### Nubank
Nubank provides monthly credit card csv files. Go to the web page and manually download a file for each month.
> Disclaimer: I have contacted the customer support. Currently, this is the only way.

In the future, I plan to combine the data with my account statement, just because. You can get a `.pdf` and a `.ofx` file via chat.

### Other banks
You have to create a input csv file that looks like this.
```
date,category,title,amount
2017-07-21,eletrônicos,Gilmar Rodrigues,120
2017-07-21,restaurante,Hamburgueria Juventus,20
2017-07-24,saúde,Panvel Filial,30.34
```
