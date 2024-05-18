from tensorflow import keras 
 
# Kaydedilen modeli yükleyin
loaded_model = keras.models.load_model("C:/Users/caner/Project/IOT/iot/raspberry/iot_train.h5")

test_x = [[
    [14.0,  22.9, 90.0,  71.4],
    [14.1, 22.9, 90.4, 71.4],
    [14.3, 22.9, 89.7, 71.5],
    [14.0,  22.9, 90.0,  71.4],
    [14.1, 22.9, 90.4, 71.4],
    [14.3, 22.9, 89.7, 71.5],
    [14.0,  22.9, 90.0,  71.4],
    [14.1, 22.9, 90.4, 71.4],
    [14.3, 22.9, 89.7, 71.5],
    [14.0,  22.9, 90.0,  71.4] 
    ]] 

y_pred = loaded_model.predict(test_x)
print(y_pred)