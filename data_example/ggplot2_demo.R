rm( list = ls() )

library(tidyverse)
library(ggplot2)
# AJR = read.csv("data_example/AJR.csv", header = TRUE)
d0 = read.csv("AJR.csv", header = TRUE)

#############
# "avexpr: average protection against expropriation risk
# "logpgp95": logarithm of GDP per capita in 1995

ggplot(data = d0) + geom_point(mapping = aes(x = avexpr, y = logpgp95))


##############################
bank_0 = read.csv("bank-full.csv", header = TRUE, sep = ";" )
bank_0$y01 = (bank_0$y == "yes")

# scatter plot
p1 <- ggplot(data = bank_0) + geom_point(mapping = aes(x = age, y = balance))
print(p1)

# scatter plot with groups
p2 <- ggplot(data = bank_0) + geom_point(mapping = aes(x = age, y = balance, color = education, alpha = 0.5))
print(p2)

p3 <- p1 + facet_wrap( ~ education)
print(p3)

# educational levels in each ago
ggplot(data = bank_0) + geom_bar(mapping = aes(x = age, fill = education))
p4 <- ggplot(data = bank_0) + geom_bar(mapping = aes(x = age, fill = education), position = "dodge")
print(p4)

p5 <- p4 + coord_flip()
print(p5)
