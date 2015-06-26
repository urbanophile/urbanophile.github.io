From time to time I need to clustering, and after k-means, hierarchical clustering is one of the most popular ways to do this. There are a number of popular implementations,
* scikit-learn
* scipy
* pycluster
but I'll covers scipy because here because scipy
    a) default tool when doing stuff in python, and
    b) I find the documentation very frustrating.

We're all sick of looking sepal width measurements, let's look at human tumor microarray data as described in Elements of Statistical learning. This should also allow you to compare the . A nice thing about this is that we will beable to

here's what were going to cover
* fit a good model
* choose k
* make a nice dendrogram
* assess fit
*

=== Dataset

The data is from a highlighly cited 2000 nature paper and consists of
http://genome-www.stanford.edu/nci60/

==== Methods


Choose a nice
* fit good model

agglomerate vs. divisive clustering? Just pick agglomerative. Brief research indicates to me that there isn't really much difference between the two


=== How do you pick k?

If you don't know, you're going to have to pick a heuristic answer. Here's 3 quick answers:
- sqrt(n)
- look at k which minimises intercluster difference (elbow method)
-

There are many, many other methods. Silhouette comes to mind, minimising is CV error is another.  Long list from stack overflow is
* choose k

There's no good method to choose k. The paper where Tishbani et al. introduce hierarchical clusteirng


* make a nice dendrogram
* assess fit



=== Further reading
k-means (the grandaddy)
gaussian mixture model
- densisty clusterings
- propagation affinity clustering
- dbscan

clustering time series
- this seems to be an
