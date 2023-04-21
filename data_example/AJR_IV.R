rm( list = ls() )

# AJR = read.csv("data_example/AJR.csv", header = TRUE)
d0 = read.csv("AJR.csv", header = TRUE)



d1 = d0[,c("shortnam", "logpgp95", "avexpr", "lat_abst", "logem4", "cons1")]

country.na <- apply(!is.na(d1), 1, all)
d2 <- d1[country.na, ]

tsls <- AER::ivreg(logpgp95 ~ avexpr + lat_abst | logem4 + lat_abst, data = d2)
print(tsls)



### Use dplyr 

dd = dplyr::filter(d0, apply(!is.na(d0), 1, all) ) # remove NA
dd1 = dplyr::select(d0, shortnam, logpgp95, avexpr, lat_abst, logem4, cons1) # select a subset