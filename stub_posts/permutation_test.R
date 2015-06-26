library(VGAM)


# generate two distinct pareto distributions

dpareto <- function(x, a=0.5, b=1) a*b^a/x^(a+1)
ppareto <- function(x, a=0.5, b=1) (x>b)*(1-(b/x)^a)
qpareto <- function(u, a=0.5, b=1) (b/1-u)^(1/a)
rpareto <- function(n, a=0.5, b=1)(qpareto(runif(n),a,b))

# uniform 5% convert to sales
# of that 5%, the purchases then follow a Pareto distribution
# consider sales data from two different regular process
test <- round(rpareto(1000, a=0.25, b=1)*100 + 10 )
control <- round(rpareto(1000, a=0.2, b=1)*100 + 10 )

plot(test, xlab='test')
plot(control, ylab='control')
hist(test)
hist(control)

df <-cbind(test,control)
boxplot(df)

# more variability in th
pareto.mean = NULL
for (i in 1:1000 ) {
  pareto.mean[i] = mean(rpareto(1000))
}

# t-test

# permutation test

# bootstrap test


# examination 
