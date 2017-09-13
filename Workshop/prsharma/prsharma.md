## Workshop


### Explore the effects for different K in K Nearest Neighbor classification
The three variations with k = 5,15,30 are in the images : prsharma_Part2_K5.png,prsharma_Part2_K15.png,prsharma_Part2_K30.png 


### Explain how we should choose K.
In KNN, k is usually chosen as an odd number if the number of classes is 2.A small value of k means that noise will have a higher influence on the result. A large value make it computationally expensive and kind of defeats the basic philosophy behind KNN (that points that are near might have similar densities or classes ) .A simple approach to select k is set  k=\sqrt{n} where is number of instances

### Explore different kernels of Support Vector Machine.
Plot of different kernels is in the image: prsharma_Output_SVM_multiple_kernels.png

### Explain how we should choose the kernel.
n -> features and 
m -> total training datapoints

* If n is relatively larger than m (like for text classification), then LR and linear SVM (with linear kernel ) can be used and both have similar complexity.
* If n is small and m is intermediate(just enough to make the modeling) , then SVM with kernel like Gaussian kernel provides better results and will be a bit harder to work on than LR.
* If n is small and m is very large, then this tend to underfit the test data. So gather additional features or add polynomial features to make it close to our 1st case and use LR or linear SVM
* If n is very large and m is small, then this tend to overfit the data. So we try to remove correlations between features, remove non-significant features, gather more datasets for training or use regularisation. Eventually we again endup with 1st case and use LR or Linear SVM.
