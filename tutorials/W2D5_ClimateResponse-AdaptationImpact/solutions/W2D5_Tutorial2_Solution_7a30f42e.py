
# Generate 100 numbers from a Gaussian distribution with zero mean
x_1_test1 = np.random.randn(data_points)
x_2_test1 = np.random.randn(data_points)

# Create an array of x values
regressors_test1 = np.array([x_1_test1, x_2_test1])

#Assuming the same relationship of alpha =.5 and beta = .1 as set above,calculate the true y values:
y_test1 = y_func(np.array([alpha,1-alpha]),regressors_test1, beta)

# Use the logistic regression model to make predictions on the new x values
preds = logreg_model.predict(regressors_test1.T)

# Calculate the confusion matrix for the model's predictions
cm = confusion_matrix(y_test1, preds)

# Visualize the confusion matrix as an image with labeled ticks
plt.imshow(cm); plt.xticks([0,1]); plt.yticks([0,1])
plt.ylabel('true category'); plt.xlabel('predicted category')
plt.colorbar()

# Print the percent of correct predictions by the logistic regression model
'Percent correct is ' + str(100*logreg_model.score(regressors_test1.T, y_test1))