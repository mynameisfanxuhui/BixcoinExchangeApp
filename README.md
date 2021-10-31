# BixcoinExchangeApp
## 1.How to build and run:
For client, go to client folder and run npm run serve.

For server, go to server and run sh run.sh.

The server I use is Python and Flask.

Install Flask, schedule and requests-cache package.
## 2.Questionnaire:

### 1. Are there any sub-optimal choices( or short cuts taken due to limited time ) in your implementation?
Yes. I did not implement database system.
### 2. Is any part of it over-designed? ( It is fine to over-design to showcase your skills as long as you are clear about it)
I define compare function in coin model. So in the future, if there is any changes like using machine learning to calculate rank score and other metrics. It will be 
easy to implement.
### 3.If you have to scale your solution to 100 users/second traffic what changes would you make, if any?
I currently use python's own requests_cache package to cache the request for the source data in one minute. So any users who request to get the price information will
not cause the server to request other sources again and again. I set the cache to timeout in one minute since if the source price change in one minute, the users can
endure this off. If the server is deployed to the cloud like using AWS. I may use AWS API Gateway for caching.
### 4.What are some other enhancements you would have made, if you had more time to do this implementation
I have not had enough time for database. I already designed a refresh data services so that the data can be refreshed once an hour and stored. For recommendation, 
I can then use history for another metric(increasing or decreasing trend). There is also user log history, region and some other information. These can be used to 
machine learning features and generate ranking score.
Currently I do not have any fault-tolerance. What if the source is unstable or having request error? I can use history data or just showing error for these situations.
And of course it is a good idea to deploy the project to the cloud. It is much more flexibility and scalability and also save a lot of trouble since cloud services like
AWS is very mature and provides a lot of useful functions like AWS Certificate Manager for security.
