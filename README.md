# Machine Learning Handling Categorical Feature Using Python Project 2:

• Handling Categorical Feature is the crucial step in making a ML model.

• If there is no Handling of Categorical Feature step on the data, your ML model won't work properly.

|Language Used: | Python |
|--- |--- |

|IDE Used: | PyCharm |
|--- |--- |

Handling Categorical Feature / Pre-processing steps required to prepare any dataset on which we will build our ML model.

## Get the Dataset:

The first step is always to get the dataset and try to understand dataset. Try to figure out what all are independent variables and what are dependent variables. In Machine Learning, some independent variables are used to predict a dependent variable.

## Importing the Libraries:

Importing following essential libraries

•	Pandas -> to import the dataset and manage the dataset

•	Sklearn -> it features various classification, regression and clustering algorithms

## Import the Dataset:

The name of the dataset I have used for this project is 'Startup_Profit.csv'.

Dataset contains five columns -> R&D Spend, Administration, Marketing Spend, State, Profit. The shape of our dataset is (50, 5).

Dataset contains information of startups expense and profit. 

First three columns are information of expenses like R&D Spend, Administration and Marketing Spend. Fourth column shows the State of startup and fifth column tells us about overall profit margin.

In Startup_Profit.csv, first four columns i.e. R&D Spend, Administration, Marketing Spend, State are independent variables whereas fifth column Profit is dependent variable.

## Handle Categorical Feature / Data:

Your dataset may contain quantitative and qualitative variables. Quantitative variables contain numeric values whereas qualitative variables contain the categories or levels within the data.

Machine Learning models are based on mathematical equations, so it would cause some problem if we keep the text and use categorical variables in the equation because ML Model want only numbers in the equations. That's why we need to encode categorical variables.

In 'Startup_Profit.csv', State is a categorical variable because it simply contains categories.

• State variable contains three different categories - New York, California and Florida

In Python, there are two ways of doing this:
   1. Using Pandas Library
   2. Using Sklearn Library

If you are using pandas you have to create dummy variable and if you are using sklearn you have to use LabelEncoder and OneHotEncoder.

Python will give levels to these categories and the order of those levels is not important. But we have to prevent ML equations from thinking one level is greater than other or vice versa. To prevent this, we use dummy variables. So, for example, for State column, instead of having one column we will have 2 columns (n-1). This can be achieved with the help of get_dummies() in pandas and OneHotEncoder class in sklearn.

In this project I have used pandas.

## Matrix of Dependent and Independent Variables:

In Python, you have to create two matrices for independent variables and dependent variable.

Hence for Startup_Profit.csv, create one matrix for four independent variables and then create one matrix dependent variable.

## Split the Dataset into Training Data and Test Data:

ML is about a machine that is going to learn from the data to make predictions.

We need to split the dataset into training set and test set. Using training set, we build the machine learning model and using test set, we test the performance of this machine learning model.

We are building our ML model on training set by establishing some correlation between independent variables and dependent variables and once the ML model understands the correlation between independent variables and dependent variables. We will test if the ML model can apply the correlations you understood based on training set on test set.

In brief, we have to make two different datasets. The training set on which the machine learning model learns and test set on which we test if the ML model learned correctly the correlations.

In Python, model_selection class from scikitlearn library is used to split the dataset into training and test set.

In this project, I have given 75% of data for training and 25% of data for testing.

## Applying Linear regression:

Linear regression is perhaps one of the most well-known and well-understood algorithms in statistics and machine learning. Linear regression is a linear approach to modeling the relationship between a scalar response (or dependent variable) and one or more explanatory variables (or independent variables).

## Accuracy Score:
In this project we have achieved an accuracy of 92% (0.9259600592002034)
