import urllib2
from bs4 import BeautifulSoup



headers = {'User-agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36'}


# pageNumber = pageNumber + 1;
page = urllib2.urlopen("https://www.amazon.com/adidas-CQ1190-Womens-Originals-Superstar/product-reviews/B01N2W6F8A/ref=cm_cr_getr_d_paging_btm_4?ie=UTF8&reviewerType=avp_only_reviews&pageNumber=4")
soup = BeautifulSoup(page)
soupString = str(soup)

beforeReview = soupString.split('review-body">',1)[1];
theReview = beforeReview.split('</span>',1)[0]
print("\n\nThis is the fucking review: \n\n " + theReview);



beforeReview1 = beforeReview.split('review-body">',1)[1];
theReview2 = beforeReview1.split('</span>',1)[0]
print("\n\nThis is the fucking review 2: \n\n " + theReview2);




# # import urllib2
# # from bs4 import BeautifulSoup

# # for pageNumber in range(10):

# #     headers = {'User-agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36'}


# #     pageNumber = pageNumber + 1;
# #     page = urllib2.urlopen("https://www.amazon.com/adidas-CQ1190-Womens-Originals-Superstar/product-reviews/B01N2W6F8A/ref=cm_cr_getr_d_paging_btm_4?ie=UTF8&reviewerType=avp_only_reviews&pageNumber=" + str(pageNumber))
# #     soup = BeautifulSoup(page)
# #     print(str(soup).count("review-body"));
# #     print(str(soup).split('review-body', 2));