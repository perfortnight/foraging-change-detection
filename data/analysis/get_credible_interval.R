library("BayesianFirstAid")
#print("hello",quote=FALSE)
args <- commandArgs(trailingOnly = TRUE)
print(args)
scores <- read.csv(args[1],sep=" ")

uniform <- scores$uniform
foraging <- scores$foraging

#print(scores)
#print(uniform)
#print(foraging)

fit <- bayes.t.test(uniform,foraging,paired=TRUE)
plot(fit)
