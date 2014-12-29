library(ggplot2)

setwd('/home/kevin/Dropbox/courses/Udacity/DataScience/IntrotoDataScience/Module4/problemSet')
turnstile_weather = read.csv('turnstile_data_master_with_weather.csv')
turnstile_weather = turnstile_weather[,-1]

#ggplot(turnstile_weather, aes(Hour, ENTRIESn_hourly, color=UNIT)) + geom_jitter()

head(turnstile_weather)

# subset into fog-norain, fog-rain, nofog-norain, nofog-rain

# fog_norain
fog_norain <- turnstile_weather[turnstile_weather$fog == 1 & turnstile_weather$rain == 0, ]
sum(fog_norain$ENTRIESn_hourly) / nrow(fog_norain)

# fog_rain
fog_rain <- turnstile_weather[turnstile_weather$fog == 1 & turnstile_weather$rain == 1, ]
sum(fog_rain$ENTRIESn_hourly) / nrow(fog_rain)

# nofog_norain
nofog_norain <- turnstile_weather[turnstile_weather$fog == 0 & turnstile_weather$rain == 0, ]
sum(nofog_norain$ENTRIESn_hourly) / nrow(nofog_norain)

# nofog_rain
nofog_rain <- turnstile_weather[turnstile_weather$fog == 0 & turnstile_weather$rain == 1, ]
sum(nofog_rain$ENTRIESn_hourly) / nrow(nofog_rain)