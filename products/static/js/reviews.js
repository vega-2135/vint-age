document.addEventListener('DOMContentLoaded', function() {
const editButtons = document.getElementsByClassName("btn-review-edit");
const reviewText = document.getElementById("id_content");
const reviewForm = document.getElementById("reviewForm");
const submitButton = document.getElementById("submitButton");
const scrollTo = document.getElementById("scroll-here")

const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-review-delete");
const deleteConfirm = document.getElementById("deleteConfirm");

// Get the close and cancel confirmation window's buttons 
const closeModalButton = document.getElementById("close-review-modal")
closeModalButton.addEventListener('click', closeConfirmationWindow);

function closeConfirmationWindow() {
  deleteModal.hide();
}


/**
* Initializes edit functionality for the provided edit buttons.
* 
* For each button in the `editButtons` collection:
* - Retrieves the associated reviews's ID upon click.
* - Fetches the content of the corresponding review.
* - Populates the `reviewText` input/textarea with the reviews's content for editing.
* - Updates the submit button's text to "Update".
* - Sets the form's action attribute to the `edit_review/{reviewId}` endpoint.
*/
for (let button of editButtons) {
  button.addEventListener("click", (e) => {
    let reviewId = e.target.getAttribute("review_id");
    let reviewContent = document.getElementById(`review${reviewId}`).innerText;
    reviewText.value = reviewContent;
    submitButton.innerText = "Update";
    reviewForm.setAttribute("action", `edit_review/${reviewId}`);
    scrollTo.scrollIntoView({behavior: 'smooth'});
  });
}

/**
* Initializes deletion functionality for the provided delete buttons.
* 
* For each button in the `deleteButtons` collection:
* - Retrieves the associated review's ID upon click.
* - Updates the `deleteConfirm` link's href to point to the 
* deletion endpoint for the specific review.
* - Displays a confirmation modal (`deleteModal`) to prompt 
* the user for confirmation before deletion.
*/
for (let button of deleteButtons) {
  button.addEventListener("click", (e) => {
    let reviewId = e.target.getAttribute("review_id");
    deleteConfirm.href = `delete_review/${reviewId}`;
    deleteModal.show();
  });
}
});