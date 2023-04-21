# play with data for summary
# `dplyr`
# related chapters:


# Ch.10: tibbles
# Ch.11: data import
# Ch.5:  data transformation
# Ch.18: pipes


rm( list = ls() )

library(tidyverse)

# `readr` packages has more flexible functions to import data
d0 = readr::read_delim("bank-full.csv", delim = ";", col_names = TRUE,
                       col_types = cols(
                         age = "i",
                         job = "c",
                         marital = "f",
                         education = "f",
                         balance = "i",
                         )
                       )

head(d0)
colnames()

# select columns
d1 = select(d0, age:loan)
head(d1)

# select a subset by conditions
filter(d1, job == "blue-collar", age > 50) 
filter(d1, job == "blue-collar", (age > 20 & age <= 30) ) 

# (re)arrange rows
arrange(d1, age, education)
arrange(d1, desc(age), education)

# add generated columns (last column)
mutate(d1, edu_f = as.numeric(education) )
transmute(d1, 
          age = age,
          marital = as.numeric(marital), 
          education = as.numeric(education))

########### Summarize #################

# overall mean balance 
summarize(d1, mean_b = mean(balance))

# mean balance by groups
group_by(d1, education) %>%
  summarize( mean_b = mean(balance))

d1 %>%
  group_by(education, marital) %>%
  summarize( mean_b = mean(balance),
             sd_b = sd(balance),
             count = n())

