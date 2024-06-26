import csv

# opening the CSV file
i=0
Dates=[]
Category=[]
Descript=[]
DayOfWeek=[]
PdDistrict=[]
X=[]
Y=[]

uDates=[]
uCategory=[]
uDescript=[]
uDayOfWeek=[]
uPdDistrict=[]
uX=[]
uY=[]



x=[]
y=[]

with open('train.csv', mode ='r')as file:
# reading the CSV file
    csvFile = csv.reader(file)
    # displaying the contents of the CSV file
    for lines in csvFile:
        if i!=0:
            # print(lines)
            Dates.append(lines[0].split(' ')[0])
            if lines[0].split(' ')[0] not in uDates:
                uDates.append(lines[0].split(' ')[0])
            Category.append(lines[1])
            if lines[1] not in uCategory:
                uCategory.append(lines[1])
            Descript.append(lines[2])
            if lines[2] not in uDescript:
                uDescript.append(lines[2])
            DayOfWeek.append(lines[3])
            if lines[3] not in uDayOfWeek:
                uDayOfWeek.append(lines[3])
            PdDistrict.append(lines[4])
            if lines[4] not in uPdDistrict:
                uPdDistrict.append(lines[4])
            X.append(lines[7])
            if lines[7] not in uX:
                uX.append(lines[7])
            Y.append(lines[8])
            if lines[8]  not in uY:
                uY.append(lines[8])
            x.append(uDates.index(lines[0].split(' ')[0]))
            y.append(uCategory.index(lines[1]))
        i=i+1
        if i==50001:
            break

# Dates
print("Dates")
# Dates_list_set = set(Dates)
# Dates_unique_list = (list(Dates_list_set))
print(Dates)
print(len(Dates))
print(uDates)
print(len(uDates))

# Category
print("Category")
# Category_list_set = set(Category)
# Category_unique_list = (list(Category_list_set))
print(Category)
print(len(Category))
print(uCategory)
print(len(uCategory))



print(x)
print(y)


dict={}
for i in uDates:
    dict[str(i)]={}

for i in range(0,len(Dates)):
    if Category[i] not in dict[str(Dates[i])].keys():
        dict[str(Dates[i])][Category[i]]=0
    dict[str(Dates[i])][Category[i]]+=1

for i in dict:
    print(i)
    print(dict[i])



import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import LSTM, Dense

for cat in uCategory:
    # try:
        print("================================")
        print("================================")
        print("================================")
        print(cat)
        x=[]
        y=[]
        for i in range(len(uDates)):
            try:
                x.append(i+1)
                y.append(dict[str(uDates[len(uDates)-i-1])][cat])
            except:
                y.append(0)

            # data = pd.read_csv('data.csv')
        data = np.array(y)
        print(data)
        print(type(data))
        print("<class 'numpy.ndarray'>")

        # Normalize the data
        scaler = MinMaxScaler()
        data = scaler.fit_transform(data.reshape(-1, 1))

        # Split the data into training and testing sets
        train_size = int(len(data) * 0.8)
        train_data, test_data = data[:train_size], data[train_size:]

        # Create sequences for the LSTM-LR model
        def create_sequences(data, look_back):
            X, y = [], []
            for i in range(len(data) - look_back):
                X.append(data[i:i+look_back])
                y.append(data[i+look_back])
            return np.array(X), np.array(y)

        look_back = 5  # You can adjust this parameter to change the sequence length
        train_X, train_y = create_sequences(train_data, look_back)
        test_X, test_y = create_sequences(test_data, look_back)

        # Build the LSTM model
        model = Sequential()
        model.add(LSTM(units=50, input_shape=(look_back, 1)))
        model.add(Dense(1))
        model.compile(optimizer='adam', loss='mean_squared_error')

        # Train the model
        model.fit(train_X, train_y, epochs=100, batch_size=64)

        # Make predictions
        train_predict = model.predict(train_X)
        test_predict = model.predict(test_X)
        print(test_predict)

        # Inverse transform the predictions to original scale
        train_predict = scaler.inverse_transform(train_predict)
        test_predict = scaler.inverse_transform(test_predict)

        # Plot the results
        plt.figure(figsize=(12, 6))
        plt.plot(np.arange(0, len(train_data)), scaler.inverse_transform(train_data), label='Training Data')
        plt.plot(np.arange(len(train_data), len(train_data) + len(test_data)), scaler.inverse_transform(test_data), label='Testing Data')
        plt.plot(np.arange(look_back, look_back + len(train_predict)), train_predict, label='Training Predictions')
        plt.plot(np.arange(len(train_data) + look_back, len(train_data) + look_back + len(test_predict),), test_predict, label='Testing Predictions')
        plt.xlabel('Time')
        plt.ylabel('Value')
        plt.legend()
        plt.show()
        print("******************************************************")
        print("******************************************************")
        print(test_predict)
        print("******************************************************")
        print( test_y)
        print("******************************************************")
    # except:
    #     pass
