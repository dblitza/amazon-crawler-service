var amazon = require('amazon-product-api');

var client = amazon.createClient({
  awsId: "aws ID",
  awsSecret: "aws Secret",
  awsTag: "aws Tag"
});





// var AmazonReviews = require('amazon-reviews');


// AmazonReviews.getReview({
//         productId: 'B00DFFT76U',
//         reviewId: 'RDQO5C2XEPVPC'

// 	}, function(err, review) {
	  
// 	  	console.log(review)
// 	});



// // getReview
// //         productId: 'B00DFFT76U'
// //         reviewId: 'RDQO5C2XEPVPC'
// //       ,
// //         (err, review) ->
// //           should.not.exist err
// //           should.exist review
          
// //           review.title.should.equal 'Swaddlers vs Cruisers Size 4'
// //           review.starCount.should.equal 5
// //           should.exist review.descText
// //           should.exist review.profile
// //           review.profile.name.should.equal 'Rebecca N'
// //           review.profile.id.should.equal 'A276OI0NHBYORX'

// //           done()