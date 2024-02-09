# User Adoption Prediction Analysis

## Introduction

The purpose of this write up is to **identify which factors predict future user adoption**. An "*adopted user*" is defined as a user who *has logged into the product on three separate days in at least one seven-day period*.

## Data
2 datasets were provided:
1. `takehome_users` : 12,000 rows, 1 for each `object_id` (`user_id`) who signed up for the product in the last 2 years. Other columns incluse: `creation_time`, `last_session_creation_time`, `email`, `invited_by_user_id`, `org_id`, `invited_by_user_id` & `creation_source`.
2. `takehome_user_engagement` : 207,917 rows, 1 for each day that a user logged into the product. Columns include `user_id` and `time_stamp`.



## Data Cleaning

The `takehome_users_engagement` dataset was first used to create the target variable `adopted_user`. Only `8823` of the `12,000` `user_id`s from the `takehome_users` dataset were found in the `takehome_user_engagement` dataset. Since we did not have logging data for some `3177` `user_id`s, these `3177` `user_id`s were dropped from the `takehome_users` dataset as they would have been  missing data in the `adopted_user` column, out target variable. Coincidentally these dropped users were also missing data in the `last_session_creation_time` column.

With the `adopted_users` feature now merged into the `takehome_users` dataset, there were still some missing values in the `invited_by_user_id` column. These missing values were as their `creation_source` was not from an invite. A value of `00000` was filled in for these as that did not represent any other `user_id`.

## Exploratory Data Analysis

Categorical Features:
Most of the categorical features did not give any significant insights into the target variable. There were some anomilies in the data set which we took advantage of such as where `invited_by_user_id` was the same as `user_id`. This had a 28% adoption rate when compared to the 18.6% of the users who did not invite self.
Other small leans towards being an `adopted_user` were 
- `creation_source` for  `GUEST_INVITE` and `PERSONAL_PROJECTS` 
- `email` for `hotmail`

but these were minor portions of the dataset. 
Numerical Features:

comparing their violin plots of the 2 choices of the target variable, `adopted_user`.
- `Frequency` & all time-relations-between-logins features had a distinctly different distribution for the target variable but those could not be used as the targetvariable was created using those variable.
- `Recency` or the `days_since_last_login` was also very distinct and this could be used as it was a raw feature gidfted to us.
- `account_age` or the time between `creation_time` and `last_session_creation_time` was easily derived.

