
# coding: utf-8

# In[28]:


# Load data
import numpy as np
from sklearn import datasets
iris = datasets.load_iris()
iris_X = iris.data
iris_y = iris.target

print(iris.feature_names)
print(iris.target_names)
print(np.unique(iris_y))


# In[29]:


# Visualize data
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
X = iris.data[:, :2]  # we only take the first two features.
y = iris.target
x_min, x_max = X[:, 0].min() - .5, X[:, 0].max() + .5
y_min, y_max = X[:, 1].min() - .5, X[:, 1].max() + .5


# In[30]:


# Plot the training points
plt.figure(2, figsize=(8, 6))
plt.clf()
plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Set1, edgecolor='k')
plt.xlabel('Sepal length')
plt.ylabel('Sepal width')
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.xticks(())
plt.yticks(())
plt.show()


# In[31]:


# Plot the distribution in boxplot
plt.boxplot(iris.data)
plt.xlabel('Features')
plt.ylabel('Cm')
plt.show()


# In[32]:


# KNN Classification
# shuffle the data
np.random.seed(0)
indices = np.random.permutation(len(iris_X))
# Split iris data in train and test data
# A random permutation, to split the data randomly
iris_X_train = iris_X[indices[:-10]]
iris_y_train = iris_y[indices[:-10]]
iris_X_test  = iris_X[indices[-10:]]
iris_y_test = iris_y[indices[-10:]]


# In[33]:


# Create and fit a nearest-neighbor classifier
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier()
knn.fit(iris_X_train, iris_y_train) 


# In[34]:


# Do prediction on the test data
knn.predict(iris_X_test)
print iris_y_test


# In[35]:


# KNN Visualization.
n_neighbors = 5
h = .02 # step size in the mesh


# In[36]:



# Create color maps
from matplotlib.colors import ListedColormap
cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA', '#AAAAFF'])
cmap_bold = ListedColormap(['#FF0000', '#00FF00', '#0000FF'])


# In[37]:


# for weights in ['uniform', 'distance']:
#     # we create an instance of Neighbours Classifier and fit the data.
#     knn = KNeighborsClassifier(n_neighbors, weights=weights)
#     knn.fit(X, y)
#     # Plot the decision boundary. For that, we will assign a color to each
#     # point in the mesh [x_min, x_max]x[y_min, y_max].
#     xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
#                          np.arange(y_min, y_max, h))
#     Z = knn.predict(np.c_[xx.ravel(), yy.ravel()])
#     # Put the result into a color plot
#     Z = Z.reshape(xx.shape)
#     plt.figure()
#     plt.pcolormesh(xx, yy, Z, cmap=cmap_light)
#     # Plot also the training points
#     plt.scatter(X[:, 0], X[:, 1], c=y, cmap=cmap_bold,
#                 edgecolor='k', s=20)
#     plt.xlim(xx.min(), xx.max())
#     plt.ylim(yy.min(), yy.max())
#     plt.title("3-Class classification (k = %i, weights = '%s')"
#             % (n_neighbors, weights))


# In[38]:


### TODO: explore the effects for different Ks.
for n_neighbors in [5,8,25,100]:
    for weights in ['uniform', 'distance']:
        # we create an instance of Neighbours Classifier and fit the data.
        knn = KNeighborsClassifier(n_neighbors, weights=weights)
        knn.fit(X, y)

        # Plot the decision boundary. For that, we will assign a color to each
        # point in the mesh [x_min, x_max]x[y_min, y_max].
        xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                         np.arange(y_min, y_max, h))
        Z = knn.predict(np.c_[xx.ravel(), yy.ravel()])

        # Put the result into a color plot
        Z = Z.reshape(xx.shape)
        plt.figure()
        plt.pcolormesh(xx, yy, Z, cmap=cmap_light)

        # Plot also the training points
        plt.scatter(X[:, 0], X[:, 1], c=y, cmap=cmap_bold,
                edgecolor='k', s=20)
        plt.xlim(xx.min(), xx.max())
        plt.ylim(yy.min(), yy.max())
        plt.title("3-Class classification (k = %i, weights = '%s')"
              % (n_neighbors, weights))
    

plt.show()


# In[13]:


# plt.show()


# In[14]:


### TODO: explore the effects for different Ks.




""" Part 3 """
from sklearn import svm
svc = svm.SVC(kernel='poly')
svc.fit(iris_X_train, iris_y_train)  
svc.predict(iris_X_test)
print iris_y_test


# In[40]:


### TODO: get the SVC visualization for different kernels.
from sklearn.svm import SVC
def variationOfkernal(kernel):
    # KNN Visualization.
    h = .02  # step size in the mesh

    # Create color maps
    from matplotlib.colors import ListedColormap
    cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA', '#AAAAFF'])
    cmap_bold = ListedColormap(['#FF0000', '#00FF00', '#0000FF'])

    for weights in ['uniform', 'distance']:
        # we create an instance of Neighbours Classifier and fit the data.
        svc = SVC(kernel=kernel)
        svc.fit(X, y)

        # Plot the decision boundary. For that, we will assign a color to each
        # point in the mesh [x_min, x_max]x[y_min, y_max].
        xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                             np.arange(y_min, y_max, h))
        Z = svc.predict(np.c_[xx.ravel(), yy.ravel()])

        # Put the result into a color plot
        Z = Z.reshape(xx.shape)
        plt.figure()
        plt.pcolormesh(xx, yy, Z, cmap=cmap_light)

        # Plot also the training points
        plt.scatter(X[:, 0], X[:, 1], c=y, cmap=cmap_bold,
                    edgecolor='k', s=20)
        plt.xlim(xx.min(), xx.max())
        plt.ylim(yy.min(), yy.max())
        plt.title("3-Class classification KERNEL="+kernel)
    plt.show()


variationOfkernal('linear')
variationOfkernal('rbf')
variationOfkernal('poly')


# In[ ]:





# In[ ]:




