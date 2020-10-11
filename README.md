# GetSetFit  

GetSetFit application is aimed to assist the people with regard to their fitness, daily diet, monitoring the intake of calories, proteins, carbohydrates, fat and fibre.  
Just on single click user can upload the the image of his diet and our application will use machine learning model to to find the item and will prepare the report of all calories, proteins,carbohydrates, fat and fibre intake and will also tell the required amount by person in accordance with his or her BMI.

## Discription and Methodology:
We had trained the multi-class Classifier using Convolution Neural Networks over 7 broad categories: Roti, Bread, Yellow-daal, Rice, Boiled-Egg, omlet, chai.
further on getting more time we could scale it at as many items as we want and could give sufficient time to train our model.  
What it does is :- In this application user is just required to scan their food and upload it . After that the trained machine learning model will predict the food item and will provide you the calories,protein ,carbohydrates,fats,fibre of that food item and will maintain your chart for whole day.  
Our app at starting calculates BMI of person and sets the initial status for the person just by using simple universal logics. like:  

```python
If BMI > 18.5 and BMI <= 24.9
   Status =Normal
   Solution = Maintenance
```
Formulas used: 
```python
BMI -- weight/(height*height)

Men_BMR = 66.4730 + (13.7516 x weight in kg) + (5.0033 x height in cm) – (6.7550 x age in years)

Women_BMR = 655.0955 + (9.5634 x weight in kg) + (1.8496 x height in cm) – (4.6756 x age in years)
```
The parameters for training models are:
1. Learning Rate: 0.0001
2. Optimizer: Adam
3. Loss function: sparse_categorical_crossentropy
4. Activation function: Relu




| Tables        | Are           | Cool  |
| ------------- |:-------------:| -----:|
| col 3 is      | right-aligned | $1600 |
| col 2 is      | centered      |   $12 |
| zebra stripes | are neat      |    $1 |
