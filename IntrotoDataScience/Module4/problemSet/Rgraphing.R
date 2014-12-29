library(ggplot2)

setwd('/home/kevin/Dropbox/courses/Udacity/DataScience/IntrotoDataScience/Module4/problemSet')

turnstile_weather = read.csv('turnstile_data_master_with_weather.csv')
# add 1 to any 0 Entries data
turnstile_weather$ENTRIESn_hourly = turnstile_weather$ENTRIESn_hourly + 1
rain = turnstile_weather[turnstile_weather$rain == 1, ]
norain = turnstile_weather[turnstile_weather$rain == 0, ]

plot_time = function(turnstile_weather) {
    plot = ggplot(turnstile_weather, aes(Hour, ENTRIESn_hourly, color = UNIT)) +
                    geom_jitter() + theme(legend.position="none")
    return(plot)
}

plot_time(turnstile_weather)

plot_hist = function(turnstile_weather, rain_type) {
    plot = ggplot(turnstile_weather, aes(x=ENTRIESn_hourly)) + 
                  geom_histogram(binwidth=10) +
                  ggtitle(paste('Histogram of Entries with', rain_type, 'weather')) +
                  xlab('entries') + 
                  ylab('frequency') #+
                  #scale_x_continuous(limits = c(0, 100000))
    return(plot)
}

plot_hist(turnstile_weather, 'rainy and not rainy')
plot_hist(rain, 'rainy') # histogram of rainy days
plot_hist(norain, 'not rainy') # histogram of no rain

# plot the number of rainy versus non-rainy times
plot_rainvsnorain = function(turnstile_weather) {
    plot = ggplot(turnstile_weather, aes(x=factor(rain), y=ENTRIESn_hourly)) +
                  geom_bar(stat = 'identity', colour='black') +
                  ggtitle('Number of entries, rainy vs not rainy') +
                  xlab(c('weather', 'No. of entries')) + 
                  scale_x_discrete(breaks=c("0", "1"), labels=c('not rainy', 'rainy')) 
    return(plot)
}

plot_rainvsnorain(turnstile_weather)

plot_dayofweek = function(dat) {
    dat$DATEn = factor(weekdays(as.Date(dat$DATEn), abbreviate=T), levels = c('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'))
    plot = ggplot(dat, aes(DATEn, ENTRIESn_hourly)) +
                  geom_boxplot() + 
                  scale_y_log10() +
                  xlab('Weekday') +
                  ylab('Hourly entries') +
                  ggtitle('Daily subway ridership')
        
    return(plot)
}

plot_dayofweek(turnstile_weather)
