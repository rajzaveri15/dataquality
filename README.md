# dataquality
Assessing Data Quality with Python

#### Project Overview
In this project, I got a chance to work with a new python library that I discovered called ‘great_expectations’. ‘great_expectations’ allows you to assess your data quality to ensure all the values make sense and are appropriate. For example, number of years or someone’s age cannot be below 0. This library helps ensure values such as those. In this project I made certain assessments on a dataset contain fitness activities data to see if there were any values that were inaccurate or maybe even impossible. 

#### Dataset overview 
The dataset consists of approximately 500 records with 84 different columns or attributes. The ones that I used in this project include Activity ID (IDs), Max Speed, and Activity Type. 

#### Installing ‘great_expectations’ Library

```python
!pip install great_expectations
```

#### Loading in the Dataset into a Dataframe
```python
import great_expectations as ge
df = ge.read_csv('activities.csv')
```
Instead of using the traditional pandas library that I normally use, I used great_expectations to create the dataframe.

#### Is Activity ID Unique?
```python
df.expect_column_values_to_be_unique(column="Activity ID")
```
The first thing I wanted to check in this database is to see if all the Activity IDs were unique as they should be.

![Screenshot (136)](https://user-images.githubusercontent.com/114118047/192682606-6adfac4b-b4ff-46e2-a4d4-4a316b5eddd5.png)

The results came back positively and successfully. The were no duplicate IDs.

#### Is the activity type one of the following: Bike, Hike, Walk, Run?
The next attribute to evaluate is the activity type. The activity type has to be one of the following: Bike, Hike, Walk and Run. If it is anything other than these four values then it has to be fixed.
```python
# Is the activity type one of the following?
# Bike Hike Walk Run 
activities = ['Run', 'Hike', 'Walk','Bike']
df.expect_column_values_to_be_in_set('Activity Type',
        value_set = activities)
```
![Screenshot (137)](https://user-images.githubusercontent.com/114118047/192682885-78b264ca-2b0c-46e8-8818-2d109eb6f597.png)

The results here shows that there were some records with the value ‘Ride’ instead of on of the four acceptable ones. The assumption here is that they are supposed to be ‘Bike’. In that case, the values would need to be changed to ‘Bike’.

#### Is the Max Speed between 0 and 12 mph?
The last attribute I explored was the Max Speed. The maximum someone should usually be able to go while running, walking, or biking is around 12 mph. Along with that, someone’s speed cannot be negative. Therefore, the max speed has to be between 0 and 12. Otherwise there is a potential mistake in the data.
```python
df.expect_column_values_to_be_between('Max Speed',0,12)
```
![Screenshot (138)](https://user-images.githubusercontent.com/114118047/192683007-508569e6-b735-4c70-b0c5-6c01025b8dde.png)

This test did not go smoothly either. There were values that were much higher than 12. One of them including around 34 mph. This is a clear error in the accuracy or the collection of data. 

#### Conclusion
As I had expected, there were some quality issues with this data. Some of the values in the Maximum speed column were highly inaccurate and some of the values in the activity type field need to be changed to fit the accepted values. These changes need to be done before the data can be further used for analysis. 

Although this project was different from any of the traditional data analysis projects, checking and ensuring data quality is an important part of the data analysis process. This project allowed to discover and play with the ’great_expectations’ library in python and gain a new skill. My plan is to continue using this library in the future starting with continuing the assessment on this dataset itself.


