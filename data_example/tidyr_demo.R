
# Ch.12: tidy data

rm( list = ls() )

library(tidyverse)


d0 = readr::read_csv("PWT100.csv", col_names = TRUE)
head(d0)
colnames(d0)

arrange(d0, year)


# work with a smaller dataset

d1 <- select(d0, countrycode, year, rgdpe, pop) %>%
  filter(countrycode %in% c("CHN", "RUS", "JPN", "USA")) %>%
  mutate(gdpc = rgdpe/pop)
  

d1 %>% 
  ggplot() + 
  geom_point(mapping = aes(x = year, y = rgdpe, color = countrycode))



s1 <- d1 %>% 
  select( countrycode, year, pop) %>%
  spread( key = year, value = pop)


g1 <- s1 %>% gather('1950':'2019', key = "year", value = "pop")



######################

# load("data_example/big150.Rdata")
load("big150.Rdata")


big150_1 <- big150 %>% select(typb, b1, b1_c) %>%
            gather("b1", "b1_c", key = "estimator", value = "value")
print(head(big150_1))




p1 <- ggplot(big150_1)
p1 <- p1 + geom_area(
  stat = "density", alpha = .25,
  aes(x = value, fill = estimator), position = "identity"
)
p1 <- p1 + facet_grid(. ~ typb)
p1 <- p1 + geom_vline(xintercept = 0)
p1 <- p1 + theme_bw()
p1 <- p1 + theme(
  strip.text = element_text(size = 12),
  axis.text = element_text(size = 12)
)
print(p1)

