import urllib2
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import csv
import pandas as pd


#headers
ua = UserAgent()
headers = {'User-Agent':str(ua.chrome)}

#get reviews from a specific page
def getReview(pageNumber):

    amazonReviewArray = [];
    pageNumber;
    #page URL
    page = urllib2.urlopen("https://www.amazon.com/Converse-Unisex-Chuck-Taylor-Sneakers/product-reviews/B01G2N1WKU/ref=cm_cr_arp_d_paging_btm_2?ie=UTF8&reviewerType=avp_only_reviews&pageNumber=" + str(pageNumber))

    soup = BeautifulSoup(page)
    soupString = str(soup)
    beforeReview = soupString.split('review-body">',1)[1];

    #extract every review from the page
    for reviewNumber in range(10):

        theReview = beforeReview.split('</span>',1)[0]
        # print("\n\n" + theReview);
        amazonReviewArray.append(theReview);

        if(reviewNumber < 9):
            beforeReview = beforeReview.split('review-body">',1)[1];
        else:
            break;
    # print("This is the array : Amazon Review Array " + str(number) + "   " + str(amazonReviewArray))

    # print(amazonReviewArray);
    return amazonReviewArray;



#return list of reviews from the page
#then append that list to all reviews
#then return ALL reviews

def getAllReviews(howManyPages):

    allAmazonReviewsArray = []
    theCurrentPageNumber = 1;
    for pageNumber in range(howManyPages):

        try:
           theReviewsFromPage = getReview(theCurrentPageNumber)
           # print(theReviewsFromPage)
           allAmazonReviewsArray.extend(theReviewsFromPage);
           # print(allAmazonReviewsArray)
           theCurrentPageNumber = theCurrentPageNumber + 1;
           print("Getting page ## " + str(theCurrentPageNumber-1));
           if(theCurrentPageNumber == howManyPages + 1):
                return allAmazonReviewsArray;

        except urllib2.HTTPError as err:
           if err.code == 503:
                print("There's an error on page: " + str(theCurrentPageNumber))
                # getAllReviews(theCurrentPageNumber);
                # if(theCurrentPageNumber == 10):
                #     return;
    # print("It is none" + allAmazonReviewsArray);


#get reviews of X amount of pages
theReviewsOutput = getAllReviews(20)


#export to CSCV
df = pd.DataFrame(theReviewsOutput, columns=["review"])
df.to_csv('reviews.csv', index=False)
print("All Done!");

