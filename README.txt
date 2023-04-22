Run the K-nearest neighbours algorithm like this
python3 knn.py mushtest.csv <k> <num_of_test_points>
number of test points must not exceed 3000
num_of_test_points must be less or equal than the number of lines you have in file mushtest.csv
file mushtest.csv can be named whatever you want, it contains the data points to test on along with their correct answers.

This algorithm runs pretty slowly. Because of the way I used selection sort.
200 test points takes about 5 minutes.


Run the Support Vector Machine program like this
python3 svm.py

it will output the accuracy scores of each SVM model using different kernels.
