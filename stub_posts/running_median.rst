if you've ever spent a lot of time mucking around a in DB or stuff like that may. It's worse!



Here's a quick method for calculating median and variance of a dataset.

=== variance
The usual way to calculate variance is not numerically stable i.e.

well sigma is given by

\sigma = (\xbar^2) - \xbar^2 = sum^N_{i=1} x^2_i - ((\sum^N_{i=1} x_i)^2 /N) /N

there's lots of pedantry about N vs N-1 (called Bessel's correct, and is unbiased estimator for )

This is bad because we get "catestrophic cancellation".

=== median

This is apparently a classic interview question heaps

unfortunately this require everything to be in memory, so wouldn't be great for truly enormous datasets. On the otherhand I've never had problem

Note in general, this is not actually particularly easy!
