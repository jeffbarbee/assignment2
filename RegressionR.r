dataset <- read.csv("regression_data.csv")

plot(dataset$YearsExperience, dataset$Salary, col="red")

model <- lm(Salary ~ YearsExperience, data=dataset)

library(ggplot2)
ggplot() +
  geom_point(aes(x = dataset$YearsExperience, y = dataset$Salary), colour = 'red') +
  geom_line(aes(x = dataset$YearsExperience, y = predict(model, newdata = dataset)), colour = 'blue') +
  ggtitle('Salary vs Experience') +
  xlab('Years of experience') +
  ylab('Salary') +
    theme_classic() #My little touch

summary(model)


