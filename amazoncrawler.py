import urllib2
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


ua = UserAgent()

# try:
#    urllib2.urlopen("some url")
# except urllib2.HTTPError as err:
#    if err.code == 404:
#        <whatever>
#    else:
#        raise

# headers = {'User-agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36'}
# headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
def getReview(pageNumber):
    pageNumber = pageNumber + 1;
    page = urllib2.urlopen("https://www.amazon.com/Converse-Unisex-Chuck-Taylor-Sneakers/product-reviews/B01G2N1WKU/ref=cm_cr_arp_d_paging_btm_2?ie=UTF8&reviewerType=avp_only_reviews&pageNumber=" + str(pageNumber))

    # page = urllib2.urlopen("https://www.amazon.com/adidas-CQ1190-Womens-Originals-Superstar/product-reviews/B01N2W6F8A/ref=cm_cr_getr_d_paging_btm_4?ie=UTF8&reviewerType=avp_only_reviews&pageNumber=" + str(pageNumber))
    soup = BeautifulSoup(page)
    soupString = str(soup)
    beforeReview = soupString.split('review-body">',1)[1];

    for reviewNumber in range(10):

        theReview = beforeReview.split('</span>',1)[0]
        print("\n\n" + theReview);

        if(reviewNumber < 9):
            beforeReview = beforeReview.split('review-body">',1)[1];
        else:
            break;


headers = {'User-Agent':str(ua.chrome)}


def getAllReviews(howManyPages):

    theCurrentPageNumber = 1;

    #uf TCPN is not 10 that means that it was 
    #not the original 10 input and that it 
    #was called from a 503 error
    # if(TCPN == 10):
    #     return;
    # if(TCPN == 11):
    #     theCurrentPageNumber = 1;
    #     theRange = TCPN - 1
    # else:
    #     theCurrentPageNumber = TCPN;
    #     theRange = 10 - TCPN;

    for pageNumber in range(howManyPages):

        try:
           getReview(theCurrentPageNumber)
           theCurrentPageNumber = theCurrentPageNumber + 1;
           print("The current page number is " + str(theCurrentPageNumber));
           if(theCurrentPageNumber == howManyPages):
                return;

        except urllib2.HTTPError as err:
           if err.code == 503:
                print("There's an error on page: " + str(theCurrentPageNumber))
                # getAllReviews(theCurrentPageNumber);
                # if(theCurrentPageNumber == 10):
                #     return;

getAllReviews(20);










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