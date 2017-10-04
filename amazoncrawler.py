import urllib2
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import csv
import pandas as pd



ua = UserAgent()
headers = {'User-Agent':str(ua.chrome)}

def getReview(pageNumber):

    amazonReviewArray = [];
    pageNumber;
    page = urllib2.urlopen("https://www.amazon.com/Converse-Unisex-Chuck-Taylor-Sneakers/product-reviews/B01G2N1WKU/ref=cm_cr_arp_d_paging_btm_2?ie=UTF8&reviewerType=avp_only_reviews&pageNumber=" + str(pageNumber))

    # page = urllib2.urlopen("https://www.amazon.com/adidas-CQ1190-Womens-Originals-Superstar/product-reviews/B01N2W6F8A/ref=cm_cr_getr_d_paging_btm_4?ie=UTF8&reviewerType=avp_only_reviews&pageNumber=" + str(pageNumber))
    soup = BeautifulSoup(page)
    soupString = str(soup)
    beforeReview = soupString.split('review-body">',1)[1];

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


# theReview = review;
# amazonReviewArray = theReview;
# # print(text);

# def setupColumns():
#   with open('reviews.csv', 'w') as outfile:
#     mywriter = csv.writer(outfile)
#     mywriter.writerow(['review'])


# setupColumns();

# #save comments to CSV file
theReviewsOutput = getAllReviews(20)

df = pd.DataFrame(theReviewsOutput, columns=["review"])
df.to_csv('reviews.csv', index=False)

# with open('reviews.csv', 'wb') as myfile:
#     wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
#     wr.writerow(theReviewsOutput)

# theFile = open('reviews.csv', 'w')
# wr = csv.writer(theFile, quoting=csv.QUOTE_ALL)
# wr.writerow(theReviewsOutput)

# for theReviews in theReviewsOutput:

#     theFile = open('reviews.csv', 'a')
#     mywriter = csv.writer(theFile)

#     print(theReviews)
#     mywriter.writerow(theReviews)


#     print("Done")
# print("Why is it noneeeee" + str(getAllReviews(5)));










# headers = {'User-Agent':str(ua.chrome)}

# try:
#     for pageNumber in range(3):

#         pageNumber = pageNumber + 1;
#         page = urllib2.urlopen("https://www.amazon.com/adidas-CQ1190-Womens-Originals-Superstar/product-reviews/B01N2W6F8A/ref=cm_cr_getr_d_paging_btm_4?ie=UTF8&reviewerType=avp_only_reviews&pageNumber=" + str(pageNumber))
#         soup = BeautifulSoup(page)
#         soupString = str(soup)
#         beforeReview = soupString.split('review-body">',1)[1];

#         for reviewNumber in range(10):

#             theReview = beforeReview.split('</span>',1)[0]
#             print("\n\n" + theReview);

#             if(reviewNumber < 9):
#                 beforeReview = beforeReview.split('review-body">',1)[1];
#             else:
#                 break;

# except urllib2.HTTPError as err:
#    if err.code == 503:
#         print("There's an error")



# def getReview(pageNumber)



# # import urllib2
# # from bs4 import BeautifulSoup

# # for pageNumber in range(10):

# #     headers = {'User-agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36'}


# #     pageNumber = pageNumber + 1;
# #     page = urllib2.urlopen("https://www.amazon.com/adidas-CQ1190-Womens-Originals-Superstar/product-reviews/B01N2W6F8A/ref=cm_cr_getr_d_paging_btm_4?ie=UTF8&reviewerType=avp_only_reviews&pageNumber=" + str(pageNumber))
# #     soup = BeautifulSoup(page)
# #     print(str(soup).count("review-body"));
# #     print(str(soup).split('review-body', 2));