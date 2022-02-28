## KARSALES_Data-collection-and-Analysis.

* Created a tool that estimates car sale price to help customers buy car at the price the car should be paid.
* Scraped over 30.000 price and information using python and selenium.
* Optimized Linear, Lasso, and Random Forest Regressors using GridsearchCV to reach the best model.
* Built a client facing API using flask (upcoming).
## Code and Resources Used
**Python Version:** 3.7  
**Packages:** pandas, numpy, sklearn, matplotlib, seaborn, selenium
**For Web Framework Requirements:**  ```pip install -r requirements.txt```  
**Flask Productionization:** https://towardsdatascience.com/productionize-a-machine-learning-model-with-flask-and-heroku-8201260503d2
## Web Scraping
Tweaked the web scraper github repo (above) to scrape 1000 job postings from glassdoor.com. With each job, we got the following:
*	Hãng
*	Dòng xe
*	Giá
*	Số Chỗ
*	số Km đã chạy
*	Tình Trạng
*	Năm sản Xuất
*	Hộp số
*	Nhiên liệu
*	Xuất sứ
*	Kiểu Dáng
*	Links
## Data Cleaning
After scraping the data, I needed to clean it up so that it was usable for our model. I made the following changes and created the following variables:
