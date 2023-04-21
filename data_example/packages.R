# install missing packages

wanted <- (c("knitr", "tidyverse", "magrittr",
  "quantmod",
  "reshape2", "gridExtra",
  "doBy", "Quandl",
  "caret",
  "shiny"))

ins <- installed.packages()

missing <- setdiff(wanted, ins[,"Package"])

install.packages(missing)