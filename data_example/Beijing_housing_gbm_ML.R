library(caret)


load("lianjia.RData")
N <- nrow(lianjia) # a smaller sample
lianjia <- lianjia[base::sample(1:N, round(N * 0.05 )), ]

train_ind <- caret::createDataPartition(1:nrow(lianjia), p = 0.1)$Resample1

gbmGrid <- expand.grid(
  interaction.depth = seq(from = 10, to = 50, by = 30),
  n.trees = seq(from = 1000, to = 10000, by = 4000),
  shrinkage = c(0.01),
  n.minobsinnode = 20
)

gbmControl <- caret::trainControl(method = "cv", number = 5)


formula.GBM <- price ~
  square + livingRoom + drawingRoom + kitchen + bathRoom +
  floor_type + floor_total + elevator + ladderRatio +
  age + DOM + followers + fiveYearsProperty +
  subway + district + Lng + Lat + t_trade +
  communityAverage



####################
library(doParallel)
library(gbm)

gbmControl=trainControl(method="repeatedcv",number=5,repeats=1)

registerDoParallel(8)
t=Sys.time()
boostingReg=train(formula.GBM, 
                  data=lianjia[train_ind,],
                  method="gbm",
                  distribution="gaussian",
                  trControl=gbmControl,
                  tuneGrid=gbmGrid,
                  metric="Rsquared",
                  verbose=F)
cat("Time Cost of Finding Best Tuning Parameters:",Sys.time()-t,"\n")
doParallel::stopImplicitCluster()


######################33
gbmTune = boostingReg$bestTune
cat("The best tuning parameters for GBM are: \n");
print(gbmTune)

########################
pred.boosting=predict(boostingReg,newdata=lianjia[-train_ind,])

########################

lmReg=lm(formula.GBM, data=lianjia[train_ind,])
pred.lm=predict(lmReg,newdata=lianjia[-train_ind,])


# Comparison

target=lianjia[-train_ind,]$price
cat("R-squared of GBM prediction =",miscTools::rSquared(target,target-pred.boosting),"\n")
cat("R-squared of LM prediction =",miscTools::rSquared(target,target-pred.lm),"\n")
