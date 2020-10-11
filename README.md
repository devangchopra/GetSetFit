# GetSetFit  
Go click pic and eat

GetSetFit application is aimed to assist the people with regard to their fitness, daily diet, monitoring the intake of calories, proteins, carbohydrates, fat and fibre.  
Just on single click user can upload the the image of his diet and our application will use machine learning model to to find the item and will prepare the report of all calories, proteins,carbohydrates, fat and fibre intake and will also tell the required amount by person in accordance with his or her BMI.

Link for model checkpoints: https://drive.google.com/drive/folders/1hROz-dhJrXPrl8bAnqthIledLCRrXgUp?usp=sharing

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
### Formulas used: 
```python
BMI -- weight/(height*height)

Men_BMR = 66.4730 + (13.7516 x weight in kg) + (5.0033 x height in cm) – (6.7550 x age in years)

Women_BMR = 655.0955 + (9.5634 x weight in kg) + (1.8496 x height in cm) – (4.6756 x age in years)
```
### The parameters for training models are:
1. Learning Rate: 0.0001
2. Optimizer: Adam
3. Loss function: sparse_categorical_crossentropy
4. Activation function: Relu, Softmax
5. Layers used are: Dense, Dropout, GlobalAveragePooling2D, Flatten, Conv2D, MaxPooling2D

### Advantage and Problem solved:





## Future Scope of the Project:


In future we can train the machine learning model with more number of images so that the prediction accuracy of the model improves. Currently we can classify the foods in 7 categories but later on we can use more data and computational power to train a better model which can classify foods into various other categories. User can have his own dieting history in the profile panel which can help him judge his own past performace. With the help of proper of dietician we can have three major diet plans of reducing weight , gaining weight and mainting the current phsique in the future.



## Buisness Aspects:



This website/software can generate revenue through these models.

### Model 01:
#### (Subscription Model)

We can make user pay for the service. Standalone user can register in our application to track their dieting activities. They will be provided with zero advertisement experience and they can choose from the available dieting plans we have or else can simply use our application for tracking and judging their calorie intake. People with obese condition, or people who are looking to gain weight and the gym freaks or physically fit people will be the target group for this category.



### Model 02:
#### (Advertisement Model)


The user will be given the same priviliges as in model 01 but the advertisement will be shown to this category user. User in this category will also be a standalone user and he will be shown with the advertisement of health cauntious brands, gym brands, dieticians in the location near him and also the restaurants who offer diet food. 


### Model 03: (-----> Main  <-----)
#### (Software as a service Model)


The software or website will be given as a service to various dieticians to track their patients growth and improvement. Dietician can look at the consumed diet of their patients regularly without physically meeting them. Dieticians can provide their diet plans or suggestion to particular patients through our portal. We will use django-tenant-model to register every dietician  as a tenant and every tenant will have his/her private patients. This dieticians will be asked to pay for our service.



## Problems Solved:

#### 1) Dietician Errors are removed :-->  During weekly or mothly meet patient might not be able to remember his exact meal. Our website will be useful in removing the human errors or confusion regarding this diet. No manual records and growth can be tracked.


#### 2) Dietician can customise for each user :---> Dietician can recommend or give the customised diet plans to every patient on judging him on the basis of his calorie intake in past, or according to his calorie intake in differnet seasons.


#### 3) User can Contact Dietician :--> If needful user can contact the dietician remtely for asking suggestions or for consultancy.

#### 4) Spreading health awareness :--> Through the free version of this application we will be spreading health awareness of the various sections of the society.


#### 5) Reduced medical fees for diet plans :-- As a single dietician can handle various patients simultaneously, the cost of consulting a dietician also reduces gradually.


## Challanges we ran into:


#### 1) Poor classification due to less time for training model



#### 2) Deployment issues due to lack of knowledge


#### 3) Designing database schema before implementation.

