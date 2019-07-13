# Youtube Videos Categorization based on Description
## Project Aim:-
To develop the machine learning model that can predict the category of video(travel vlog/food vlog/history/manufacturing/science n tech) on youtube with the help of description provided by the creator of that video.
## IDE USED -  
* pycharm(for scraping)
* jupyter notebook(for preprocessing and developing model)

### LANGUAGE USED -   
Python(version 3.7)

## LIBRARIES USED – 
* selenium(for scraping)
* pandas,numpy,nltk,sklearn(for model)

## Procedure:-
### For data collection-
* 1. As we have to train our model to predict the category of video from description hence it must be trained on the same type of data.Hence firstly we have to create our own dataset .
* 2. For scraping the data ,we will use selenium library so that we can easily scrap the video details (selenium mainly because the youtube pages are dynamically loaded means u scroll down n new videos appear hence no fixed length of page).
* 3. Firstly category is putin search bar so that all realted videos appear then Using selenium we sracp details of videos like video ID,Video Title,Description,And category of that video(that we put in search bar).
* 4. These all details are then put in one single csv file which will be used to train the model.
### For Developing Model:-
* 1. Numpy and pandas are imported for some required preprocessing and dataframe.
* 2. As the differnce bw no. of videos for each category is high hence it is reduced to small diffence so that model is not biased.
 
![image](https://user-images.githubusercontent.com/46081301/61169061-417d5400-a575-11e9-9352-69ee851d0810.png)

* 3. Feature variable(description) values are stored in X variable and target values(category) in Y variable.
* 4. Then we import nltk functions to preprocess the description of the videos (removing stopwords,punctuations ,not ASCII chacarcters,emails,websites,phone no.,money symbols and all other stuff that does not required).
* 5. Then we tokenize words and put them in the dictionary along with value True for all word sin dictionary only if words are not in stopwords and (doesnot start with “//” (part of preprpcessing)).
* 6. Dictionary is made so that it can be feed to naivebyes algo provided by nltk itself and it accepts dictionary format only.
* 7. Data is split into training and testing with test_size = 0.20.
* 8. Naive byes is imported from nltk(read about this..coz some differneces from normal naivebyes) and the model is trained on the training data(there is no y_train because the format of dictionary is like {{word1:true,woed2:true,….}:category1},{same as first with its category}{cate3}…}hence categories are also included in the dictioanry.Hnece data is only divided into train,test.
* 9. Accuracy of model is tested and it comes out to be around 88%.
* 10. Some random descriptions are also feeded to test the model and it correctly predict the category.
