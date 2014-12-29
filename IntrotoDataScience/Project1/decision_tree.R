library(caret)

file_source <- '/home/kevin/Dropbox/courses/Udacity/DataScience/IntrotoDataScience/Project1/train.csv'

dat <- read.table(file_source, header=T, sep=",")
dat$Survived <- as.factor(dat$Survived)
dat$PassengerId <- as.factor(dat$PassengerId)
dat$Pclass <- as.factor(dat$PassengerId)
dat$Parch <- as.factor(dat$Parch)
dat$SibSp <- as.factor(dat$SibSp)
inTrain <- createDataPartition(y=dat$Survived, p=.8, list=F)
training <- dat[inTrain,]
testing <- dat[-inTrain,]
modFit <- train(Survived ~ ., method='rf', data=training, prox=T)
#print(modFit$finalModel)
modFit

# Accuracy of the model
pred <- predict(modFit, testing)
testing$predRight <- pred==testing$Survived
table(pred, testing$Survived)
