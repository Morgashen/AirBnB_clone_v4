const amenities = {};
$(document).ready(function () {
 let myAmenities = [];
  let myStates = [];
  let myCities = [];



  $('#review-toggle').click(function () {
    const reviewList = $('#review-list');
    const toggleText = $(this).text();

    if (toggleText === 'show') {

      fetchReviews();
      $(this).text('hide');
    } else {

      reviewList.empty();
      $(this).text('show');
    }
  });
});


function fetchReviews() {
  $.get('http://0.0.0.0:5001/api/v1/places/{{ place_id }}/reviews', function (reviews) {
    const reviewList = $('#review-list');
    reviewList.empty();

    $.each(reviews, function (index, review) {
      const reviewItem = $('<li>').text(`${review.text} (${review.user_id})`);
      reviewList.append(reviewItem);
    });
  });
}
